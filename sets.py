"""
Sets in Python


A set is a built-in data structure in Python that is used to store unique items.
sets are unordered, unindexted and do not allow duplicate values.

my set = {item1, item2, item3, ...}

"""

fruits = {"apple", "banana", "cherry"}
print(fruits)

fruit = {"apple", "banana", "cherry", "apple"}
print(fruits) # apple duplicate will be ignored

print("banana" in fruits)  # True

fruits.add("orange") #add single item
print(fruits)

fruits.update(["kiwi", "mango"]) #add multiple items
print(fruits)

fruits.remove("banana") #removes item, raises error if not found
print(fruits)

fruits.discard("watermelon") #removes item, does not raise error if not found
print(fruits)

# Set Operations
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

print(set1.union(set2)) # combines both sets with no duplicates
print(set1.intersection(set2)) # common elements
print(set1.difference(set2)) # elements in set1 but not in set2

#length 
print(len(set1))

# copying sets
new_set = set1.copy() 
print(new_set)

# clearing sets
set1.clear()
print(set1)  # Output: set()  

