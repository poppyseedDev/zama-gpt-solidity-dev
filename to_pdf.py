import os
from markdown_pdf import MarkdownPdf
from markdown_pdf import MarkdownPdf, Section

def convert_each_markdown_to_pdf(markdown_files):
    """
    Convert each markdown file in the list into a separate PDF.
    PDFs are saved in the collected/pdf directory.

    Args:
        markdown_files (list): List of paths to markdown files.
    """
    # Ensure the output directory exists
    pdf_dir = "./collected/pdf"
    os.makedirs(pdf_dir, exist_ok=True)

    for md_file in markdown_files:
        pdf = MarkdownPdf(toc_level=2)
        
        # Read the markdown content
        with open(md_file, 'r', encoding='utf-8') as file:
            content = file.read()
        
        # Add the content as a section
        pdf.add_section(Section(content))
        
        # Set metadata for the PDF
        pdf.meta["title"] = f"Documentation for {md_file}"
        pdf.meta["author"] = "Generated by markdown-pdf script"
        
        # Generate the output PDF filename in the pdf directory
        pdf_filename = os.path.basename(md_file).replace(".md", ".pdf")
        output_pdf = os.path.join(pdf_dir, pdf_filename)
        
        # Save the PDF
        pdf.save(output_pdf)
        print(f"Generated PDF: {output_pdf}")