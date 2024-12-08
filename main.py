import os

def collect_markdown_files(input_dir, output_file):
    """
    Collects all markdown (.md) files in a directory and its subdirectories into one file.
    
    Args:
        input_dir (str): Path to the directory to search for markdown files.
        output_file (str): Path to the output file where content will be written.
    """
    with open(output_file, 'w', encoding='utf-8') as outfile:
        for root, _, files in os.walk(input_dir):
            for file in files:
                if file.endswith('.md'):
                    file_path = os.path.join(root, file)
                    outfile.write(f"# File: {file}\n\n")  # Include file header
                    with open(file_path, 'r', encoding='utf-8') as infile:
                        outfile.write(infile.read())
                        outfile.write("\n\n")  # Separate files with new lines
    print(f"Collected all Markdown files into {output_file}")

# Example usage
input_directory = "./docs"  # Change this to your folder containing markdown files
output_file_path = "./collected_markdown.md"
collect_markdown_files(input_directory, output_file_path)
