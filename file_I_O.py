#FILE IO: python can be used to perform operations on a file. I/O means input and output
#there are two types of file. text files which contain text like .txt, .docx, .log. binary files dosent contain text they are bytes like .png, .jpeg, .mp3, .mp4, .mov

#open, read and close
#open is required to perform IO on a file
f = open("D:/Proggraming/python2/file.txt", "r")
#first is file path
#second is mode
data = f.read()#reads the data of the file
print(data)
f.close()#important for privacy and a mark of a good coder
#MODES
#r is for read
#w is for overwriting
#x is for creating a new file if exists then fail
#a is for appending directly after it ends
#b is for binary mode
#t is for text mode
#+ is for opening a disk file for updating
#r+ is for a and r
#w+ is for w and r
#a+ is for create if dosent exist, r and w

#line-by-line
f = open("D:/Proggraming/python2/file.txt", "r")
line1 = f.readline()
line2 = f.readline()
print(line1, line2, sep = "\n")
f.close()

#overwriting
f = open("D:/Proggraming/python2/file.txt", "w")
f.write("Changed")
f.close()
f = open("D:/Proggraming/python2/file.txt", "r")
data = f.read()
print(data, "Changed the data")
f.close()

#writing directly after
f = open("D:/Proggraming/python2/file.txt", "a")
f.write(" New thing")
f.close()
f = open("D:/Proggraming/python2/file.txt", "r")
data = f.read()
print(data, "Added on same line")
f.close()

#writing on new line
f = open("D:/Proggraming/python2/file.txt", "a")
f.write("\nNew line")
f.close()
f = open("D:/Proggraming/python2/file.txt", "r")
data = f.read()
print(data, "New line added")
f.close()

#with syntax

with open("D:/Proggraming/python2/file.txt", "r") as f:
    print(f.read())
#automatically closed

#deleting file
#using the os module
#module: it is a code written by another proggramer in which there are functions to use like a book of a library the name of the library is python and some modules are mini libraries like panda
with open("D:/Proggraming/python2/delete.txt", "x") as f:
    pass
import os
os.remove("D:/Proggraming/python2/delete.txt")#deletes

#practice1
#WAF to find the word "Learning" exists and if not found print(-1)
def find_word():
    word = "learning"
    with open("D:/Proggraming/python2/file.txt", "r") as f:
        data = f.read()
        if(data.find(word) != -1):
            print("Found")
        else:
            print(-1)

