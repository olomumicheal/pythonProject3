# print("Hello World")

"""
Data Types in Python
1. String data type
2. Int data type
3. float data type
4. Boolean data type
5. list data type
6. tuple data type
7. set data type
8. Dictionary data type
"""

#1. String data type
myFirstName = "Micheal"
myLastName = "Ola"

print(myFirstName)
print(myLastName)

#String Concatenation
myFullName = myFirstName + " " + myLastName
print(myFullName)

print("I am " + myFullName + " and am from Edo/Ondo state")

#2. Int data type
x = 200
y = 400
z = y + x
print(z)

#3. Float data type
x = 0.34
y = 00.5677
z = x - y
print(z)
print(type(z))

#4. Boolean data type
isMarried = True
isNotMarried = False
print(isMarried)
print(type(isMarried))
print(isNotMarried)

#5. List Data type
myList = ["Micheal", 25, False, 0.45]
print(myList)

#6. Tuple data type
myTuple = ("Micheal", 25, False, 0.45)
print(myTuple)

#7. Set data type
mySet = {"Micheal", 25, False, 0.45}

#8. Dictionary Data type
myDictionary = {
    "FullName": "Ola Micheal",
    "age": 25,
    "isMarried": False,
    "MyFavGames": ["Football", "Volleyball", "Basketball"]
}
print(myDictionary)

"""
            ASSESSMENT
1. declare a variable of welcome and concatenate it, as "welcome to Bizmarrow Techology"
2. create a dictionary of your state and few details
"""

"""
            Types of Arithmetic Operators
1. Arithmetic operator
2. Assigment Operators
3. Comparison Operators
4. Logical Operators
"""

# Python Operators
x = 50
if(x > 50):
    print("X is less than 50")
elif(x == 50):
    print("x is equal to 50")
else:
    print("x is greater than 50")