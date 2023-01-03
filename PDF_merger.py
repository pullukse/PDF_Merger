#All files have to be in PDF format and located under the same folder.

import os
from PyPDF2 import PdfFileReader, PdfFileWriter

def merge_pdfs(paths, output):
    pdf_writer = PdfWriter()
    
    for path in paths:
        pdf_reader = PdfReader(path)
        for page in range(len(pdf_reader.pages)):
            # Add each page to the writer object
            pdf_writer.add_page(pdf_reader.pages[page])
    
    # Write out the merged PDF
    with open(output,'wb') as out:
        pdf_writer.write(out)
        
        
cwd = os.getcwd()
files = os.listdir(cwd)

#Ensure PDFs are in your current directory
files 
        
if __name__ == '__main__':
    paths = [#insert str (with .pdf) of the files to be merged by desired order of pages]
    merge_pdfs(paths, output = #insert str (with .pdf) desired for the output file name)
               
               
               
               
               
