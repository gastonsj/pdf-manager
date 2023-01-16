from PyPDF2 import PdfMerger
import os

pdfs = [archivo for archivo in os.listdir('./') if archivo.endswith(".pdf")]
nombre_archivo_salida = "output.pdf"
merger = PdfMerger()

for pdf in pdfs:
    merger.append(open(pdf, 'rb'))

with open(nombre_archivo_salida, 'wb') as salida:
    merger.write(salida)