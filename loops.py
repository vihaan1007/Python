#LOOPS: they are used to repeat instructions
#like sending 100000 emails. Will you write manually?

#WHILE loop: they are just a syntax of loops

#printing numbers till 6
n = 0#iterator
while n < 6:#while and condition
    print(n)#work
    n += 1#updation
    #one iteration complete 
print("INTERVAL")
#while tells that this is a loop
#condition tells what to check each time it reapeats
#work tells what to do each time
#updation is for it to work without it the loop is INFINITE

#like errors infinite loops stop the whole code because the lines after it will only work when it will finish like a countdown to infinite which is impossible 

#numbers from 17 to 21
n = 17
while n < 21:
    print(n)
    n += 1
print("INTERVAL")
#all odd numbers from 1 to 12
n = 1
while n < 12:
    print(n)
    n += 2

#same for even starting is 0
#lets see how that odd number runs
#python checks if 1 < 12 which is TRUE then print(1) then update n to 3 ........ checks if 13 < 12 FALSE loop ends

#practice1
#print numbers from 1 to 100
n = 1
while n < 100:
    print(n)
    n += 1
print("INTERVAL")

#practice2
#print numbers from 100 to 1
n = 100
while n > 1:
    print(n)
    n -= 1
print("INTERVAL")

#practce3
#Print the multiplication table of n
n = int(input("Enter your number: "))
itr = 1
while itr < 10:
    print(n * itr)
    itr += 1
print("INTERVAL")

#practice4
#Print the elements of the following list using a loop:
#[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
n = 0
lis = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
while n < len(lis):
    print(lis[n])
    n += 1
print("INTERVAL")
#practice5
#Search for 36 in [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
x = 36
n = 0
lis = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
while n < len(lis):
    if(lis[n] == x):
        print(n)
    n+=1
print("INTERVAL")
#BREAK and CONTINUE
#break: used to terminate the loop when encountered
#continue: terminates execution in the current iteration & continues execution of the loop with the next iteration

#Search for 36 in [1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 36]
x = 36
n = 0
while n < len(lis):
    if(lis[n] == x):
        print(n)
        break#ends when 36 appears 
    n += 1
print("INTERVAL")
#print numbers 1 to 6 without 3
n = 1
while n < 6:
    if(n == 3):
        n +=1
        continue
    print(n)
    n += 1
print("INTERVAL")

#FOR loops: the other syntax of loops for traversal
lis = [1, 2, 3, 4]
for n in lis:#for, iterator, in, iterator of
    print(n)#work
    #no updation it is automatic
else:
    print("INTERVAL")#works when loop ends optional   

#practice1
lis = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
for n in lis:
    print(n)
else:
    print("INTERVAL")
#practice2
x = 49
idx = 0
for n in lis:
    if(n == x):
        idx += 1
        print(idx)
    idx += 1
else:
    print("INTERVAL")

#to give power to for use range
#range gives a sequence of numbers
#range(stop) or range(start, stop) or range(start, stop, step)
#start is 0 by default and step is 1

#even numbers from 1 to 11
for n in range(0, 11, 2):
    print(n)
else:
    print("INTERVAL")

#pass is used when you are leaving a loop with no work

#practice1
#WAP to find the sum of first n numbers
sum = 0
for n in range(1, 6):
    sum += n
else:
    print(sum)
    print("INTERVAL")

#practice2
#WAP to find the factorial of first n numbers
fact = 1
for n in range(1, 6):
    fact *= n
else:
    print(fact)
    print("INTERVAL")