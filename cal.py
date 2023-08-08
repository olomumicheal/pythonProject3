#def add()
def add(x, y):
    return x + y

#def subtract()
def subtract(x, y):
    return x - y

#def multiply()
def multiply(x, y):
    return x * y

#def divide()
def divide(x, y):
    return x / y

print("Select Operation: ")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")


#creating input operation
choice = input("Select Operation 1, 2, 3, 4: ")

#defining x and y parameters as num1 and num2
num1 = float(input("Enter 1st number: "))
num2 = float(input("Enter 2nd number: "))

#implementing our functions
if choice == "1":
    print(num1, "+", num2, "=", add(num1, num2))
elif choice == "2":
    print(num1, "-", num2, "=", subtract(num1, num2))
elif choice == "3":
    print(num1, "*", num2, "=", multiply(num1, num2))
elif choice == "4":
    print(num1, "/", num2, "=", divide(num1, num2))
else:
    print("not an option")