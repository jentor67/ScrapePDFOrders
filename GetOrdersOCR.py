#!/usr/bin/python3
"""
File: GetOrdersOCR.py
Project: ScrapPDFOrders with OCR
Author: John Major
Date: 2025-11-17
Description:  Extract orders from pdf
"""


from pdf2image import convert_from_path
import pytesseract

def ocr_pdf(pdf_path):
    images = convert_from_path(pdf_path)
    text = ""

    for i, img in enumerate(images):
        page_text = pytesseract.image_to_string(img)
        text += f"\n--- Page {i + 1} ---\n"
        text += page_text

    return text


pdf_text = ocr_pdf("input/testImage.pdf")
print(pdf_text)


