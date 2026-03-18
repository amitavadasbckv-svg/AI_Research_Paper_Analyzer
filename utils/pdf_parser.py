import pdfplumber

def extract_text(file):
    text = ""
    first_page_text = ""

    with pdfplumber.open(file) as pdf:
        for i, page in enumerate(pdf.pages):
            page_text = page.extract_text() or ""
            text += page_text

            if i == 0:
                first_page_text = page_text

    return text, first_page_text