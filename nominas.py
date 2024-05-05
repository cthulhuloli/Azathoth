from PyPDF2 import PdfReader as pdf
import pdfplumber

"""
estructura:
1. leer pdf recorrer archivo
2.
2. buscar dentro del rrecorido la casilla 
"""
pdf_path = 'C:\Users\AKK\OneDrive\nominas\nomina.pdf'

"""
read_pdf = pdf(path)

name_list = []



number_of_pages = len(reader.pages)
page = reader.pages[0]
text = page.extract_text()

"""

def extract_text_from_pdf(pdf_path):
    text = ""
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            # Extraer texto de cada página
            page_text = page.extract_text()
            # Concatenar el texto de la página al texto total
            text += page_text + "\n"
    return text


# Extraer texto del PDF
extracted_text = extract_text_from_pdf(pdf_path)

# Imprimir el texto extraído
print(extracted_text)
