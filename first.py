#!/usr/bin/python3
import fitz
import module

doc = fitz.open("test.pdf")
page = doc[0]


ext = module.pdfTools()

workingFile = "workingFile.pdf"

xg = 0
yg = 0

HeartFlowRep = ext.getText(page, xg+37, yg+300, 400)
print(HeartFlowRep)

phyNameX = ext.getText(page, xg+35, yg+375, 15)
print(phyNameX)

phyName = ext.getText(page, xg+118, yg+375, 280)
print(phyName)

NPI = ext.getText(page, xg+450, yg+375, 100)
print(NPI)

siteNameX = ext.getText(page, xg+35, yg+405, 15)
print(siteNameX)

siteName = ext.getText(page, xg+118, yg+405, 450)
print(siteName)

address = ext.getText(page, xg+72, yg+438, 230)
print(address)

city = ext.getText(page, xg+330, yg+438, 120)
print(city)

state = ext.getText(page, xg+474, yg+438, 25)
print(state)

zip = ext.getText(page, xg+525, yg+438, 55)
print(zip)

website = ext.getText(page, xg+70, yg+465, 500)
print(website)

email = ext.getText(page, xg+65, yg+522, 230)
print(email)

phone = ext.getText(page, xg+340, yg+522, 100)
print(phone)

fax = ext.getText(page, xg+473, yg+522, 100)
print(fax)


fullName = ext.getText(page, xg+100, yg+665, 250)
print(fullName)

Title = ext.getText(page, xg+382, yg+665, 200)
print(Title)

dateOf = ext.getText(page, xg+482, yg+695, 135)
print(dateOf)
doc.save(workingFile)

doc.close()



