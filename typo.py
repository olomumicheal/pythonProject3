# #Simple dictionary
# myDef = {
#     "firstName": "John",
#     "lastName": "Doe",
#     "year": 1996,
#     "favGames": ["Football", "Volleyball", "Basketball"]
# }
#
# print(myDef)
#
#
# #How To chnage a Dictionary
# myDef["year"] = 2000
# print(myDef)
#
# #usimg update()
# myDef.update({"isMarried": False})
# print(myDef)
#
# myDef.update({"isMarried": True})
# print(myDef)
#
# #To remove an item from a dictionary using pop()
# myDef.pop("isMarried")
# print(myDef)
#
# #To remove an item from a dictionary using popitem()
# myDef.popitem()
# print(myDef)
#
# #To remove an item from a dictionary using del
# del myDef["lastName"]
# print(myDef)
#
# #To print all key names in the dictionary using loop method,
# for x in myDef:
#     print(x)
#
# #To print all value names in the dictionary using loop method
# for x in myDef:
#     print(myDef[x])
#
# #Nested Dictionaries
# myFamily = {
#     "child1": {
#         "fullName": "Tobias",
#         "age": 12,
#     },
#     "child2": {
#         "fullName": "James",
#         "age": 10,
#     },
#     "child3": {
#         "fullName": "Samuel",
#         "age": 6
#     }
# }
#
# print(myFamily)
# child1 = {
#         "fullName": "Tobias",
#         "age": 12,
#     },
# child2 = {
#         "fullName": "James",
#         "age": 10,
#     },
# child3 = {
#         "fullName": "Samuel",
#         "age": 6
#     }
#
# myPeople = {
#     "child1": child1,
#     "child2": child2,
#     "child3": child3
# }
#
# print(myPeople)
#
# print(myFamily["child2"]["fullName"])

#Conditional Statement
#IF conditional statement
a = 55
b = 60

if a < b:
    print("a is less than b")

#ELIF conditional statement
x = 55
y = 60

if x > y:
    print("x is greater than y")
elif x < y:
    print("x is less than y")

#ELSE conditional statement
m = 55
n = 55

if m < n:
    print("m is less than n")
elif m > n:
    print("m is greater than n")
else:
    print("m is equal to n")

#short hand if else
l = 2
k = 2.5

print("l is greater than k") if l > k else print("l is less than k")

#AND logical operator
j = 33
i = 44
m = 33

if j < i and m == j:
    print("both conditions are true")
else:
    print("both conditions are not true")


#OR logical operator
j = 33
i = 44
m = 33

if j > i or m == j:
    print("one of the conditions is true")
else:
    print("none of the conditions is true")

#NOT logical operator
#AND NOT logical operator
j = 33
i = 44
m = 33

if not(j < i and m == j):
    print("both conditions are true")
else:
    print("both conditions are not true")

#OR NOT logical operator
j = 33
i = 44
m = 33

if not(j > i or m == j):
    print("one of the conditions is true")
else:
    print("none of the conditions is true")



