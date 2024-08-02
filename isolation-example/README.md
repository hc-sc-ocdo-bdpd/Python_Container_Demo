# Isolation Example

## Introduction
This folder demonstrates how to set up Docker containers with network isolation using the `--network none` flag. This approach helps mitigate risks when working with unknown packages and models. The example includes configuration files and tests to ensure the container cannot access any network resources.

Additionally, this setup includes dropping all Linux capabilities to further enhance security. Capability dropping ensures that the container has the least privileges necessary to operate, reducing the potential attack surface.

Moreover, resource limiting is configured to restrict the container's memory and CPU usage. This ensures that the container cannot consume excessive resources, which could impact the host system.

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

### Install Python Extension Inside the Container
- Once inside the container, open the Extensions view by clicking on the Extensions icon in the Activity Bar on the side of the window, or by pressing `Ctrl+Shift+X`.
- Type `Python` in the search bar.
- Locate the `Python` extension by Microsoft and click on the install button.

## Running the Tests
The `tests` directory contains various tests to ensure that the container cannot access network resources and respects resource limits. These tests include HTTP/HTTPS requests, DNS resolution, socket connections, FTP connections, ICMP ping requests, SMTP connections, HTTP/HTTPS uploads and downloads, and resource usage limits.

Additionally, a parameterized test is included to verify that specific Linux capabilities have been dropped from the container.

### Running Tests in VSCode
- Ensure you have the Python extension installed in the container as described above.
- Open the Command Palette using `Ctrl+Shift+P` or by going to `View > Command Palette`.
- Choose `Python: Configure Tests` and select `pytest` as the testing framework.
- Once configured, you will see a beaker icon (Flask icon) on the left side of the VSCode Activity Bar.
- Click on the beaker icon to access the Test Explorer.
- Click on the `Run Tests` button to run all tests in the `tests` directory.

## Configuration Files
- [.devcontainer/devcontainer.json](./.devcontainer/devcontainer.json)
- [Dockerfile](./Dockerfile)

## Resource Limiting
Resource limiting is configured to restrict the container's memory and CPU usage. 

### Changing Resource Limits
To modify the resource limits, such as increasing memory or CPU allocation, adjust the relevant parameters in the `.devcontainer/devcontainer.json` file's `runArgs` section. 

### Test Files
The `tests/test_network_isolation.py` file contains various tests to ensure network isolation:

- `test_http_https_requests`
- `test_dns_resolution`
- `test_socket_connection`
- `test_ftp_connection`
- `test_icmp_ping`
- `test_smtp_connection`
- `test_http_https_upload`
- `test_http_https_download`

The `tests/test_cap_drop.py` file contains a parameterized test to verify that specific Linux capabilities have been dropped:

- `test_capabilities` (parameterized to check the following capabilities):
  - `cap_chown`
  - `cap_kill`
  - `cap_setuid`
  - `cap_setgid`
  - `cap_mknod`
  - `cap_net_admin`
  - `cap_sys_time`
  - `cap_sys_module`
  - `cap_net_raw`
  - `cap_dac_override`
  - `cap_audit_write`
  - `cap_setfcap`

The `tests/test_resource_limiting.py` file contains tests to verify resource limiting:

- `test_memory_limiting`
- `test_cpu_limiting`

Refer to the test files for detailed test implementations and purposes.

For additional Docker setup instructions, refer to the main project's [README](../README.md).
