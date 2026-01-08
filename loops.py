"""
Loops

A for loop in Python is a control structure that lets you repeat a block of code for each item in sequence
such as (list, tuple, dictionary or a range of numbers).

for variable in sequence:
    - Code block to be executed for each item in the sequence

"""

fruits = ["apple", "banana", "cherry"] #list

for fruit in fruits:
    print(fruit)

print("-----")

for letter in "Steph": #string
    print(letter)

print("-----")  

for number in range(5):
    print(number) # Output: 0, 1, 2, 3, 4 because range() only includes numbers less than the stop value. 

print("-----")

for number in range(2, 6): #range with start and stop
    print(number)

print("-----")

for number in range(1, 10, 2): #range with start, stop and step
    print(number)

print("-----")

"""
Mini-Challenge

1. Ask the user to enter a number and store it in a variable called num
2. Use a for loop with range(1,11) to repeat 10 times (from 1 to 10)
3. Inside the loop, multiply num by the current loop value.

"""

num = int(input("Enter a number: "))

for i in range(1, 11):
    result = num * i
    print(f"{num} x {i} = {result}")




"""
While loops

A while loop repeats a block of code as long as a condition is True.

while condition:
    - Code block run as long as condition is True

"""

print("-----")

count =  1

while count <=5:
    print("Count is:", count)
    count += 1  # Increment count to avoid infinite loop

number = 0

while True: # Infinite loop
    print(number)
    number += 1
    if number == 3:
        break  # Exit the loop when number reaches value