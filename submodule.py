import os
import subprocess

def add_submodule(repo_url, submodule_path):
    """
    Adds a Git submodule to the specified path.
    
    Args:
        repo_url (str): URL of the Git repository to add as a submodule.
        submodule_path (str): Path where the submodule should be added.
    """
    if not os.path.exists(submodule_path):
        try:
            subprocess.run(["git", "submodule", "add", repo_url, submodule_path], check=True)
            subprocess.run(["git", "submodule", "update", "--init", "--recursive"], check=True)
            print(f"Submodule added to {submodule_path} successfully.")
        except subprocess.CalledProcessError as e:
            print(f"Error adding submodule: {e}")
    else:
        print(f"The folder {submodule_path} already exists. Skipping submodule addition.")

# Example usage
repo_url = "https://github.com/zama-ai/fhevm"
submodule_path = "./docs/fhevm"
add_submodule(repo_url, submodule_path)
