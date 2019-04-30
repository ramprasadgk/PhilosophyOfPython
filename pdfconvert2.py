from pdfrw import PdfReader

x = PdfReader('C:\\Users\\user\\Downloads\\page-3.pdf')

print (x.pages[0].Parent.Kids.get())