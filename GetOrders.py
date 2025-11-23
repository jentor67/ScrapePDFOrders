#!/usr/bin/python3
"""
File: GetOrders.py
Project: ScrapPDFOrders
Author: John Major
Date: 2025-11-17
Description:  Extract orders from pdf
"""

import fitz
import glob
import os
import module
import csv

workingFile = "output/workingFile.pdf"
# set global position
xg = 0
yg = 0

# create a list
dataRows =[]

# create a list header record
line = [
    "HeartFlowRep",
    "phyNameX",
    "phyName",
    "dateOf"]

# add header record to dataRows list
dataRows.append(line)

# define class
ext = module.pdfTools()

# set the extension to be used
pdfFiles = (".pdf",".PDF")

# open each file and gather info
doc = fitz.open("input/test.pdf")
num_pages = doc.page_count

print(num_pages)

# set page
page = doc[0]

accountNumber = ext.getText(page, 7.7, .25, .7)
pageOfPages = ext.getText(page, 7.5, .25+.18, .8)
items = ext.getText(page, 7.65, .25+2*.18, .5)
pageNo = pageOfPages.split(" of ")[0].strip()
pages = pageOfPages.split(" of ")[1].strip()

for pg in range(num_pages):
    # set page
    page = doc[pg]

    accountNumber = ext.getText(page, 7.7, .25, .7)
    pageOfPages = ext.getText(page, 7.5, .25+.18, .8)
    items = ext.getText(page, 7.65, .25+2*.18, .5)

    pageNo = pageOfPages.split(" of ")[0].strip()
    pages = pageOfPages.split(" of ")[1].strip()

    print(accountNumber, items, pageNo, pages)

    if pageNo == "1" :
        #  Address Block 
        addrX=1
        addrY=2
        lineincrement=.18
        name = ext.getText(page, addrX, addrY, 3)
        address = ext.getText(page, addrX, addrY+lineincrement, 3)
        cityStateZip = ext.getText(page, addrX, addrY+2*lineincrement, 3)
        
        print(name,address,cityStateZip)

"""
    # assign values to each variable 

    # append variables to a list
    line = [
    HeartFlowRep,
    phyNameX,
    dateOf]

# append line values to dataRows
    dataRows.append(line)

# create file and and add data to csv
with open("output/output.csv", "w", newline="") as csvfile:
    writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
    writer.writerows(dataRows)
"""
# save to working file
doc.save(workingFile)
# close pdf
doc.close()
