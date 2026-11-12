print("Vihaan is my name.", "I am 10 years old.")#letters
print(23)#numbers
print(23 + 53)

name = "Vihaan"#str
age = 10#int
price = 99.99#float
isold = False#bool
cars = None#NoneType

print(type(name))#data types of variables function in function type in print
print(type(age))
print(type(price))
print(type(isold))
print(type(cars))

#Print Sum

a = 5
b = 2
sum = a + b
print(sum)

#CTRL + / multi line c = toggle in comment and uncomment
#comment start with # and dosent affect code execution

# operators - it is a symbol thatperforms a certain operation between oprands

#arithematic operators- they are for performing methamatical expressions
#a and b are defined above

sum = a + b# + is operator for add
diff = a - b# - is operator for difference
prod = a * b# * is operator for product
quot = a / b# / is operator for quotient
rema = a % b# % is operator for remainder
expo = a ** b# ** is operator for exponents
print("numbers are", a, "and", b)
print("sum = ", sum)
print("diff = ", diff)
print("product = ", prod)
print("quotient = ", quot)
print("remainder = ", rema)
print("exponent = ", expo)

#relational operators- they return boolean values True and False

print(a == b)# same; false
print(a != b)# not same; true
print(a > b)# greater than; true
print(a < b)# less than; false
print(a >= b)# greater than or equal to; true
print(a <= b)# less than or equal to; false

#assigment operators- they directly change the value of the variable- they are same as arithematic operators with a = in front

a += b
print(a)# 7
a -= b
print(a)# 5
a *= b
print(a)# 10
a /= b
print(a)# 5
a %= b
print(a)# 1
a **= b
print(a)# 1

#logical operators- not and and or

#not is true when the value is false and vice versa; It is opposite of the boolean value
#and is true when both values are true if one is false then false
#or any one is true then it is true

isFollowed = True
isOld = False
isYoung = True
isCoder = False

print(not isFollowed)# False
print(isFollowed and isOld)# False
print(isOld and isFollowed)# False
print(isFollowed and isYoung)# True
print(isOld or isYoung)# True
print(isCoder or isOld)# False

#Type conversion -> automatic; when possible

c = 5  #5.0 -> float
d = 2.1#2.1
suma = c + d#because of sum; must be same type; into the one which is more powerful
print(suma)#7.1

#Type casting -> manual

e = float("2")# 2.0 
f = float(4)# 4.0

#int() for integer, float() for float, bool() for boolean, none() for nonetype, str for string

#input- takes value from the user

name = input("enter your name: ")#prompt is "enter your name: " 
print(name)
# inputs value is always a string

#Practice 1
# WAP to input 2 numbers & print their sum.

numa = float(input("Enter your number 1: "))
numb = float(input("Enter your number 2: "))
print("The sum of", numa, "and", numb, "is", numa + numb)

#Practice 2
# WAP to input side of a cube & print its Volume, Diagnal, LSA and TSA

side = int(input("Enter the side of your cube in cm: "))
print("LSA: ", 4 * (side ** 2), "cm" , sep = "")
print("TSA: ", 6 * (side ** 2), "cm", sep = "")
print("Volume: ", side ** 3, "cm", sep = "")
print("Diagonal: ", side, "√2", "cm", sep = "")