import subprocess

def update_submodules():
    try:
        # Initialize and update submodules
        subprocess.run(["git", "submodule", "update", "--init", "--recursive"], check=True)
        print("Submodules initialized and updated.")

        # Update to the latest commit on the tracked branch
        subprocess.run(["git", "submodule", "update", "--remote", "--recursive"], check=True)
        print("Submodules updated to the latest commits on tracked branches.")

    except subprocess.CalledProcessError as e:
        print(f"Error during submodule update: {e}")
