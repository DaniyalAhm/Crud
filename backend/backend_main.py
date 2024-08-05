from flask import Flask, send_from_directory, jsonify, request
import requests
import os
from flask_cors import CORS
import firebase_admin
import boto3
from botocore.exceptions import EndpointConnectionError

from firebase_admin import credentials, firestore

cred = credentials.Certificate('crud-app-5cb08-firebase-adminsdk-8r60v-25a3eaa877.json')  # Replace with the path to your downloaded JSON file
firebase_admin.initialize_app(cred)
s3 = boto3.client('s3')
rekognition = boto3.client('rekognition',region_name='us-east-2')
response = s3.list_buckets()
print('Existing buckets:')
for bucket in response['Buckets']:
    print(f'  {bucket["Name"]}')


app = Flask(__name__)
token = os.environ.get('GITHUB_TOKEN')
CORS(app, origins=["http://localhost:3000"])

db = firestore.client()
bucket_name = 'asdsadssaddsad'

@app.route('/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    
    image = request.files['file']
    if image.filename == '':
        return jsonify({'error': 'No selected file'}), 400
    if image:
            filepath = os.path.join('upload', image.filename)
            image.save(filepath)

            classifcation = classify(filepath, image.filename)
            upload_to_firebase(classifcation)
            return jsonify({'message': 'File successfully uploaded', 'filepath': filepath, 'classification': classifcation})
    else:
        return jsonify({'error': 'Invalid file'}), 400
         

def classify(filepath,image_name):
    
     
     
    # Upload the file to S3
    try:
        s3.upload_file(filepath, bucket_name, image_name)
    except EndpointConnectionError as e:
        print(f"Failed to connect to the endpoint: {e}")
        return

    # Call the Rekognition API
    try:
        response = rekognition.detect_labels(
            Image={
                'S3Object': {
                    'Bucket': bucket_name,
                    'Name': image_name
                }
            },
            MaxLabels=10
        )
    except EndpointConnectionError as e:
        print(f"Failed to connect to the Rekognition endpoint: {e}")
        return
    best_confidence = 0
    best_label = ''
    for label in response['Labels']:
        print(f"Label: {label['Name']}, Confidence: {label['Confidence']:.2f}%")
        if 96 < label['Confidence']:
            best_confidence = label['Confidence']
            best_label += "-"+label['Name']

    return best_label



@app.route('/database', methods=["GET"])
def to_front_end():
    docs = db.collection('Items')
    items = docs.stream()
    item_list=[]
    for item in items:
        item_dict=item.to_dict()
        item_list.append(item_dict)
        


    return jsonify(item_list), 200





def upload_to_firebase(classification):
    docs = db.collection('Items')
    query = docs.where('title', '==', classification).limit(1)
    results = list(query.stream())
    if( not results):
         new = db.collection('Items').document()

         new.set({
            'title':classification,
            'quantity': 1

         })

    else:
        for doc in results:
        
            post_ref = db.collection('Items').document(doc.id)
            post_ref.update({
            'quantity': firestore.Increment(1) 
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)


# Initialize the S3 client

# Upload an image to S3

