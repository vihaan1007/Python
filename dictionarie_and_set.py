#DICTIONARIES: they are used to store data values in key:value pairs They are unordered, muable & dont allow dulicate keys 
#mutable means they can be changed
#unordered means no indices
#no duplicate keys means no keys can show again
 
emp_dict = {}
print(type(emp_dict))#dict
print(emp_dict)
stu = {
    "name": "vihaan",
    "class": 5.3,
    "roll.no": 524,
    "marks": 97 
}
print(type(stu))    
print(stu)

#they can store any data types like lists and tuples
product = {
    "product": "chips",
    "price": 1.99,
    "no.": 55,
    "available": True,
    "hazardous": None
}#list tuples and others are also ok
print(product)
print(product["no."])#55
#changing, making new, or owerwriting
product["available"] = False
print(product)

#nesting is possible in dictionaries also. they are also in lists and tuples
score = {
    "name": "Vihaan",
    "score": {
        "math": 40,
        "EVS": {
            "SST": 40,
            "Science": {
                "phy": 13,
                "chem": 13,
                "bio": 13
            }
        },
        "computer": 39.5
    },
    "rank": 1,
    "percentage": 97.1
}
#print(score) dont want mess
print(score["score"]["EVS"]["Science"]["chem"])

#DICTIONARY METHODS

print(product.keys())#returns all keys
#for len
print(len(list(product.keys())))#same as the length of the dict(if not nested)

print(product.values())#returns all values. same as keys for len

print(product.items())#returns all (key, val) pairs as a tuple. same as keys for len

print(product.get("price"))#returns value of the specified keys.
#USE. if product[key] works
#if the key dosent exist then:
#print(product["AAA"])# error
print(product.get("AAA"))# no error it gives None
# and error stops the whole code means a whole application will collapse on this

city = {"city": "Jabalpur"}
product.update(city)# adds a new key:value pairor owerwrite it in the dict also can be passed directly
print(product)

#SET: Set is a collection of the unordered items.Each element is unique & immutable.Each element is immutable but set itself is mutable

emp_set = set()
nums = {1, 2, 3, 4, 3, 2, 1}#no elements can be reapeated so,
#nums resolves to {1, 2, 3, 4}
print(type(nums))
#bool, int, float, str, tuple can be stored in a set while list and dict cant be stored
#they are at a new level of unordered 
print(nums)
print(nums)
print(nums)
print(nums)
#all of them are different order

#SET METHODS

nums.add((1, 2, 3, 4))#adds a element at anywhere
print(nums)

nums.remove((1, 2, 3, 4))#removes the element
print(nums)

num = {1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 8, 9, 7, 9}
print(num)
num.clear()#clears the set
print(num)

nums.pop()#removes a random value

set1 = {1, 2, 3}
set2 = {3, 2, 4, 5}
print(set1.union(set2))#combines value of both sets resolved and no value is reapeated and it retuns the answer

print(set2.intersection(set1))#returns the common value of two resolved sets

#practice1
#Store following words in a python dictionarie
#table: "a piece of furniture", "list of facts and figures" and cat: "a small animal"

pra1 = {
    "table": ["a piece of furniture", "list of facts and figures"],
    "cat": "a small animal"
}

#practice2
#You are given a list of subjects for students. Assume one classroom is required for 1 subject. How many classrooms are needed by all students.
#"python", "java", "C++", "python", "javascript", "java", "python", "java", "C++", "C"
#ANS- 5

pra2 = {"python", "python", "python", "java", "java", "java", "C++", "C++", "javascript", "C"}
print(len(list(pra2)))#5

#practice3
#WAP to enter marks of 3 subjects from the user and store them in a dictionary. Start with an empty dictionary & add one by one. Use subject name as key and marks as value

pra3a = int(input("Enter the marks of phy: "))
pra3b = int(input("Enter the marks of chem: "))
pra3c = int(input("Enter the marks of bio: "))
pra3 = {}
pra3.update({"phy":pra3a})
pra3.update({"chem":pra3b})
pra3.update({"bio":pra3c})

#practice4
#Find a way to store 9.0 & 9 as seperate values in a set
pra4 = {"9", 9.0}#do it in cheats:)