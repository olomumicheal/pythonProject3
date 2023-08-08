#creating a list
myList = ["Fruits", "Games", "Athlete", "Ministry", True, 60, 0.56]
print(myList)

#How to access list item
print(myList[3])
print(myList[-1])

#How to acces items using range method
print(myList[2:6])

#How to change a list item
myList[2] = "ESP"
print(myList)

#using range method to change an item in a list
myList[2:4] = ["Orange", "Mango"]
print(myList)


#using insert() to position an item
myList.insert(5, "Apple")
print(myList)

#How to add two items together using append()
myList.append("welcome")
print(myList)

##How to add two items together using extend()
newlist = ["Predator", "Science", "Supernatural"]
myList.extend(newlist)
print(myList)

#How to remove an item using remove()
myList.remove("Orange")
print(myList)

#How to remove an item using pop()
myList.pop(3)
print(myList)


#How to remove an item using del method
del myList[5]
print(myList)

#Looping through a list data
for a in myList:
    print(a)

#to print item by index
for a in range(len(myList)):
    print(myList[a])

#List comprehension
club = ["man u", "chelsea", "barca", "real madrid", "lei pzid"]
newestlist = []

for a in club:
    if "a" in a:
        newestlist.append(a)
print(newestlist)


"""
                    ASSESSMENT
1. create a list of fruits, inside the list of fruits introduce a boolean of False and a numeric value of float
a. from above;
i. access the float item
ii. remove the boolean data
iii. add an int data
iv. loop through the data using For loop
"""

#sorting list data
fruit = ["orange", "mango", "kiwi", "pineapple", "banana"]
fruit.sort()
print(fruit)


numeric = [100, 50, 65, 82, 23]
numeric.sort()
print(numeric)

#sorting in descending order
fruit = ["orange", "mango", "kiwi", "pineapple", "banana"]
fruit.sort(reverse= True)
print(fruit)

numeric = [100, 50, 65, 82, 23]
numeric.sort(reverse=True)
print(numeric)


#joining list items
list3 = fruit + numeric
print(list3)

#using the append method

for x in numeric:
    fruit.append(x)
print(fruit)