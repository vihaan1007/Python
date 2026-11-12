#LISTS: it is a data type in python which can store any data type in a set

emp_list = []
marks = [90, 95, 98, 87, 99]# lists
product = ["Chips", 1.99, 55, True, None]#float integer boolean string nonetype
#index -      0   ,   1 ,  2,   3 ,   4
#index-       -5  ,  -4 , -3,  -2 ,  -1 
print(marks)
print(type(product))#list
print(len(product))#5 only elements are included not the indivisual length of each
print(product[4])#None
#LISTS: they are mutable means you can change value of any index
marks[1] = 100
print(marks)
#slicing is same as strings
print(product[1:4])
print(product[0:])
print(product[:3])
print(product[-5:-2])

#LIST METHODS
list = [2, 1, 3]

list.append(4)# adds one element in the end
print(list)# 2, 1, 3, 4

list.sort()#sorts in ascending order
print(list)# 1, 2, 3, 4

list.sort(reverse = True)#sorts in descending order
print(list)# 4, 3, 2, 1

list.reverse()# reverses the list
print(list)# 1, 2, 3, 4

list.insert(1, 6)# adds the first value which is index to insert to the second value which is element
print(list)# 1, 6, 2, 3, 4

list.append(5)# 1, 6, 2, 3, 4, 5
list.remove(5)# removes first occurence of the element
print(list)# 1, 6, 2, 3, 4

list.pop(1)# removes the element at the given index. here, 6
print(list)# 1, 2, 3, 4

#TUPLES: they are same as list but they are immutable they cant be changed at any index like string

emp_tup = ()
tup1 = (1,)#comma is important because without it python treats it as a integer
prod = ("Kurkere", 0.99, 73, False)
#           0    ,   1 ,  2,   3
#          -4    ,   -3, -2,  -1
print(prod)
print(prod[1])
print(type(prod))#tuple
print(len(prod))#4
#no changing of index because it is immutable
#tuple slicing is same as all
print(prod[0:2])

#tuple methods

tup = (2, 1, 3, 1)
#      0, 1, 2, 3
print(tup.index(3))#2, returns the index of the first occurence of the element
print(tup.count(1))#2, returns the amount of occurences of the element in the tuple

#practice1
#WAP to ask the user to enter the name of their 3 favourite movies and store them in a list

mova = input("Enter the name of your favourite movie1: ")
movb = input("Enter the name of your favourite movie2: ")
movc = input("Enter the name of your favourite movie3: ")
movies = [mova, movb, movc]
print("Your favourite movies are: ", movies)

#practice2
#WAP to check if a list contains a palindrome of elements

pali = [1, 2, 3, 4, 3, 2, 1]
pali2 = pali.copy()
print(pali2)
pali2.reverse()
print(pali2)
if(pali2 == pali):
    print("the list is a palindrome")
else:
    print("The list is not a palindrome")

#practice3
#WAP to count the number of students with the "A" grade in the following list:
#["C", "D", "A", "A", "B", "B", "A"]
#Store the above values in a list & sort them from "A" to "D"

grades = ["C", "D", "A", "A", "B", "B", "A"]
print("The number of students with A grade are ", grades.count("A"))
grades.sort()
print("The grades from A to D are: ", grades)