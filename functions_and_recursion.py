#FUNCTION: Block of statements that perform a specific task
#they can be reused as much as needed
#sum of a and b
def sum(a, b):#def function name and arguments or parameters
    return a + b#work and return
print(sum(5, 4))#function call

#def is the keyword to start a block of function
#function name tells to what name to call with
#arguments(/parameters) are the variable taken from the coder to use
#return ends a function and returns the value if you want to use it more useful for recursion
#function call calls a function when you need to use it in the example 5 and 4 were the arguments value in the order of a then b

#no parameter is possible
def hello():
    print("hello")

#nothing
def nothing(a, b):
    pass

#FUNCTIONS have two types built-in and user-defined
#built-in are already defined in python like print(), len(), type(), range()
#user-defined are defined by the coder some examples are the above ones

#print() has two optional arguments because they have default values like sep and end they have sep = " " and end = "\n" by default0

#default parameters. add a = after the parameter then value to give a default value like
def prn(e = "\n"):
    pass

#practice1
#WAF to print the length of a list
def prn_len(list = [0]):
    return len(list)

#practice2
#WAF to print the elements of a list in a single line.
def prn_list(list = [0]):
    for i in list:
        print(i, end = "")

#practice3
#WAF to find the factorial of n
def prn_fact(n = 1):
    fact = 1
    for i in range(1, n+1, 1):
        fact *= i
    else:
        return fact

#practice4
#WAF to convert USD to INR
def curr_conv(v):
    return 95.46 * v

#RECURSION: when a function calls itself
#recursion and loops can copy each other
#it is mostly harder then loops

def show(n):
    if(n == 0):#base case is mandatory
        return#sends you back
    print(n)
    show(n-1)
    print("END")
#5 then 4 = 5-1 then 3 = 5-2 then 2 = 5-3 then 1 = 5-4 then 0 will stop
#call stack
#n = 3. 3 comes prints 3 calls 2 2 comes prints 2 calls 1 1 comes prints 1 calls 0 0 comes get FALSE and returns back now 3 checks if something is left yes END prints END same for all so it is 3 2 1 END END END
show(3)

#to make it infinite remove base case

#practice1
#WARF to calculate sum of first n natural numbers
def sum(n):    
    if(n == 0):
        return 0
    return sum(n - 1) + n

#practice2
#WARF to print all elements in a list
def prin_list(list = [0]):
    idx = 0
    if(idx == len(list) - 1):
        return
    print(list[idx])
    idx += 1
    prin_list(list)