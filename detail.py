#!/usr/bin/python3
"""
File: detail.py
Project: ScrapePDFOrders
Author: John Major
Date: 2025-11-24
Description:  Detail extract data
"""
import fitz # PyMuPDF

class detail():
    def __init__(self):
        self.temp=1


    def getDetailLine(self,page,  x, y):
        idv = self.getText(page, x, y, 1)
        desc = self.getText(page, x+1.5, y, 2.9)
        loc = self.getText(page, x+4.5, y, 1)
        qty = self.getText(page, x+6.5, y, 1)

        return idv,desc,loc,qty


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
