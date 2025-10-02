# The print function outputs text to the console
print("Hello World")

# The plus sign (+) concatenates (joins) strings together
print("Hello" + " " + "World")

# The input function gets user input from the console
input("Enter your name: ")

# The len function returns the length of a string
len("Hello")

# The equal sign (=) assigns a value to a variable
name = "Jack"

# A variable can be used to store user input
name = input("Enter your name: ")
print("Hello " + name)

# Get the user's name and print the length of the name
name = input("Enter your name: ")
print("Hello " + name + ". The lenght of your name is: ", len(name)) 
# Or try a direct approach like this:
print(len(input("What is your name?: ")))

# Variable interchange and manipulation
a = input("enter a value: ")
b = input("enter b value: ")
a = int(a)
b = float(b)
a = a + b
b = a + b
print("a = ", a)
print("b = ", b)
print("The sum of a and b = ",a + b)
# You can also do this in a more concise way
a = int(input("enter a value: "))
b = float(input("enter b value: "))
a = a + b
b = a + b
print("a = ", a)
print("b = ", b)
print("The sum of a and b = ",a + b)
# Or even like this
a = int(input("enter a value: "))
b = float(input("enter b value: "))
print("a = ", a + b)
print("b = ", a + b + b)
print("The sum of a and b = ",a + b + a + b)
# Note: The above code snippets demonstrate basic Python concepts such as
# printing to the console, string concatenation, user input, variable assignment,
# type conversion, and arithmetic operations.


# Switching the value of Varialbles
a = int(input("enter a value: "))
b = int(input("enter b value: "))
c = b
b = a
a = c
print("a = ", a)
print("b = ", b)

# You can also do this without a temporary variable
a = int(input("enter a value: "))
b = int(input("enter b value: "))
a, b = b, a
print("a = ", a)
print("b = ", b)
# Or like this
a = int(input("enter a value: "))
b = int(input("enter b value: "))
a = a + b
b = a - b
a = a - b
print("a = ", a)
print("b = ", b)

# Create a greeting for your program.
print("Hello", "Welcome to the band name generator.")
# Ask the user for the city that they grew up in.
city = str(input("Which city did you grow up in?\n"))
# Ask the user for the name of a pet.
pet = str(input("What is the name of a pet?\n"))
# Combine the name of their city and pet and show them their band name.
print("Your band name could be " + city + " " + pet)

# Simple Calculator in Python
print("Welcome to super simple calculator")
# Basic Input and Output
a = float(input("enter first number: "))
b = float(input("enter second nummber: "))
print("The value of a // b is : ", a // b)