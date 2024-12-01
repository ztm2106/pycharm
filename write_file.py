#an example of writing same text/data to a file using python

#open file in "write mode" so that we have a python variable where we can give data that will be saved to the file
f = open("sample_output.txt", "w")

#write method allows is to write/output a string to a file
#add new line  (\n)
f.write("Hello World!\n")
f.write("My Names is Zakiy")
#when done we need to close file
f.close()

