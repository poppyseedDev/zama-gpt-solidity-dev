import os

def collect_files(input_dir, output_file, extensions, append=True):
    """
    Collects files with specified extensions from a directory and its subdirectories into one file.

    Args:
        input_dir (str): Path to the directory to search for files.
        output_file (str): Path to the output file where content will be written.
        extensions (list): List of file extensions to include (e.g., ['.md', '.ts', '.sol']).
        append (bool): Whether to append to the file (True) or overwrite it (False).
    """
    mode = 'a' if append else 'w'
    with open(output_file, mode, encoding='utf-8') as outfile:
        for root, _, files in os.walk(input_dir):
            for file in files:
                if any(file.endswith(ext) for ext in extensions):
                    file_path = os.path.join(root, file)
                    outfile.write(f"# File: {file_path}\n\n")
                    with open(file_path, 'r', encoding='utf-8') as infile:
                        outfile.write(infile.read())
                        outfile.write("\n\n")
    print(f"{'Appended' if append else 'Collected'} files into {output_file}")

def collect_only_specific_file(input_dir, output_file, target_file, append=True):
    """
    Collects a specific file from a directory into an output file.

    Args:
        input_dir (str): Path to the directory containing the file.
        output_file (str): Path to the output file where content will be written.
        target_file (str): Name of the specific file to collect.
        append (bool): Whether to append to the file (True) or overwrite it (False).
    """
    file_path = os.path.join(input_dir, target_file)
    print(file_path)
    if os.path.exists(file_path):
        mode = 'a' if append else 'w'
        with open(output_file, mode, encoding='utf-8') as outfile:
            outfile.write(f"# File: {file_path}\n\n")
            with open(file_path, 'r', encoding='utf-8') as infile:
                outfile.write(infile.read())
                outfile.write("\n\n")
        print(f"{'Appended' if append else 'Collected'} {target_file} into {output_file}")
    else:
        print(f"File {target_file} not found in {input_dir}")


# Collect Markdown files from fhevm (overwrite)
fhevm_docs_dir = "./modules/fhevm/docs"
fhevm_output_file = "./collected/fhevm_docs.md"
collect_files(fhevm_docs_dir, fhevm_output_file, ['.md'], append=False)

# Collect .ts, .sol, and README.md files from fhevm-hardhat-template
hardhat_template_dir = "./modules/hardhat"
hardhat_output_file = "./collected/hardhat_files.md"
hardhat_folders = ['./contracts', './deploy', './tasks', './test']
# Collect README.md from root of hardhat template (overwrite)
collect_only_specific_file(hardhat_template_dir, hardhat_output_file, "README.md", append=False)


# Loop through the specified folders and collect files (append)
for folder in hardhat_folders:
    print(f"Processing folder: {folder}")
    full_path = os.path.join(hardhat_template_dir, folder.lstrip('./'))
    if os.path.exists(full_path):
        collect_files(full_path, hardhat_output_file, ['.ts', '.sol'], append=True)
