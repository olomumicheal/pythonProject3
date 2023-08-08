# try block
x = "atlanta"

try:
    print("x is defined")
except:
    print("x is not defined")

#Many Exceptions
try:
    print(y)
except NameError:
    print("y is not defined")
except:
    print("something went wrong")


#Else keyword
try:
    print("Hello World")
except:
    print("something went wrong")
else:
    print("Nothing went wrong")

#finally block
try:
    print(z)
except:
    print("something went wrong")
finally:
    print("the try except, is finished")


#Try to open and write to a file that is not writable:
try:
    f = open("demofile.txt")
    try:
        f.write("lorem Ipsum")
    except:
        print("something went wrong when writing to the file")
    finally:
        f.close()
except:
    print("something went wrong when opening the file")


#Raise Exception keyword
# x = -1
#
# if x < 1:
#     raise Exception("No number below zero")

#Typeof
# a = "welcome"

#
# if not type(a) is int:
#     raise  TypeError("a is not an integer")


#userinput() in python
userName = input("Name: ")
print("my name is " + userName)


#python string formatting
price = 50
x = "The price is {} dollar"
print(x.format(price))

#python string formatting with multiple values
quantity = 4
item_no = 300
price = 35

statement = "he bought {} quantities of {} items, tagged at {:.2f} dollar"
print(statement.format(quantity, item_no, price))