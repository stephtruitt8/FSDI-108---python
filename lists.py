# Lists In Python

"""
A List is a built-in data type in Python that is used to store
multiple items in a single variable.

variable_name = [item1, item2, item3, ...]
"""


# Example of creating lists
my_list = [10, 20, 30, 40]
print(my_list)

mixed_list = [1, "apple", 3.5, True]
print(mixed_list)


# Accessing Items
#            [0]      [1]       [2]
fruits = ["apple", "banana", "cherry"]
print(fruits[1])  # Output: banana
print(fruits[0]) # Output: apple
print(fruits[2]) # Output: cherry 

print(fruits[-1])  # Output: cherry (last item)
print(fruits[-2])  # Output: banana (second last item)
print(fruits[-3])  # Output: apple (third last item)



# Slicing Lists
print(fruits[0:2]) # items from index 0 to 1
print(fruits[:2]) # first 2 elements
print(fruits[1:]) # items from index 1 to end

# Modifying Lists (To replace an item)
fruits[1] = "mango"
print(fruits)  # Output: ['apple', 'Mango', 'cherry']



# Adding Items
fruits.append("orange")  # Adds 'orange' at the end
print(fruits)  # Output: ['apple', 'Mango', 'cherry', 'orange']

fruits.insert(1, "kiwi")  # Inserts 'kiwi' at index 1
print(fruits)  # Output: ['apple', 'kiwi', 'Mango', 'cherry', 'orange']



# Removing Items
fruits.remove("apple")  # Removes 'apple' from the list
print(fruits)  # Output: ['kiwi', 'Mango', 'cherry', 'orange']

fruits.pop()  # Removes the last item
print(fruits)  # Output: ['kiwi', 'Mango', 'cherry']

del fruits[0]  # Deletes item at index 0
print(fruits)  # Output: ['Mango', 'cherry']

# List Length
print(len(fruits))  # Output: 2
print(len(["cohort63", True, "Python", 3.1416, 2025])) # Output: 5
# Returns the number of items in the list

"""
Mini-Challenge:
1. Create a list of your favorite movies.
"""
"""
print("-------- Mini-Challenge Solution: --------")
favorite_movies = ["Rush Hour", "Scott Pilgrim vs. The World", "Napolean Dynamite", "Sonic the Hedgehog"]
favorite_movies[1] = "Inception"
favorite_movies.remove("Napolean Dynamite")
del favorite_movies[2]
print(favorite_movies)
print(len(favorite_movies))

"""




"""
---------- Assignment #2 ----------

games = ["The Legend of Zelda", "Super Mario Bros", "Minecraft", "Fortnite", "Among Us"]
1. Replace "Minecraft" with "Cyberpunk 2077".
2. Add "Elden Ring" to the end of the list.
3. Remove "Fortnite" from the list. 
4. Print the final list and its length.

"""

print("-------- Assignment #2 Solution: --------")
games = ["The Legend of Zelda", "Super Mario Bros", "Minecraft", "Fortnite", "Among Us"]
print(games) # Initial list 
games[2] = "Cyberpunk 2077"
print(games) # After replacing "Minecraft"
del games[3]  # Removing "Fortnite"
print(games) # After removing "Fortnite"

print(len(games)) # Length of final list