"""
if-else statement 

An if-else statement in Python is a conditional control structure that lets you decide which block of code to run depending on whether a condition is True or False

The if block runs only if the condition evaluates to True.
If the condition is False, the else block runs instead.
You can also use elif (short for "else if") to check multiple conditions in sequence.

if condition:
    - Code block runs if condition is True

elif another_condition:
    - Code block runs if the first condition is False and another_condition is True

else:
    - Code block runs if none of the above conditions are True

"""

x = 30

if x > 0:
    print("x is a positive number.")

elif x == 0:
    print("x is zero.")

else:
    print("x is a negative number.")

# nested if statements
if x > 0:
    if x < 20:
        print("x is a positive number less than 20.")

# combined conditions

age = 18

if age >= 18 and age <= 21:
    print("You are between 18 and 21 years old.")
    

username = "john123"

if username == "peter321":
    print("You are peter")

"""

Mini-Challenge

1. Ask the user to enter a number from 0-100 and store in a variable called score.
2. If the score is under 90 or above, print "Grade A"
3. If the score is between 80-89, print "Grade B"
4. If the score is between 70-79, print "Grade C"
5. Otherwise, print "Grade F"

"""

score = int(input("Enter your score (0-100): "))

if score >= 90:
    print("Grade: A")

elif score >= 80 and score <= 89:
    print("Grade: B")

elif score >= 70 and score <= 79:
    print("Grade: C")

else:
    print("Grade: F")

"""
Mini-Challenge

1. Ask the user to enter today's temperature in fahrenheit and store it in a variable called temperature.
2. Use if-elif-else statements to print out the following messages based on the temperature:
    - If the temperature >= 86, print "It's hot outside!"
    - If the temperature >= 65 and temperature <= 86, print "The weather is nice."
    - If the temperature >= 50 and temperature <= 68, print "It's a bit chilly."
    - If the temperature is below 50, print "It's cold outside!"

"""

temperature = float(input("Enter today's temperature in Fahrenheit: "))

if temperature >= 86:
    print("It's hot outside!")

elif temperature >= 65 and temperature <= 86:
    print("The weather is nice.")

elif temperature >= 50 and temperature <= 68:
    print("It's a bit chilly.")

else:
    print("It's cold outside!")