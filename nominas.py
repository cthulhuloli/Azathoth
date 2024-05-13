import pdfplumber
import pytesseract
from PIL import Image
from pdf2image import convert_from_path

"""
estructura:
1. leer pdf recorrer archivo y extraer por pagionas el texto
2. puedo detectar 
el nombre es la 9 linea del pdf 
2. buscar dentro del rrecorido la casilla 
"""
pdf_path = 'C:\\Users\\AKK\\OneDrive\\nominas\\nomina.pdf'



def extract_text_from_pdf(pdf_path):
    text = ""
    with pdfplumber.open(pdf_path) as pdf:
        pages = pdf.pages
        for idx, page in enumerate(pages):
            images = convert_from_path(pdf_path, dpi=200, first_page=idx+1, last_page=idx+1)
            for img in images:
                text += pytesseract.image_to_string(img) + "\n"
    return text


# Extraer texto del PDF
extracted_text = extract_text_from_pdf(pdf_path)

# Imprimir el texto extraído
print(extracted_text)