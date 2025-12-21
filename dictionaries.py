# Dictionaries in Python
"""
A Dictionary is a built-in data structure in Python that is used to store
data in key-value pairs.
Dictionaries are mutable, ordered, keys must be unique.

OPTION 1
my_variable = {"key1": value1, "key2": value2, ...}

OPTION 2
my_variable = {
    "key1": value1,
    "key2": value2,
    ...
}
"""

# Creating a dictionary
student = {
    "name": "John",
    "age": 68,
    "major": "Physics"
}

print(student)

new_student = {
    "name": "Pam",
    "age": 22,
    "name": "Angela"  # Duplicate key, will overwrite previous "name"
    
}
print(new_student)  # Output: {'name': 'Angela', 'age': 22}


# Accessing Items
print(student["name"])  # Output: John
print(student["age"])   # Output: 68
print(student["major"])  # Output: Physics


# Adding Items
student["graduation_year"] = 2025
print(student)

# Changing Values
student["age"] = 70
print(student)

# Removing Items
student.pop("major") # Removes the item with key "major"
print(student)

del student["name"] # Removes the item with key "name"
print(student)

# Dictionary Length
print(len(student))  # Output: 2

# Clearing a Dictionary
student.clear()
print(student)  # Output: {}  


# Nested Dictionaries
students_group = {
    "student1": {
        "name": "Alice",
        "age": 20
    },
    "student2": {
        "name": "Bob",
        "age": 22
    }
}

print(students_group)
print(students_group["student1"]["name"])  # Output: Alice


"""
----------
Mini-Challenge: Song Metadata 


"""

song = {
    "title": "Imagine",
    "artist": "John Lennon",
    "duration": 183,
}
print(song["title"])

#add
song["album"] = "Imagine"

#update value
song["duration"] = 201
print(song)

#remove
song.pop("album")
print(song)

#length
print(len(song))  # Output: 3

"""
---------- Assignment #2 -----------
"""


games = {
    "title": "The Legend of Zelda",
    "genre": "Adventure",
    "platform": "Nintendo Switch",
}

print(games["title"])

games["release_year"] = 2017

print(games["release_year"])

games["platform"] = "Nintendo Wii U"

print(games)

games.pop("genre")
print(games)

print(len(games))  # Output: 3  