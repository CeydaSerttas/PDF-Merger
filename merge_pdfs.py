import os
from PyPDF2 import PdfMerger
from natsort import natsorted

INPUT_DIR = "pdfs"
OUTPUT_DIR = "output"
OUTPUT_FILE = "merged.pdf"

os.makedirs(OUTPUT_DIR, exist_ok=True)

all_files = os.listdir(INPUT_DIR)
pdf_files = natsorted([f for f in all_files if f.lower().endswith(".pdf")])

if not pdf_files:
    print("No PDF files found in the input directory.")
    exit(1)

merger = PdfMerger()

for pdf_file in pdf_files:
    pdf_path = os.path.join(INPUT_DIR, pdf_file)
    print(f"Adding {pdf_file} ...")
    merger.append(pdf_path)

output_path = os.path.join(OUTPUT_DIR, OUTPUT_FILE)
merger.write(output_path)
merger.close()

print(f"Merged PDF saved to {output_path}")
