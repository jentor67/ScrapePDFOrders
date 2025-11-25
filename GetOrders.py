#!/usr/bin/python3
"""
File: GetOrders.py
Project: ScrapPDFOrders
Author: John Major
Date: 2025-11-17
Description:  Extract orders from pdf
"""

import fitz
import module
import detail as d

# set the working files
workingFile = "output/workingFile.pdf"


# set global position
xg = 0
yg = 0


# define class
ext = module.pdfTools()
det = d.detail()


# set the doc
doc = fitz.open("input/test.pdf")
num_pages = doc.page_count # get page numbers

print(num_pages)

# set page
page = doc[0]


detailStartX = .5
rowHeight = 1


for pg in range(num_pages):
    # set page
    page = doc[pg]

    ## collect essential values
    accountNumber = ext.getText(page, 7.7, .25, .7)
    pageOfPages = ext.getText(page, 7.5, .25+.18, .8)
    items = ext.getText(page, 7.65, .25+2*.18, .5)
    pageNo = pageOfPages.split(" of ")[0].strip()
    pages = pageOfPages.split(" of ")[1].strip()

    print(accountNumber, items, pageNo, pages)

    detailStartY = 1.33
    detailLines =9
    if pageNo == "1" :
        detailStartY=4.23
        detailLines = 6
    
        #  Address Block 
        addrX=1
        addrY=2
        lineincrement=.18
        name = ext.getText(page, addrX, addrY, 3)
        address = ext.getText(page, addrX, addrY+lineincrement, 3)
        cityStateZip = ext.getText(page, addrX, addrY+2*lineincrement, 3)
        
        print(name,address,cityStateZip)


    # collect detail
    for detailLine in range(detailLines):
        i = detailLine
        idV, description, location, qty = det.getDetailLine(page, \
                detailStartX, detailStartY+rowHeight*detailLine)

        # test if at the end of the detail
        if len(idV) > 0 :
            detailLine = 1000
            print(idV, description, location, qty)


# save to working file
doc.save(workingFile)
# close pdf
doc.close()
