import os
import pytest
import subprocess

@pytest.fixture(scope="module")
def test_file():
    # Create a temporary file for testing
    filename = "/workspace/test_file.txt"
    with open(filename, 'w') as f:
        f.write("Test file for security options.")
    yield filename
    # Cleanup after tests
    os.remove(filename)

@pytest.mark.parametrize("command, expected_output", [
    (['grep', 'NoNewPrivs', '/proc/self/status'], 'NoNewPrivs:\t1'),
])
def test_no_new_privileges(command, expected_output):
    """
    Test that the no-new-privileges option is enabled.
    """
    result = subprocess.run(command, capture_output=True, text=True, check=True)
    assert expected_output in result.stdout, f"Expected output '{expected_output}' not found in '{result.stdout}'"

@pytest.mark.parametrize("suid_file", [
    '/usr/bin/passwd',
    '/usr/bin/su'
])
def test_suid_file(suid_file):
    """
    Test that the container cannot gain new privileges through SUID.
    """
    try:
        # Try to run the SUID file
        result = subprocess.run([suid_file], capture_output=True, text=True)
        assert result.returncode != 0, f"SUID file {suid_file} executed successfully, which should not happen"
    except FileNotFoundError:
        pytest.skip(f"{suid_file} not found in the container")

@pytest.mark.parametrize("sgid_file", [
    '/usr/bin/chfn',
    '/usr/bin/newgrp'
])
def test_sgid_effect(sgid_file):
    """
    Test that the container cannot gain new privileges through SGID.
    """
    original_egid = os.getegid()
    try:
        # Run a command that should not change the effective group ID
        result = subprocess.run([sgid_file], capture_output=True, text=True)
    except subprocess.CalledProcessError as e:
        pytest.fail(f"Command {sgid_file} failed with error: {e}")
    
    new_egid = os.getegid()
    assert original_egid == new_egid, f"Effective group ID changed after running {sgid_file}, which should not happen"
