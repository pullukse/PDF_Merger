#All files have to be in PDF format and located under the same folder.

from PyPDF2 import PdfFileReader, PdfFileWriter

def merge_pdfs(paths, output):
    pdf_writer = PdfFileWriter()
    for path in paths:
        pdf_reader = PdfFileReader(path)
    for page in range (pdf_reader.getNumPages()) :
        # Add each page to the writer object
        pdf_writer.addPage(pdf_reader.getPage(page))
        # Write out the merged PDF
    with open(output,'wb') as out:
        pdf_writer.write (out)
        
if __name__ == '__main__':
    paths = [#insert str (with .pdf) of the files to be merged by desired order of pages]
    merge_pdfs(paths, output = #insert str (with .pdf) desired for the output file name)
               
               
               
               
               
