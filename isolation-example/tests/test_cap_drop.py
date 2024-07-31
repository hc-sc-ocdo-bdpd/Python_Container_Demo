import os
import pytest
import subprocess

@pytest.fixture(scope="module")
def test_file():
    # Create a temporary file for testing
    filename = "/workspace/test_file.txt"
    with open(filename, 'w') as f:
        f.write("Test file for capability drop.")
    yield filename
    # Cleanup after tests
    os.remove(filename)

def check_capability_dropped(cap_name):
    try:
        result = subprocess.run(['capsh', '--print'], capture_output=True, text=True, check=True)
        assert 'Current: =' in result.stdout and f'!{cap_name}' in result.stdout, f"{cap_name} not dropped"
    except subprocess.CalledProcessError as e:
        pytest.fail(f"capsh command failed with error: {e}")

@pytest.mark.parametrize("cap_name", [
    'cap_chown',       # The container cannot change ownership of files.
    'cap_kill',        # The container cannot send signals to other processes.
    'cap_setuid',      # The container cannot change the UID of the process.
    'cap_setgid',      # The container cannot change the GID of the process.
    'cap_mknod',       # The container cannot create special files.
    'cap_net_admin',   # The container cannot perform network administration tasks.
    'cap_sys_time',    # The container cannot change the system clock.
    'cap_sys_module',  # The container cannot load or unload kernel modules.
    'cap_net_raw',     # The container cannot use raw sockets.
    'cap_dac_override',# The container cannot bypass file read, write, and execute permission checks.
    'cap_audit_write', # The container cannot write to the audit log.
    'cap_setfcap'      # The container cannot set file capabilities.
])
def test_capabilities(cap_name):
    """
    Test that the specified capability is dropped.
    """
    check_capability_dropped(cap_name)
