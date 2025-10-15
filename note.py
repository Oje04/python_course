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

# Type Conversion/Casting in Python
# Since the input function always returns a string, you can directly use len() on it
# but if you want to store the length in a variable, you need to convert it to string for concatenation
# else it will throW a TypeError
num_char = input("What is your name?:")
print("The number of characters in your name is: " + str(len(num_char)))
           # OR #
num_char = len(input("What is your name: "))
new_num_char = str(num_char)
print("The number of characters in your name is: " + new_num_char)

# For confirmation on what kind of data type you are working with, you can use the type() function
num_char = 964.52
print(type(num_char))

# You can also use type() to check the data type of user input
two_digit_number = input("Type a two digit number: ")
print(type(two_digit_number))
a = int((two_digit_number[0]))
b = int((two_digit_number[1]))
print("The sum of a and b is: ", a + b)

# Calculating BMI (Body Mass Index)
height = float(input("enter your height in meter: "))
weight = int(input("enter your weight in KG: "))
BMI = weight / height ** 2
print(type(BMI))
print(int(BMI))

# Calculating the remaining days, weeks and months left if you live until 90 years old
life_span = 90
days = 365 * life_span
weeks = days / 7
month = life_span * 12
age = int(input("Enter your current age: "))
print (f"you have {days - (age * 365)} days, {weeks - (age * 52)} weeks, and {month - (age * 12)} months, left.")
     #OR#
curent_age = int(input("Enter your current age: "))
life_span = 90
years_remaining = life_span - current_age
months_remaining = years_remaining * 12
weeks_remianing = years_remaining * 52
days_remaining = years_remaining * 365
message = f"you have {days_remaining} days, {weeks_remianing} weeks, and {months_remaining} months, left."
print(message)

# Final Project: Tip Calculator
print("Welcome to the tip calculator.")
bill = float(input("What was the total bill?: "))
percent = float(input("What percentage tip would you like to give? 10, 12, or 15?: "))
num_of_people = int(input("How many people to split the bill?: "))
percent = float(percent / 100)
tip = float(bill * percent)
total_bill = float(bill + tip)
final_split = round(total_bill / num_of_people, 2)
message = f"Each perrson should pay: ${final_split}"
print(message)

# A program that checks if a number is odd or even
print("this program checks for odd or even number")
num = int(input("Enter a number: "))
if num % 2 == 0:
    print("this is an even number")
else:
    print("this is an odd number") 

# A rollercoaster ride ticketing program as an example of using if-else, nested if-else and elif statements.
print("Welcome to the rollercoaster party!")
height = int(input("Enter your height in cm: "))
if height >= 120:
    print("You can ride, head over to the ticket boot")
    age = int(input("How old are you?: "))
    if age < 10:
        print("Your ticket cost $4.99")
    elif age <= 15:
        print("Your ticket cost $9.99")
    elif age <= 20:
        print("Your ticket cost $14.99")
    else:
        print("Your ticket cost $19.99")
else:
    print("Sorry you can't ride the rollercoaster\nBye!")

# BMI 2.0 Calculator
print("Welcome to the BMI calculator!")
height = float(input("Please enter your height in cm: "))
weight = int(input("Please enter your weight in kg: "))
bmi = round(weight / height ** 2, 2)
if bmi < 18.5:
    print(f"{bmi} You are underweight")
elif bmi <= 25:
    print(f"{bmi} You are normal weight")
elif bmi <= 30:
    print(f"{bmi} You are overweight")
elif bmi <= 35:
    print(f"{bmi} You are obese")
else:
    print(f"{bmi} You are clinically obese")

# Nested if statement to check if a year is a leap year
print("Welcome to the leap year calculator")
year = int(input("Enter the year you want to check: "))
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(f"{year} is a leap year")
        else:
            print(f"{year} is not a leap year")
    else:
        print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")

# Rollercoaster 2.0 with photo option
print("Welcome to the rollercoaster party!")
height = int(input("Enter your height in cm: "))
bill = 0
if height >= 120:
    print("You can ride, head over to the ticket boot")
    age = int(input("How old are you?: "))
    if age < 10:
        bill = 4.99
        print("Toddler ticket cost $4.99")
    elif age <= 15:
        bill = 9.99
        print("Adolescent ticket cost $9.99")
    elif age <= 20:
        bill = 14.99
        print("Youth ticket cost $14.99")
    else:
        bill = 19.99
        print("Adult ticket cost $19.99")
    photo = input("Do you want a photo taken? Y or N: ")
    if photo == "Y":
        bill += 2.99
    print(f"Your sub-total is ${bill}, enjoy your ride!")
else:
    print("Sorry you can't ride the rollercoaster\nBye!")

# A pizza ordering program
print("Welcome to python pizza deliveries!")
size = input("What size pizza do you want? S, M, L: ")
pepperoni = input("Do you want pepperoni? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")
price = 0
if size == "S":
    price += 14.99
elif size == "M":
    price += 19.99
else:
    price += 24.99
if size == "S":
    if pepperoni == "Y":
        price += 1.99
    else:
        price = price
elif size == "M":
    if pepperoni == "Y":
        price += 2.99
    else:
        price = price
elif size == "L":
    if pepperoni == "Y":
        price += 2.99
    else:
        price = price
if extra_cheese == "Y":
    price += 0.99
else:
    price = price
print(f"Your sub-total is ${price}.")

 #OR#

 print("Welcome to python pizza deliveries!")
