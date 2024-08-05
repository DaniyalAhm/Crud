

# CRUD Application

This repository contains a CRUD (Create, Read, Update, Delete) application developed using a variety of technologies to ensure isolation, security, and efficiency.

## Overview

This project was instrumental in introducing me to TensorFlow. However, for this particular application, I opted to use Amazon Rekognition due to its advanced features and ease of integration.

## Features

- **Dockerized Environment**: The project is structured to run the backend and frontend in separate Docker containers. This approach ensures isolation between services, enhancing security and maintainability.
- **Backend**: Developed using Node.js and Flask, providing a robust and scalable server-side solution.
- **Frontend**: Built with React, offering a dynamic and responsive user interface.
- **Amazon Rekognition Integration**: Utilized for image analysis and recognition, providing powerful and accurate insights.

## Getting Started

### Prerequisites

- Docker
- Docker Compose

### Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/DaniyalAhm/Crud.git
   cd Crud
   ```

2. **Build and run the containers**:
   ```bash
   docker-compose up --build
   ```

### Usage

The application can be accessed via `http://localhost:3000` for the frontend and `http://localhost:5000` for the backend.

## Technologies Used

- **Frontend**: React
- **Backend**: Node.js, Flask
- **Image Analysis**: Amazon Rekognition
- **Containerization**: Docker

## Contributing

Contributions are welcome! Please fork the repository and create a pull request with your changes.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

- [TensorFlow](https://www.tensorflow.org/)
- [Amazon Rekognition](https://aws.amazon.com/rekognition/)
- [Docker](https://www.docker.com/)
- [React](https://reactjs.org/)
- [Node.js](https://nodejs.org/)
- [Flask](https://flask.palletsprojects.com/)

