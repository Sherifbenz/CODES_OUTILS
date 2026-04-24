import os
from pypdf import PdfWriter

script_dir = os.path.dirname(os.path.abspath(__file__))
print(script_dir)
os.chdir(script_dir)

def merge_pdfs(pdf_list, output_path):
    writer = PdfWriter()

    for pdf in pdf_list:
        # Appends all pages from the specified PDF
        writer.append(pdf)

    with open(output_path, "wb") as output_file:
        writer.write(output_file)

    writer.close()

# Example usage
pdfs_to_merge = ["Diplome_Master_N.pdf", "Reconnaissance Master_N.pdf"]
merge_pdfs(pdfs_to_merge, "Master.pdf")
