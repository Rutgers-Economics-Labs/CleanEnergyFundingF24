# extract all the text from a PDF file and save it to a text file
# Usage: python load.py

import os
import PyPDF2

# create a folder to save text files
if not os.path.exists('texts'):
    os.makedirs('texts')

# open each pdf
for pdf in os.listdir('pdfs'):
    pdf_path = os.path.join('pdfs', pdf)
    with open(pdf_path, 'rb') as f:
        pdf_reader = PyPDF2.PdfReader(f)
        text = ''
        for page_num in range(len(pdf_reader.pages)):
            page = pdf_reader.pages[page_num]
            text += page.extract_text()
        text_path = os.path.join('texts', pdf.replace('.pdf', '.txt'))
        with open(text_path, 'w', encoding='utf-8') as out_file:
            out_file.write(text)