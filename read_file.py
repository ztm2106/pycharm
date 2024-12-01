#on example of reading text data from a file in python

#open the file

f = open("words.txt")

#when reading a file, python has access to a sequence of lines in the file
#we can use a for loop to access each line one at a time.

for line in f:
    #python does not remove the newline from text data as it is read
    #we can use a method called"rstrip" to remove any whitespace from the right side of the text
    print(line.rstrip())

f.close()