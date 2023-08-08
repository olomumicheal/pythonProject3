#List Data type
myList = ["Fruits", "Mango", "Academic", 25, 4.07, True]
print(myList)
print(type(myList))

#Accessing a list item
print(myList[0])
print(myList[-1])
print(myList[2:4])

#check if an item in the list
if "Fruits" in myList:
    print("yes fruits is in the list")
else:
    print("fruits but Fruits is the one in the list")

#To change a list item
myList[2] = "Enviroment"
print(myList)

#changing data using range method
myList[3:5] = ["Socioloigy", "Fraction"]
print(myList)


#using insert method to add an item to the list
myList.insert(1, "petroleum")
print(myList)

#using append() to add an item to a list
myList.append("University")
print(myList)

#To add two list together using extend()
theList = ["Maria", "Ronaldo", "Atlanta", False]
myList.extend(theList)
print(myList)

#To remove an item from a list using remove()
myList.remove("University")
print(myList)

#remove an item from the list using pop()
myList.pop(2)
print(myList)

#to remove an item from the list using del keyword
del myList[3]
print(myList)

#looping through a list using for method
for a in myList:
    print(a)

#looping through the range()
for x in range(len(myList)):
    print(x)

#list comprehension
fruits = ["Mango", "Orange", "Kero", "Mukus"]
newlist = []
for x in fruits:
    if "a" in x:
        newlist.append(x)

print(newlist)


#Joining two list together
list1 = ["fruits", "schools", "arithmetic"]
list2 = ["set", "maths", "chemistry"]
list3 = list1 + list2
print(list3)

#Using the append() to join two list
for a in list2:
    list1.append(a)

print(list1)

#introduction to Dictionary
myDetails = {
    "fullName": "Olomu Micheal",
    "age": 26,
    "isMarried": False,
    "myFavGame": ["Football", "Basketball", "Volleyball"],
    "myFavSub": {"Maths", "Engineering", "Astronaut"}
}

print(myDetails)
