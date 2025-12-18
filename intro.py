# Python Basics - Session#1 

print("Hello World from Python!") #no semicolons needed 
print(2) # printing a number
print(5 + 3) # Printing the result of a match operation

print("Cohort#63 Welcome")

# Shortcuts (save File)
# Windows: ctrl + S

"""
This is a multi-line comment
Triple quotes let you write longer explanations.

"""

# ----- Variables and contatenation -----

name = "Angela" #string
age = 28 #integer
print(name) #prints the variable value
print(age) 

print("My name is " + name + " and I am "  + str(age) + " years old.")

first_name = "Michael" #snake_case
middle_name = "John"
last_name = "Scott"
age = 46
print("My name is " + first_name + " " + middle_name + " " +last_name + " and I am " + str(age) + " years old. " )

# ----- F-String (Cleaner way to format strings) -----

print(f"hello")
print(f"My name is {first_name} {middle_name} {last_name} and I am {20+33} years old.")
 #add curly braces to insert variables

# Multi-line F-string 
print(f"""
My name is {first_name} {middle_name} {last_name}
and i am {age} years old.
""")

# MINICHALLENGE 1
"""

"""

my_name = "Stephen"
my_last_name = "Truitt"
my_age = 33
my_city = "Cleveland, OH"
my_hobby = "draw"
my_favorite_technology = "Videogames"

print(f"My name is {my_name} {my_last_name}, I am {my_age} years old and I'm from {my_city}. I love to {my_hobby} and my favorite technology is {my_favorite_technology}.")

# Type function
print(type("Peter")) #string
print(type(last_name)) #string variable
print(type(True)) #boolean 
print(type(1234)) #integer

# ----- Input Function -----
user_name = input("Enter your name: ") #input function to get user input
print(f"Hello {user_name}")

user_age = int(input("Enter your age: ")) #common approuch to convert input to integer
print(f"You are {user_age - 1} years old.")