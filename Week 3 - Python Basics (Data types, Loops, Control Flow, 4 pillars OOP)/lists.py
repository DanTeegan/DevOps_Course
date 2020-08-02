# Data collection

# Java they use arrays in python lists are the same as arrays
# both serve the same purpose of storing data
# why should we use a list?
# Helps to manage data, helps to access data in order it gives us the option to add, remove etc..

# Syntax of list: [] list, () tuple, {} dictionary - key:value
# Tuples are immutable - meaning they cannot be edited

# Lets create a list of cities

cities = ["Tokyo", "Paris", "Prague", "Luxumberge"]
#display (print()) list the cities
print(cities)
print(type(cities))

print(cities[3]) # This will print the string luxumberge
print(cities[1]) # This will print the string Paris
cities[3] = "Helsinki" # This will replace the string with the 3rd index with the new city input
print(cities)

cities.append("Vilnius") # append() will add the new string into the list. it was add it on the end of the list
print(cities)

cities.remove("Paris") # This will remove the string of Paris from the list
print(cities)


# cities = ["Tokyo", "Paris", "Prague", "Luxumberge"]
# cities.pop() # pop() would delete the last index in the list
# print(cities)
#
cities.insert(0, "Hesinki") # insert() used add a string to a list. You can choose the position of the index where it will be added
# print(cities)

# mix_type_string = [1,2,3, "one", "two", "three"]
# print(mix_type_string)

# Below shows how we can use multiple lists
mix_type_string = [[1,2,3], ["one", "two", "three"]]

# or we can use multiple lists as seen below

mix_type_string = [1,2,3]

string_list = ["one", "two", "three"]

print(mix_type_string + string_list)

# Lists are able to store and concatenate any data type









