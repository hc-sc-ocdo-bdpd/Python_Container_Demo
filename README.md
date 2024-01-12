# Introduction 
This is a demo project for containerized Python with Docker.

# Setup

The following setup instructuions assumne a Windows 10 machine running with VS Code as the IDE.

1.	Install Docker and WSL2 using local admin.
2.	Add all relevant non-admin user names to the Docker user group: ```net localgroup docker-users "your-user-id" /ADD```
3.	Check the docker path settings in VS Code. These should simply read "docker", a full path does not seem to be required.
4.	Other containerization software, such as Podman, may cause conflicts with Docker and may need to be uninstalled.