size = input("What size pizza do you want? S, M, L: ")
pepperoni = input("Do you want pepperoni? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")
price = 0
if size == "S":
    price += 14.99
elif size == "M":
    price += 19.99
else:
    price += 24.99
if pepperoni == "Y":
    if size == "S":
        price += 1.99
    else:
        price += 2.99
if extra_cheese == "Y":
    price += 0.99
print(f"Your sub-total is ${round(price, 2)}.")

# Rollercoaster 3.0 with logical operator to consider middle age group discount
print("Welcome to the rollercoaster party!")
height = int(input("Enter your height in cm: "))
bill = 0
if height >= 120:
    print("You can ride, head over to the ticket boot")
    age = int(input("How old are you?: "))
    if age < 10:
        bill = 4.99
        print("Toddler ticket cost $4.99")
    elif age <= 15:
        bill = 9.99
        print("Adolescent ticket cost $9.99")
    elif age <= 20:
        bill = 14.99
        print("Youth ticket cost $14.99")
    elif age >= 45 and age <= 55:
        print("Middle age ticket cost $0.00")
    else:
        bill = 19.99
        print("Adult ticket cost $19.99")
    photo = input("Do you want a photo taken? Y or N: ")
    if photo == "Y":
        bill += 2.99
    print(f"Your sub-total is ${round(bill, 2)}, enjoy your ride!")
else:
    print("Sorry you can't ride the rollercoaster\nBye!")

# Love calculator using the lower() & count() function to make the input case insensitive and count the number of times a letter appears in a string
print("Welcome to the Love Calculator!")
name1 = input("Enter your name \n")
name2 = input("Enter your partner'S name \n")

name = name1 + name2

name_check = name.lower()

t = name_check.count("t")
r = name_check.count("r")
u = name_check.count("u")
e = name_check.count("e")

true = t + r + u + e

l = name_check.count("l")
o = name_check.count("o")
v = name_check.count("v")
e = name_check.count("e")

love = l + o + v + e

love_score = int(str(true) + str(love))

if love_score < 10 | love_score > 90:
    print(f"Your score is {love_score} you go together like coke and mentos")
elif love_score >= 40 & love_score <= 50:
    print(f"Your score is {love_score} you are alright together.")
else:
    print(f"Your score is {love_score}.")

# Treasure Island Game
print('''  _                                     _     _                 _ 
| |                                   (_)   | |               | |
| |_ _ __ ___  __ _ ___ _   _ _ __ ___ _ ___| | __ _ _ __   __| |
| __| '__/ _ \/ _` / __| | | | '__/ _ \ / __| |/ _` | '_ \ / _` |
| |_| | |  __/ (_| \__ \ |_| | | |  __/ \__ \ | (_| | | | | (_| |
 \__|_|  \___|\__,_|___/\__,_|_|  \___|_|___/_|\__,_|_| |_|\__,_|
                                                                 
                                                                 
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/
*******************************************************************************''')
print("Welcome to the Treasure Island!\nYour mission is to find the Treasure.\nGoodluck!!!")
choice1 = input('You\'ve arrived at a crossroad, type "Right" if you want to go right or type "Left" if you want to go left.\n').lower()
if choice1 == "left":
    choice2 = input('You made the right choice however, the Treasure is in the middle of the lake. type "Swim" if you want to\nswim to the island or "Wait" if you want a boat to get you to the island.\n').lower()
    if choice2 == "wait":
        choice3 = input('Yay! You\'ve made it to the island but there is a tower and an old hut.\nWhich do you want to check first?\ntype "Tower" to go to the tower or type "Hut" to go to the hut.\n').lower()
        if choice3 == "tower":
            choice4 = input('Well done! You\'ve reached the Tower but there are three doors, choose which door to enter by typing either "Yellow", "Blue" or "Red"\n').lower()
            if choice4 == "yellow":
                print('''         _________
        /\____;;___\\        
       | /         /
       `. ())oo() .
        |\(%()*^^()^\
        
       %| |-%-------|
      % \ | %  ))   |
      %  \|%________|\nCongratulations! You found the treasure. You Win!!!''')
            elif choice4 == "blue":
                print('''        	 ______________
           ,===:'.,            `-._
                `:.`---.__         `-._
                   `:.     `--.         `.
                     \.        `.         `.
             (,,(,    \.         `.   ____,-`.,
          (,'     `/   \.   ,--.___`.'
      ,  ,'  ,--.  `,   \.;'         `
       `{D, {    \  :    \;
         V,,'    /  /    //
         j;;    /  ,' ,-//.    ,---.      ,
         \;'   /  ,' /  _  \  /  _  \   ,'/
               \   `'  / \  `'  / \  `.' /
                `.___,'   `.__,'   `.__,'  \nOops! you have entered a dragon\'s lair. Game Over.''')
            elif choice4 == "red":
                print('''               (  .      )
           )           (              )
                 .  '   .   '  .  '  .
        (    , )       (.   )  (   ',    )
         .' ) ( . )    ,  ( ,     )   ( .
      ). , ( .   (  ) ( , ')  .' (  ,    )
     (_,) . ), ) _) _,')  (, ) '. )  ,. (' )
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\nOops! You entered a room full of fire. Game Over.''')
            else:
                print("You have picked a wrong door. Game Over.")
        else:
            print("Dang! There was a snake in the hut and you got bitten by the snake. Game Over.")
    else:
        print('Oops! You\'ve been attacked by a shark. Game Over.')
else:
    print("Oops! You fell into a hole. Game Over.")

