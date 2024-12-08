import os
from collect_files import collect_files, collect_only_specific_file
from to_pdf import convert_each_markdown_to_pdf

def main():
    # Collect Markdown files from fhevm (overwrite)
    fhevm_docs_dir = "./modules/fhevm/docs"
    fhevm_output_file = "./collected/markdown/fhevm_docs.md"
    collect_files(fhevm_docs_dir, fhevm_output_file, ['.md'], append=False)

    # Collect .ts, .sol, and README.md files from fhevm-hardhat-template
    hardhat_template_dir = "./modules/hardhat"
    hardhat_output_file = "./collected/markdown/hardhat_files.md"
    hardhat_folders = ['./contracts', './deploy', './tasks', './test']
    # Collect README.md from root of hardhat template (overwrite)
    collect_only_specific_file(hardhat_template_dir, hardhat_output_file, "README.md", append=False)

    # Loop through the specified folders and collect files (append)
    for folder in hardhat_folders:
        print(f"Processing folder: {folder}")
        full_path = os.path.join(hardhat_template_dir, folder.lstrip('./'))
        if os.path.exists(full_path):
            collect_files(full_path, hardhat_output_file, ['.ts', '.sol'], append=True)

    # Collect .ts, .sol, and README.md files from fhevm-contracts
    contracts_template_dir = "./modules/contracts"
    contracts_output_file = "./collected/markdown/contracts-files.md"
    contracts_folders = ['./contracts', './tasks', './test/confidentialERC20', './test/governance', './test/utils']
    # Collect README.md from root of hardhat template (overwrite)
    collect_only_specific_file(contracts_template_dir, contracts_output_file, "README.md", append=False)

    # Loop through the specified folders and collect files (append)
    for folder in contracts_folders:
        print(f"Processing folder: {folder}")
        full_path = os.path.join(contracts_template_dir, folder.lstrip('./'))
        if os.path.exists(full_path):
            collect_files(full_path, contracts_output_file, ['.ts', '.sol'], append=True)


    # Convert markdown files to PDF
    print("\nConverting markdown files to PDF...")

    # List of Markdown files to convert
    markdown_files = [
        "./collected/markdown/fhevm_docs.md",
        "./collected/markdown/hardhat_files.md",
        "./collected/markdown/contracts-files.md"
    ]

    # Convert each Markdown file to a separate PDF
    convert_each_markdown_to_pdf(markdown_files)

if __name__ == "__main__":
    main()