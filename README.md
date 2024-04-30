# 🐍 Python Container and Jupyter Notebook Demos

## Introduction
This repository contains three demonstration projects: a containerized web application, a Jupyter notebook example, and a gpu-enabled notebook example. Each subfolder in this repository has its own README with specific instructions.

## Docker Setup

### Prerequisites
- Windows 10 machine with VS Code as the IDE.

### Installation Steps
1. Install Docker and WSL2 using local admin.
2. Add non-admin user names to the Docker user group: 
   ```net localgroup docker-users "your-user-id" /ADD```
3. Check Docker path settings in VS Code. They should simply read "docker".
4. Uninstall any conflicting containerization software like Podman.
5. Ensure Docker is running (as local admin) for the IDE to recognize it.

## Subfolders

### [Web App Example](./web-app-example)
The `web-app-example` folder contains a simple Flask-based web application. For more details on setup and usage, refer to its [README](./web-app-example/README.md).

### [Jupyter Notebook Example](./jupyter-notebook-example)
The `jupyter-notebook-example` folder showcases a Jupyter notebook setup. For instructions on accessing and using the notebook, see its [README](./jupyter-notebook-example/README.md).

### [GPU Notebook Example](./gpu-notebook-example)
The `gpu-notebook-example` folder contains minimal code to connect your container to your local gpu and use it in a Jupyter notebook. For usage details, see its [README](./gpu-notebook-example/README.md).
