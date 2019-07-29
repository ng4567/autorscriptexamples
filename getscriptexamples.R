library(downloader)
library(Rd2md)

rdfile = "/Users/nikhilgopal/Downloads/stocks/man/convert_gain.rd"
outfile = "/Users/nikhilgopal/Downloads/stocks/samplefile.txt"

Rd2markdown(rdfile = rdfile, outfile = outfile)



url = "https://cran.r-project.org/src/contrib/stocks_1.1.4.tar.gz"
destfile = "/Users/nikhilgopal/Downloads/file.tar.gz"


download.file(url, destfile, method = "libcurl") #download the file
untar("/Users/nikhilgopal/Downloads/file.tar.gz", exdir = "/Users/nikhilgopal/Downloads") #unzip it



list_of_filenames <- list.files("/Users/nikhilgopal/Downloads/stocks/man") #get the list of files within the directory that has contains the information to be extracted
cwd = "/Users/nikhilgopal/Downloads/stocks/man/"



setwd("/Users/nikhilgopal/Downloads/stocks/man")
create_holding_file <- file.create("/Users/nikhilgopal/Downloads/holdingfile.txt")
file_that_holds_example_functions <- "/Users/nikhilgopal/Downloads/holdingfile.txt"

parsefiles <- function(filename){
  Rd2markdown(rdfile = filename, outfile = "/Users/nikhilgopal/Downloads/stocks/samplefile.txt")
  txt <- readLines(outfile) #variable that holds the lines being parsed
  line_number = 1 
  other_line_number = 1
  target_line_number <- 0  #initialize variable used to tell the computer if it should copy lines
  vector_to_hold_target_lines = c(filename)
  counter_variable_of_line_numbers = 1 
  
  
  for(line in txt) {
    if(grepl("Examples", line) == TRUE){
      target_line_number = line_number}
    line_number = line_number + 1
    }
    
  for(line in txt){
    if((other_line_number >= target_line_number + 1)&(line != "")&(line != " ``` ")&(line != "```r ")){
      counter_variable_of_line_numbers = counter_variable_of_line_numbers + 1
      vector_to_hold_target_lines[counter_variable_of_line_numbers] <- line
    }
    other_line_number = other_line_number + 1
    }  
    print(vector_to_hold_target_lines)
  }


parsefiles(list_of_filenames[1])



'
for(filename in list_of_filenames) { #iterate through all files in the directory
    file_being_parsed <- paste(cwd, list_of_filenames[counter], sep = "") #variable that tells the computer which file is being parsed at the current moment
    
    Rd2markdown(rdfile = file_being_parsed, outfile = outfile) 
    counter <- counter + 1
    txt <- readLines(outfile) #read the file 
    
    
    
    for(line in txt){ #read through the textfile line by line
      
      if(grepl("Example", line) == TRUE){ #if the word example is in the line, change the value of copy to True
       copy = TRUE
      }
    }
    return(TRUE)
}
  
  '''





