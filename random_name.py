import random
names = ["Apple", "Banana", "Cat", "Dog", "Elephant", "Fish", "Grapes", "Horse", "Ice cream", "Joule", "Kilo", "Length", "Monkey", "Nest", "Orange", "Plum", "Queen", "Rabbit", "South", "Temperature"]
i = 0
while i < 20:
    length = len(names)-1
    n = random.randint(0, length)
    print(names[n])
    names.pop(n)
    length-=1
    i+=1