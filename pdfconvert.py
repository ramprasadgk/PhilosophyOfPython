# importing required modules 
import PyPDF2 
import types



# creating a pdf file object 
pdfFileObj = open('D:\\sample.pdf', 'rb') 

# creating a pdf reader object 
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

page = print(pdfReader.getPage(10))

