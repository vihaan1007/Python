#STRINGS

#string is data type that stores a sequence of characters.

str1 = "A"#'' single quotes
str2  = "B"#"" double quotes
str3 = """C"""#"""""" triple quotes; three times double quotes
#all are valid
print(str1)
print(str2)
print(str3)
#use double quotes because single quotes will fail here:
str4 = "Hello this is our's"
print(str4)

#espace sequence characters are special words for formatting on a string like \n and \t for newline and tab space
str5 = "Hello.\n\tHello."
print(str5)

#adding two strings using + is called concatenation
a = "Apna"
b = "college"
concat = a + b
print(concat)#Apnacollege

#length of a string
print(len("Hello world"))#11 including spaces

#INDEXING- it is the name of characters on a string

# "APNA_COLLEGE"
#  012345678901 the end is 10 and 11 not 0 and 1

print(concat[0]) # since concat is Apnacollege 0 is A
print(concat[1])# p
print(concat[2])# n

#index can be done in negative by starting in the end which is -1 then going backwards -2 -3 -4 -5 -6 ........ -infinite
#you cant change the value of a indexing like variables

#SLICING- a part of a string str[start idx: end idx] end idx is not included
print(concat[2:5])# since concat is Apnacollege then "nac"

# str[1:] is same as str[1:len(str)] and str[:5] is same as str[0:5]

#string functions

str6 = "i am a coder"

print(str6.endswith("er"))#asks if endswith the substr or not. true

str6.capitalize()# capitalizes 1st index of the str
print(str6)

print(str6.replace("am", "we"))# replaces the 1st value with the second one

print(str6.find("a"))# returns 1st index of 1st occurence

print(str6.count("am"))# counts the number of occurence of the substr 

#practice1
#WAP to input user's first name and print its length

name = input("Enter your name: ")
print("The length of your name is: ", len(name))

#practice2
#WAP to find the occurence of $ in a string
d = "$HELLO$oo$$$E$"
print("The occurence of $ in this string is", d.count("$")) 

#CONDITIONAL STATEMENTS: It gives the ability to python to make decisons. This is where relational and assigment operators shine.

#if elif and else
#if is checked the first there is only 1 of this per condition
#elif is checked when if gives false there may be multiple elif
#else is there when all if and all elif fail else has no statement and is always true. it is one per condition

#a trafic light

color = "pink"
if(color == "green"):
    print("Go")
elif(color == "yellow"):
    print("Wait")
elif(color == "red"):
    print("Stop")
else:
    print("Your traffic light is broken")
#always 4 spaces or tab in VS Code called identation

marks = 97
if(marks >= 90):
    print("Grade A")
elif(marks >= 80 and marks < 90):
    print("Grade B")
elif(marks >= 70 and marks < 80):
    print("Grade C")
else:
    print("Failed")

#It can also be nested like if in if in if does the work of and
age = 34
if(age > 18):
    if(age < 80):
        print("Can drive")
    else:
        print("Cannot drive")
else:
    print("Cannot drive")

#practice1
#WAP to check if a number entered by the user is odd or even

num = int(input("Enter your number: "))
if(num % 2 == 0):
    print("Your number is even")
else:
    print("your number is odd")

#practice2
#WAP to find the greatest of 3 numbers entered by the user

numa = int(input("Enter your number1: "))
numb = int(input("Enter your number2: "))
numc = int(input("Enter your number3: "))

if(numa > numb):
    if(numa > numc):
        print("the number 1 is the greatest")
elif(numb > numc):
    if(numb > numa):
        print("the number 2 is the greatest")
else:
    print("the number 3 is the greatest")

#practice3
#WAP to check if a number is a multiple or not

numg = int(input("Enter your number: "))
if(numg % 7 == 0):
    print("The number is a multiple of 7")
else:
    print("The number is not a multiple of 7")