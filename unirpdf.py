from PyPDF2 import PdfMerger
import os

pdfs = [archivo for archivo in os.listdir('./') if archivo.endswith(".pdf")]
nombre_archivo_salida = "salida.pdf"
fusionador = PdfMerger()

for pdf in pdfs:
    fusionador.append(open(pdf, 'rb'))

with open(nombre_archivo_salida, 'wb') as salida:
    fusionador.write(salida)