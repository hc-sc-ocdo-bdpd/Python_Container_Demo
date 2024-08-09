import pytest
import os
import subprocess
import time
import json

@pytest.fixture(scope="module")
def memory_limit():
    """
    Fixture to read the memory limit from .devcontainer/devcontainer.json file.
    """
    try:
        with open("../.devcontainer/devcontainer.json", "r") as file:
            config = json.load(file)
            for arg in config.get("runArgs", []):
                if "--memory" in arg:
                    return int(arg.split(" ")[-1][:-1]) * 1024 ** 3  # Convert from GB to bytes
    except FileNotFoundError:
        pytest.skip("Skipping memory limit test as the configuration file was not found.")
    except Exception as e:
        pytest.fail(f"Failed to read memory limit from configuration file: {e}")

@pytest.mark.skipif(os.environ.get("CI") == "true", reason="Skipping resource tests in CI environment")
def test_memory_limiting(memory_limit):
    """
    Test that the container respects the memory limit.
    Purpose: Verify the container is killed if it exceeds the specified memory limit.
    """
    try:
        # Allocate memory in a loop to exceed the limit
        allocation_size = memory_limit + (1024 ** 3)  # Exceed by 1GB
        process = subprocess.Popen(["python", "-c", f"a = ' ' * {allocation_size}"], stderr=subprocess.PIPE)
        process.wait(timeout=30)
        # If the process is killed due to exceeding memory limit, returncode should be non-zero
        assert process.returncode != 0, "Process should be killed due to memory limit"
    except subprocess.TimeoutExpired:
        process.kill()
        pytest.fail("Process did not get killed despite exceeding memory limit")

@pytest.mark.skipif(os.environ.get("CI") == "true", reason="Skipping resource tests in CI environment")
def test_cpu_limiting():
    """
    Test that the container respects the CPU limit.
    Purpose: Verify the container is throttled if it exceeds the specified CPU limit.
    """
    start_time = time.time()
    
    # Perform a more CPU-intensive task
    process = subprocess.Popen(["python", "-c", "for i in range(10**9): pass"])
    process.wait()
    
    elapsed_time = time.time() - start_time
    
    # If the CPU is limited, the task should take longer than usual
    # Adjust the expected time threshold based on your environment
    assert elapsed_time > 8, f"Process should be throttled due to CPU limit, but it took only {elapsed_time} seconds"

