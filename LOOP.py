#python has two primitive loop command
# 1. while loop
# 2. For loop

#loop example
a = 0
while a <= 6:
    print(a)
    a += 1

#introducing a break in our loop
i = 1
while i < 10:
    print(i)
    if i == 5:
        break
    i += 1

#continue statement in loop
i = 1
while i < 10:
    i += 1
    if i == 5:
        continue
    print(i)

#introducing else in while loop
a = 0
while a <= 6:
    print(a)
    a += 1
else:
    print("a is no longer less than 6")


#For loop
# fruits = ["Orange", "Apple", "Banana", "pineaple"]
# for x in fruits:
#     print(x)

#implementing break method
fruits = ["Orange", "Apple", "Banana", "pineaple"]
for x in fruits:
    if x == "Banana":
        break
    print(x)

#implementing continue method
fruits = ["Orange", "Apple", "Banana", "pineaple"]
for x in fruits:
    if x == "Banana":
        continue
    print(x)

#using range()
for x in range(6):
    print(x)

for x in range(2, 4):
    print(x)

#using range() and else
for x in range(6):
    print(x)
else:
    print("finally finished")


#using range() and else with break
for x in range(6):
    if x == 3: break
    print(x)
else:
    print("finally finished")


#Nested loop
Details = ["Ministries", "Academic", "Infrastructure"]
myDetails = ["Numpy", "Scipy", "Matplotlib"]

for x in Details:
    for y in myDetails:
        print(x, y)

        """
        Assessment
        1. if m < 100, break it at 60 using while loop
        2. loop through a sequence of defined datas of cities
        3. Nest two sequence detail using for loop
        """



