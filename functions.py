"""
Functions

A function is a block of code that only runs when it is called.
We can pass data to functions(parameters). And they can return data as a result.

def function_name(parameters):
    - Code block (indeted)
    - return value (optional)

"""

def my_function():
    print("This is a function.")

#call the function
my_function()

def other_function():
    print("This is another function.")

other_function()

def hello():
    cohort = 64
    print("Ello Cohort #", cohort)

hello()  # Output: Ello Cohort # 64
hello()
my_function()
other_function()
hello()

def get_full_name(first_name, last_name):
    return f"hello {first_name} {last_name}" #sends back the full name as text

   full_name = get_full_name("Steph", "Truitt")
   print(full_name)

   # default parameter
   def greet(name="Steph"):
       return (f"Hi {name}, welcome to the class!")

greet()
greet("Pam")
greet("Angela")