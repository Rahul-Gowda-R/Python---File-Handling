#file handling / working with files:

#file: file is collection of data/information stored in a secondary storage device

#each file will be having filename for its identification and extension 
#name to identify its types

#example: myfile.txt:(my file is the name of the file and .txt is the extension name)

#example: .png , .docx , .pptx , .xlsx , .jpeg , .pdf , .csv.....

#file handling functions in python:
#read()
#readline()
#readlines()
#seek()
#open()
#close()

#steps to work with files:
#open the file---->read the data----->process the data------>close the file 


#open():
#filevariable=open("path\filename",:mode")
#opens the file from the given path and laods it to the memory

#mode:w write, a ppend mode, r read mode
#by default mode is read(r)



file1=open("E:/Rahul/Demo.txt")
data=file1.read()

print(data)

file1.close()