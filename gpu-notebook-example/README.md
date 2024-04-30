# Jupyter Notebook Example

## Introduction
This folder contains a demonstration Jupyter notebook called 'hello_world.ipynb' for Python development within a containerized environment.

## Install VSCode Remote Development Extension
- Open Visual Studio Code.
- Access the Extensions view by clicking on the Extensions icon in the Activity Bar on the side of the window, or by pressing `Ctrl+Shift+X`.
- Type `Remote Development` in the search bar.
- Locate the `Remote Development` extension pack by Microsoft and click on the install button.

## Working with Containers
### Rebuild and Reopen in Container
- To access the Command Palette, either press `Ctrl+Shift+P` or navigate to `View > Command Palette`.
- Choose `Dev Containers: Rebuild and Reopen in Container`.

### Switching Back to Local
- Open the Command Palette using `Ctrl+Shift+P` or by going to `View > Command Palette`.
- Select `Dev Containers: Reopen Folder Locally`.

## Verifying GPU visibility and Jupyter Notebook
- Navigate to the 'hello_world.ipynb' Jupyter notebook within the project.
- Click on 'Select Kernel' in the top right corner of the notebook interface.
- Choose 'Python Environments'.
- Select the 'Python 3.10.12' kernel for the correct Python environment.
- Run the top cell to confirm your gpu can be seen by the container. The expected printed output should be 'True' and the name of your GPU.


## CUDA and GPU Requirements
This project relies on specific versions of CUDA and GPU drivers to function correctly:
- **CUDA Version**: 12.2
- **NVIDIA-SMI**: 536.45
Ensure that your development environment matches these specifications to avoid compatibility issues.


For additional Docker setup instructions, refer to the main project's [README](../README.md).
