#Python Conditional Statement
#IF conditional statement
x = 20
y = 40

if x < y:
    print("x is less than y")

#ELIF and Else conditional statement
a = 20
b = 30

if a > b:
    print("a is greater than b")
elif a == b:
    print("a is equal to b")
else:
    print("none of the condition above is true")

#short hand conditional statement
m = 7
n = 5

print("m is equal to n") if m == n else print("m is greater than n")


#logical and operator
k = 12
l = 12.5
s = 0.5

if k < l and l > s:
    print("both conditions are true")

#logical OR operator
k = 12
l = 12.5
s = 0.5

if k > l or l > s:
    print("one of the conditions is true")

#not logical operator with and
k = 12
l = 12.5
s = 0.5

if not(k < l and l > s):
    print("both conditions are true")
else:
    print("both conditions are not true")

#not logical operator with or
k = 12
l = 12.5
s = 0.5

if k > l or l > s:
    print("one of the conditions is true")
else:
    print("none of the conditions are true")


#Functions in Python
def myFunction():
    print("Welcome To Atlanta")

myFunction()


def micheal():
    print("Micheal hOW aRE yOU")
micheal()

#functions with argument
def myfunction(fname):
    print("my first name is " + fname)

myfunction("Samuel")
myfunction("James")
myfunction("Zedris")

#function with multiple argument and parameter
def Myfunction(fname, lname):
    print(fname + " " +lname)

Myfunction("Samuel", "John")

#functions with arbitrary argument
def my_function(*kids):
    print("the last child is the youngest and his name is " + kids[2])

my_function("james", "samuel", "kelvin")

#functions with keyword argument
def mYfunction(child1, child2, child3):
    print("the youngest child is " + child2)

mYfunction(child1="solo", child2="blessing", child3="favor")

#return method in function
def myFuNction(x):
    return x * 5

print(myFuNction(12))
print(myFuNction(10))
print(myFuNction(4))


"""
1. work on default parameter value in function
2. passing a list as an argument
"""



