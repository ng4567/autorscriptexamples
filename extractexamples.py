import urllib2
import PyPDF2
import os



path_to_pdf = "/Users/nikhilgopal/PycharmProjects/autorscriptexamples/tradestatistics.pdf"
pdfFileObj = open(path_to_pdf, 'rb')  # read the pdf
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

number_of_pages = pdfReader.numPages  # object that holds number of pages int he document
whole_pdf_document = []  # initialize a list to hold the pages of the pdf

path_to_text_file = "/Users/nikhilgopal/Pycharmprojects/autorscriptexamples/extractedpdf.txt"

temp_file_handle = open(path_to_text_file, "w")

for line in range(0, number_of_pages):  # iterate through the pdf document, write the pdf to a textfile

    pageObj = pdfReader.getPage(line)
    whole_pdf_document.append(pageObj.extractText())

    for line in whole_pdf_document: #decode uncode characters
        linee = line.encode('ascii', 'ignore').decode('ascii')
        temp_file_handle.write(linee)
    temp_file_handle.write("*****page break******")
    temp_file_handle.write("\n")
temp_file_handle.close()

list_of_function_names = []  # list to hold the names of the functions
temp_file_handle = open(path_to_text_file, "r")
for line in temp_file_handle:  # iterate through the documentation, save all of the function names and add them to a list
    if "........." in line:
        list_of_function_names.append(line[0:line.index('...')])


def parsefiles():
     copy = False
     function_number = 0
     example_code = []
     page_number = 1
     line_number = 1

     pdf_line_by_line = [line.rstrip('\n') for line in open(path_to_text_file)]  # initialize a list with

     for line in pdf_line_by_line:
        if line in list_of_function_names:
            copy = False
        elif "*****page break******" in line:
            copy = False
            page_number += 1
        elif "Examples" in line:
            copy = True
            example_code.append('\n')
            example_code.append("#")
            example_code.append(line)
            example_code.append('\n')
         elif copy == True:
            example_code.append(line)
            #print  "Line #/copy status: " + str(line_number) + "/" + str(copy)
            #print "line: " + str(line)
        line_number += 1


     #print list_of_function_names
     file_with_example_code_file_handle = open('examples.txt',  'w')

     for index in example_code:
        file_with_example_code_file_handle.write(index)
        print "index:" +  str(index)

     file_with_example_code_file_handle.close()
     #os.remove(path_to_pdf)
     #os.remove(path_to_text_file)
parsefiles()




'''if len(list_of_function_names) == 1:
for line in pdf_line_by_line:
if "*****page break******" in line:
 copy = False
 page_number += 1
elif "Examples" in line:
 copy = True
 example_code.append("#")
 example_code.append(line)
 example_code.append('\n')
elif copy == True:
 example_code.append(line)
 example_code.append("\n")
line_number += 1
else:
for line in pdf_line_by_line:
if function_number >= len(list_of_function_names):
    break
elif "*****page break******" in line:
   copy = False
   page_number += 1
elif line == list_of_function_names[1]:
   copy = False
   function_number = 2
elif line == list_of_function_names[function_number]:
   copy = False
   function_number += 1
elif "Examples" in line:
   copy = True
   example_code.append('\n')
   example_code.append("#")
   example_code.append(line)
   example_code.append('\n')

elif copy == True:
   example_code.append(line)
   example_code.append("\n")

line_number += 1


#print list_of_function_names[6]
print  "Line #/copy status: " + str(line_number) + "/" + str(copy)
print "line: " + str(line)
print "fcn number: " + str(function_number)
#print "length list of fcn names: " + str(len(list_of_function_names))
if function_number >= len(list_of_function_names):
pass
else:
print "current fcn: " + str(list_of_function_names[function_number])
'''