#python conditional statement
#if conditional statement
a = 55
b = 40

if a > b:
    print("a is greater than b")

#Elif conditional statement
a = 55
b = 40

if a < b:
    print("a is less than b")
elif a > b:
    print("a is greater than b")

#Else conditional statement
a = 55
b = 40

if a < b:
    print("a is less than b")
elif a == b:
    print("a is equal to b")
else:
    print("a is greater than b")


#short hand if conditional statement
x = 12
y = 14
print("x is less than y") if x < y else print("x is greater than y")

#using shorthand method to print out the above example. short hand method is only limited to if and else
print("a is less than b") if a < b else print("a is greater than b")

#the and keyword operator
k = 22
l = 22.5
m = 30

if k < l and m > k:
    print("both conditions are true")

#the or keyword operator
k = 22
l = 22.5
m = 30

if k > l or m > k:
    print("one of them are correct")

#not operator, works as opposite of any true statement
k = 22
l = 22.5
m = 30

if not(k < l and m > k):
    print("both conditions are true")
else:
    print("both conditions are false")


k = 22
l = 22.5
m = 30

if not(k > l or m < k):
    print("none of them are correct")