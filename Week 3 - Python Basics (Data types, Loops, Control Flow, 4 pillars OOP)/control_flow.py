# What is control flow?

# conditional statements and loops

# if, elif, else, for loop, while loop

weather = "sunny"
if weather == "sunny":
    print(" Lets go to the beach")

weather = "snow"
conditional_weather = "rainy"

# conditional block of code
if weather == "sunny" and conditional_weather == "rainy": # For this both conditions must be TRUE
    print(" Lets go to the beach!")
else:
    print(" Sorry better luck next time")
# We use AND when both conditions must be true

# Using OR operator
# We use OR when one of the conditions must be true
if weather == "sunny" or conditional_weather == "rainy": # For this both conditions must be TRUE
    print(" Lets go to the beach!")
else:
    print(" Sorry better luck next time")

if age == 18 or age > 18: # For this both conditions must be TRUE
    print(" Please proceed to checkout")
else:
    print(" SSorry you are to young to watch the movie")

# To simplify the code we can use just one operator as seen below:
age = 18

if age >= 18:
    print(" Please proceed to checkout")
else:
    print(" SSorry you are to young to watch the movie")

# What are sets - sets are very similar to Lists

# What is the difference between a set and a list? - sets are unordered

# Syntax for sets: We us {} brackets

# Lets create a set!

car_part = {"Wheels", "Windows", "Doors"}
print(car_part)

# What can we do with sets
# Add an item to the set

car_part.add("Seats") # Seats will be added into the 0 Index
print(car_part)

car_part.discard("Windows") # Used to remove an item from the set
print(car_part)

#Frozen set - it is immutable

#Syntax - We use () store them in a variable first

counting = frozenset([1, 2, 3, 4])
print(counting)


name = "daniel"

print("Hello {} how are you".format(name))