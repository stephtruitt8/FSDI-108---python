"""
Tuples in Python

A tuple is a built-in data structure in Python, Like a list/
tuples can store multiple item, but the are immutable.

my_tuple = (item1, item2, item3, ...)

"""

my_tuple = ("apple", "banana", "cherry")
print(my_tuple)

print(my_tuple[0]) # first item
print(my_tuple[2]) #third item

#length
print(len(my_tuple))

# single-item tuple
single = ("apple",)
print(type(single)) 
print(single)

correct = ("apple",)
print(type(correct))
print(correct)

print(my_tuple[0:2]) #slicing

# Nested tuples
tuple1 = ("a", "b", "c")
tuple2 = (1, 2, 3)
combine = (tuple1, tuple2)
print(combine)

temp_list = list(my_tuple)
print(temp_list)

temp_list.append("orange")
my_tuple = tuple(temp_list)
print(my_tuple)



"""
Mini-Challenge

1. Create a tuple calling travel_bag with a least 5 items: "shirt", "socks", "pants", "jacket", "shoes".
2.Print the second and foruth items.
3. Make a new tuple called essentials with 3 must-have items.


"""

travel_bag = ("shirt","socks","pants", "jacket", "shoes")
print("--Mini Challenge --")
print(travel_bag)

print(travel_bag[1])
print(travel_bag[3])

essentials = ("Switch", "Toothbrush", "Soap")
print(essentials)