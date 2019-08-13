import wget #import necessary libraries
import PyPDF2
import os

abspath = os.path.abspath(__file__) #change working  directory to where the script is, so that document is written there
dname = os.path.dirname(abspath)
os.chdir(dname)

url= raw_input("Please enter the url to the package documentation: ")
wget.download(url, "file.pdf")

path_to_pdf = "file.pdf"
pdfFileObj = open(path_to_pdf, 'rb')  # read the pdf
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

number_of_pages = pdfReader.numPages  # object that holds number of pages int he document
whole_pdf_document = []  # initialize a list to hold the pages of the pdf

path_to_text_file = "holdingfile.txt"

temp_file_handle = open(path_to_text_file, "w") 

for line in range(0,number_of_pages): #iterate through the pdf document, add each page to its own index in the list
     pageObj = pdfReader.getPage(line)
     whole_pdf_document.append(pageObj.extractText())
     linee = whole_pdf_document[line].encode('ascii', 'ignore').decode('ascii')
     temp_file_handle.write(linee)
     temp_file_handle.write("*****page break******")
     temp_file_handle.write("\n")
temp_file_handle.close()

list_of_function_names = []  # list to hold the names of the functions
temp_file_handle = open(path_to_text_file, "r") #need to reopen bc was previously in write mode
for line in temp_file_handle:  # iterate through the documentation, save all of the function names and add them to a list
    if "........." in line:
        list_of_function_names.append(line[0:line.index('...')])
pdfFileObj.close()
temp_file_handle.close()

def parsefiles():
     copy = False
     example_code = []
     line_number = 1
     function_number = 1
     page_break_blocked_line_numbers = [] #list for the line immdediately after examples, in case it is the same as the function name
     has_function_finished = True
     function_has_not_finished_protected_lines = []


     pdf_line_by_line = [line.rstrip('\n') for line in open(path_to_text_file)]  # initialize a list with
     file_with_example_code_file_handle = open('examples.txt',  'w')

     for line in pdf_line_by_line:
        if function_number >= len(list_of_function_names):
            break
        elif line_number in page_break_blocked_line_numbers:
            copy = False
        elif line == "Description":
            copy = False

            has_function_finished = True
        elif has_function_finished == False:
            if line == "*****page break******":
                copy = False
                page_break_blocked_line_numbers.append(line_number+1)
                page_break_blocked_line_numbers.append(line_number+2)
                function_has_not_finished_protected_lines.append(line_number+3)
            elif line in list_of_function_names:
                copy = False
                function_number += 1
                has_function_finished = True
            elif line_number in function_has_not_finished_protected_lines:
                copy = True
        elif "Examples" in line:
            example_code.append("\n")
            copy = True
            has_function_finished = False
        line_number += 1

        if copy == True:
            example_code.append(line)
        else:
            pass

     for line in example_code:
        file_with_example_code_file_handle.write("\n")
        file_with_example_code_file_handle.write(line)


     file_with_example_code_file_handle.close()  #close open files
     os.remove(path_to_text_file) #delete files not needed anymore
     print "Done"

     return True

parsefiles() #call function to extract example code (still reads apostrophes as new lines)

list_of_code =[]
with open("examples.txt", "rt") as code: #get the code into an iterabole format (list)
    for line in code:
        list_of_code.append(line)

apostrophe_lines = []
lines_to_not_write = []
index_counter = 0
for index in list_of_code: #figure out where the lines are that have apostrophes
    if index == "'\n" or index == "`\n":
        apostrophe_lines.append(index_counter)
        lines_to_not_write.append(index_counter-1)
        lines_to_not_write.append(index_counter)
        lines_to_not_write.append(index_counter+1)
    index_counter += 1

fh=open("test.txt","w")

line_number = 0
for line in list_of_code:  #merge the lines with apostrophes with the lines before and after, undoing the bad PDF scraping
    if line_number in lines_to_not_write:
        if line_number in apostrophe_lines:
            a= list_of_code[line_number-1]
            b=list_of_code[line_number]
            c=list_of_code[line_number+1]
            a=a.rstrip("\n")
            b=b.rstrip("\n")
            c=c.rstrip("\n")
            fh.write(a+b+c+"\n")
    else:
        fh.write(line)
    line_number += 1

fh.close()

list_of_code =[]
with open("test.txt", "rt") as code:
    for line in code:
        list_of_code.append(line)


apostrophe_lines = []
lines_to_not_write = []
index_counter = 0
for index in list_of_code: #do the same process again in case there are apostrophes next to each other
    if index == "'\n" or index == "`\n":
        apostrophe_lines.append(index_counter)
        lines_to_not_write.append(index_counter-1)
        lines_to_not_write.append(index_counter)
        lines_to_not_write.append(index_counter+1)
    index_counter += 1




fh=open("CodeExamples.txt","w")

line_number = 0
for line in list_of_code:
    if line_number in lines_to_not_write:
        if line_number in apostrophe_lines:
            a= list_of_code[line_number-1]
            b=list_of_code[line_number]
            c=list_of_code[line_number+1]
            a=a.rstrip("\n")
            b=b.rstrip("\n")
            c=c.rstrip("\n")
            fh.write(a+b+c+"\n")
    else:
        fh.write(line)
    line_number += 1

fh.close()



os.remove("test.txt") #delete unnecessary files
os.remove("examples.txt")
os.remove("file.pdf")

