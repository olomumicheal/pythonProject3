#functions in python
def myFunction():
    print("Welcome To Bizmarrow")

myFunction()

#functions with argument
def Myfunction(fname):
    print("my first name is " + fname)

Myfunction("Samuel")

#function with parameters
def mYfunction(fname, lname):
    print(fname + " " + lname)

mYfunction("John", "Doe")

#functions with arbitrary argument
def my_function(*kids):
    print("The youngest kid is " + kids[3])

my_function("james", "austin", "sam", "john")

#arbitrary key argument
def my_Functions(child1, child2, child3):
    print("The smartest child is " + child2)

my_Functions(child1="solomon", child2="sammy", child3="favor")


#using return statement in function
def myFUNCion(x):
    return x * 5

print(myFUNCion(16))
print(myFUNCion(20))
print(myFUNCion(10))

#lOOP IN python
#We have two types of loop in python
#1. while loop
#2. For loop

#while loop
i = 0

while i < 6:
    print(i)
    i += 1

#while loop with break statement
i = 0

while i < 10:
    print(i)
    if i == 7:
        break
    i += 1

#while loop with continue statement
i = 0

while i < 10:
    i += 1
    if i == 7:
        continue
    print(i)

#For Loop
#For loop loop through a sequence of data
fruits = ["Banana", "Mango", "Apple", "Pineaple"]
for x in fruits:
    print(x)

#using break in For loop
fruits = ["Banana", "Mango", "Apple", "Pineaple"]
for x in fruits:
    if x == "Apple":
        break
    print(x)



#using continue in For loop
fruits = ["Banana", "Mango", "Apple", "Pineaple"]
for x in fruits:
    if x == "Apple":
        continue
    print(x)

#Nested loop
Ministries = ["Art & culture", "Information", "Power", "fmst"]
Schools  = ["Futmina", "Futo", "Unizik"]

for x in Ministries:
    for y in Schools:
        print(x, y)
