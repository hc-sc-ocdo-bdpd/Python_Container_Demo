# Web App Example

## Introduction
This subfolder contains a Python Flask-based web application designed to run in a Docker container. The application is a simple "Hello World" server.

## Setting Up the Development Environment

### Build the Docker Image
In the VS Code terminal, navigate to the web-app-example directory and run:
`docker build -t pythoncontainerdemo .`

## Running the Application

### Using Docker Compose
In the VS Code terminal, run:
`docker-compose up`

The web application should now be running on `localhost:5000`.

### Accessing the Web Application
Open a web browser and navigate to `http://localhost:5000`. You should see a "Hello World!" message.

For additional Docker setup instructions and details about the entire project, refer to the main [README](../README.md) in the repository.