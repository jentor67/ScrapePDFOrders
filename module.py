#!/usr/bin/python3
import shutil
import fitz # PyMuPDF
import os
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import qrcode
from pdf2image import convert_from_path
from pyzbar.pyzbar import decode

class pdfTools():
    def __init__(self):
        self.temp=1

    def copy_pdf(self,input_path, output_path):
        shutil.copy(input_path, output_path)


    def getText(self,page, startXin, startYin, widthin):
        startX = startXin*72
        startY = startYin*72
        width = widthin*72
        # Define box coordinates: (x0, y0, x1, y1)
        endX = startX + width
        endY = startY + .18*72 # height of line

        rect = fitz.Rect(startX,startY, endX, endY)

        # Draw rectangle (border only)
        page.draw_rect(rect, color=(1, 0, 0), width=2)  # red outline

        # Extract text from that area
        value = page.get_text("text", clip=rect).strip() 
       

        return value
