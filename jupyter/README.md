# 🐍 Python_Container_Demo

## Introduction 
This is a demo project for containerized Python with Docker.

## Docker Setup

### Prerequisites
- Ensure you are using a Windows 10 machine with VS Code as the IDE.

### Installation Steps
1. Install Docker and WSL2 using local admin.
2. Add all relevant non-admin user names to the Docker user group: 
   ```net localgroup docker-users "your-user-id" /ADD```
3. Check the Docker path settings in VS Code. These should simply read "docker"; a full path does not seem to be required.
4. Uninstall any other containerization software, such as Podman, that may conflict with Docker.
5. Ensure Docker is running (using local admin) for the IDE to detect it.

## Install VSCode Remote Development Extension
- Open Visual Studio Code.
- Go to the Extensions view by clicking on the Extensions icon in the Activity Bar on the side of the window, or by pressing `Ctrl+Shift+X`.
- In the search bar, type `Remote Development`.
- Find the `Remote Development` extension pack by Microsoft and click on the install button.

## Working with Containers
### Rebuild and Reopen in Container
- To open the Command Palette, press `Ctrl+Shift+P` or go to `View > Command Palette`.
- Select `Dev Containers: Rebuild and Reopen in Container`.

## Switching Back to Local
### Reopen Folder Locally
- To open the Command Palette, press `Ctrl+Shift+P` or navigate to `View > Command Palette`.
- Choose `Dev Containers: Reopen Folder Locally`.

## Working with Jupyter Notebooks
- Navigate to the 'hello_world.ipynb' Jupyter notebook in the project.
- Click on 'Select Kernel' in the top right corner of the notebook interface.
- Choose 'Python Environments'.
- Select the 'Python 3.10.4' kernel to ensure the notebook runs with the correct Python environment.