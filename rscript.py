import urllib2
import PyPDF2



url= 'https://cran.r-project.org/web/packages/stocks/stocks.pdf'
script_name = '\Desktop\stocksscript.pdf'

filedata = urllib2.urlopen(url) #download file
datatowrite = filedata.read()

'''
with open('C:\Users\NGopal1\Desktop', 'wb') as f:
    f.write(datatowrite)  #write the downloaded file to the given directory
    f.close()
'''

'''pdfFileObj = open("C:\Users\NGopal1\Desktop\scriptname.pdf", 'rb') #read the pdf
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

number_of_pages = pdfReader.numPages
whole_pdf_document = [] #initialize a list to hold the pages of the pdf
pageObj = pdfReader.getPage(0)
'''

temp_file_handle = open("tempfile.txt", "r")

'''for line in range(0,number_of_pages): #iterate through the pdf document, add each page to its own index in the list
     pageObj = pdfReader.getPage(line)
     whole_pdf_document.append(pageObj.extractText())
     temp_file_handle.write(whole_pdf_document[line])
     temp_file_handle.write("*****page break******")
'''


whole_pdf_line_by_line = temp_file_handle.readlines()

for index in whole_pdf_line_by_line:







