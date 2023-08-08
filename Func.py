#Functions in python
def myFunction():
    print("Welcome To Europe")

myFunction()


#u can use any terms for function
def micheal():
    print("how are u")
micheal()

#Functions with argument
def my_function(fname):
    print("my first name is " + fname)

my_function("Solomon")
my_function("James")
my_function("Kelvin")

#functions with parameters of Argument
def Myfunction(fname, lname):
    print(fname + " " + lname)

Myfunction("John", "Doe")

#python with Arbitrary argument
def mYfunction(*kids):
    print("The favourite kid is " + kids[1])

mYfunction("Tobias", "James", "Cambel")

#keyword argument
def MYfunction(child1, child2, child3):
    print("The youngest child is " + child3)

MYfunction(child1= "Solompn", child2="James", child3="Kelvin")

#Arbitrary keyword argument
def MYFunction(**Names):
    print("the last name is " + Names["lastName"])

MYFunction(firstName = "John", lastName="Doe")

#Default parameter value
def myFUNCtion(country = "Canada"):
    print("I have been to " + country)

myFUNCtion("Norway")
myFUNCtion("Italia")
myFUNCtion("Austria")
myFUNCtion()

#return statement
def myfunctION(x):
    return x * 5

print(myfunctION(30))
print(myfunctION(10))
print(myfunctION(3))

"""
        HOME WORK
1. Passing a List as an Argument
2. The pass Statement
3. Recursion
"""