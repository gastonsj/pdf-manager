from PyPDF2 import PdfMerger
import os

pdfs = [archivo for archivo in os.listdir('./') if archivo.endswith(".pdf")]
foldername="output_folder"
output_filename = "output.pdf"
fullpath=foldername + "//" + output_filename
print(fullpath)
isExist = os.path.exists(foldername)
if not isExist:
   # Create a new directory because it does not exist
   os.makedirs(foldername)

merger = PdfMerger()

for pdf in pdfs:
    merger.append(open(pdf, 'rb'))

with open(fullpath, 'wb') as salida:
    merger.write(salida)