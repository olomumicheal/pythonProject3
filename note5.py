#creating a dictionary
myDetails = {
    "firstName": "Samuel",
    "lastName": "Maxwell",
    "age": 25,
    "isMarried": False,
    "favGames": ["Football", "Volleyball", "Basketball"],
    "favFood": {"Spag", "Rice", "Indomie"},
    "Hobie": ("Programming", "Coding", "Gaming")
}

print(myDetails)

#Accessing an item in a dictionary
x = myDetails["lastName"]
print(x)

#to get the keys
x = myDetails.keys()
print(x)

#to get the values
x = myDetails.values()
print(x)

#to get our items
x = myDetails.items()
print(x)


#to check if a key exist
if "isMarried" in myDetails:
    print("Yes the key is present")
else:
    print("The key is not present")

#How to change an item in a Dictionary
myDetails["firstName"] = "Michael"
print(myDetails)

#How to change an item in a Dictionary using an update()
myDetails.update({"Africa": "Nigeria"})
print(myDetails)
