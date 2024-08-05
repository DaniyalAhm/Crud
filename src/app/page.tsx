
"use client";

import styles from "./page.module.css";
import { useState } from "react";
import axios from 'axios';
import Table from './Table'




export default function Home() {
  const [selectedFile, setSelectedFile] = useState(null);
  const [filePreview, setfilePreview]= useState(null);

  function handleSubmit(event) {
    event.preventDefault();
    console.log("File selected:", selectedFile);

    const formData = new FormData();
    formData.append('file', selectedFile);


    const response =  axios.post("http://localhost:5000/upload", formData, {
      headers: {
        'Content-Type': 'multipart/form-data'
      }})
      .then(response => {
        console.log("File uploaded successfully:", response.data);
        setSelectedFile(null);
        setfilePreview(null);
      })
      .catch(error => {
        console.error("Error uploading file:", error);
      });
    }


    


  

  function handleFileChange(event){
    const file = event.target.files[0];
    setSelectedFile(file)

    setfilePreview(URL.createObjectURL(event.target.files[0]))
  };


  return (
    <main className={styles.main}>
      <h1>

      Pantry Tracker
      </h1>
      <form onSubmit={handleSubmit} >
        <input type="file" id="myFile" name="filename" onChange={handleFileChange}  />
        <input type="submit" value="Submit" />
      </form>

{ 

(
      <img src= {filePreview}>
      </img>
)}


    <Table></Table>

    </main>

    



  )};

