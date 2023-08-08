#loop in python
a = 0
while a < 6:
    print(a)
    a +=1

#using break statement in a loop
a = 0
while a < 10:
    print(a)
    if a == 6:
        break
    a += 1


#using break statement in a loop
a = 0
while a < 10:
    a += 1
    if a == 6:
        continue
    print(a)

#use else statement in a while loop
a = 10
while a < 100:
    print(a)
    a +=10
else:
    print("a is no longer less than 6")

#For loop
fruits = ["Mango", "Banana", "Apple"]

for x in fruits:
    print(x)

#using a break statement in a For loop
fruits = ["Mango", "Banana", "Apple"]

for x in fruits:
    print(x)
    if x == "Banana":
        break

#using a continue statement in a For loop
fruits = ["Mango", "Banana", "Apple", "water melon"]

for x in fruits:
    if x == "Banana":
        continue
    print(x)

ministries = ["FMST", "Environment", "Architecture"]

for x in fruits:
    for y in ministries:
        print(x, y)






