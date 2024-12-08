import os
import json
from collect_files import collect_files, collect_only_specific_file
from to_pdf import convert_each_markdown_to_pdf
import submodules

def load_config(config_file):
    """
    Load the configuration from a JSON file.
    """
    try:
        with open(config_file, 'r') as file:
            return json.load(file)
    except Exception as e:
        print(f"Error loading config file: {e}")
        exit(1)

def update_submodules():
    print("\nUpdating submodules...")
    try:
        submodules.update_submodules()
        print("Submodules updated successfully.")
    except Exception as e:
        print(f"Error updating submodules: {e}")
        exit(1)

def collect_files_from_source(source_dir, output_file, folders, file_types):
    print(f"\nCollecting files from {source_dir}...")
    if not os.path.exists(source_dir):
        print(f"Source directory does not exist: {source_dir}")
        return

    # Collect README.md (overwrite)
    collect_only_specific_file(source_dir, output_file, "README.md", append=False)

    # Collect files from specified folders (append)
    for folder in folders:
        full_path = os.path.join(source_dir, folder.lstrip('./'))
        if os.path.exists(full_path):
            print(f"Processing folder: {full_path}")
            collect_files(full_path, output_file, file_types, append=True)
        else:
            print(f"Folder does not exist: {full_path}")

def convert_markdown_to_pdf(markdown_files):
    print("\nConverting Markdown files to PDF...")
    try:
        convert_each_markdown_to_pdf(markdown_files)
        print("PDF conversion completed.")
    except Exception as e:
        print(f"Error converting Markdown to PDF: {e}")

def main():
    # Load the configuration
    config = load_config("config.json")

    # Step 1: Update submodules
    update_submodules()

    # Step 2: Collect files
    collected_dir = config["collected_dir"]

    # Collect Markdown files from fhevm
    fhevm_config = config["submodules"]["fhevm"]
    fhevm_output_file = os.path.join(collected_dir, fhevm_config["output_file"])
    collect_files(fhevm_config["docs_dir"], fhevm_output_file, config["file_types"]["markdown"], append=False)

    # Collect files from hardhat
    hardhat_config = config["submodules"]["hardhat"]
    hardhat_output_file = os.path.join(collected_dir, hardhat_config["output_file"])
    collect_files_from_source(
        hardhat_config["source_dir"],
        hardhat_output_file,
        hardhat_config["folders"],
        config["file_types"]["code"]
    )

    # Collect files from contracts
    contracts_config = config["submodules"]["contracts"]
    contracts_output_file = os.path.join(collected_dir, contracts_config["output_file"])
    collect_files_from_source(
        contracts_config["source_dir"],
        contracts_output_file,
        contracts_config["folders"],
        config["file_types"]["code"]
    )

    # Step 3: Convert collected Markdown files to PDF
    markdown_files = [
        fhevm_output_file,
        hardhat_output_file,
        contracts_output_file
    ]
    convert_markdown_to_pdf(markdown_files)

if __name__ == "__main__":
    main()
