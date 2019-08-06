import urllib2
import PyPDF2

url= 'https://cran.r-project.org/web/packages/stocks/stocks.pdf'
script_name = 'stocksscript.pdf'

filedata = urllib2.urlopen(url) #download file
datatowrite = filedata.read()


with open('stockscript.pdf', 'wb') as f:
    f.write(datatowrite)  #write the downloaded file to the given directory
    f.close()


pdfFileObj = open("stockscript.pdf", 'rb') #read the pdf
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

number_of_pages = pdfReader.numPages
whole_pdf_document = [] #initialize a list to hold the pages of the pdf
pageObj = pdfReader.getPage(0)

#print pdfReader.getPage(0)
#print pdfReader.getPage(35)



temp_file_handle = open("tempfile.txt", "w")

for line in range(0,number_of_pages): #iterate through the pdf document, add each page to its own index in the list
     pageObj = pdfReader.getPage(line)
     whole_pdf_document.append(pageObj.extractText())
     temp_file_handle.write(whole_pdf_document[line])
     temp_file_handle.write("*****page break******")

#print whole_pdf_document

text_file_handle = open('tempfile.txt', 'r')

list = [] #list to hold the names of all of the functions in the documentation

for line in text_file_handle: #iterate through the documentation, save all of the function names and add them to a list
    if "........." in line:
        #print line
        list.append(line[0:line.index('...')])




text_file_handle = open('tempfile.txt', 'r')

array_of_array_of_strings = []

counter = 0
line_number = 1


new_array = []

copy = False

for line in text_file_handle:
    if "Examples\n" in line: #start copying when word examples is detected, because we only want example code
        copy = True


    if :



    if '*****page break******' not in line and copy == True:
        new_array.append(line)


    line_number += 1

print array_of_array_of_strings




