
print(" Hello world ")

# Let's create a variable

x = 10  # Type of integer
y = 3.6 # Type of float (Decimal)
name = "Sparta" # Type of string

print(x)
print(y)
print(name)
print(x + y)

# Built in method called type()

print(type(name)) # Returns the type of data in this case it is a string

print( x + name ) # You cannot add together data types of string and int

print(str(x) + name) # You must convert the INT into a string using the str() function. This is known as casting.

age = 99
NHS = 1231312
name = input("Please enter your name")
salary = 50000

name = input(" Please enter your name ")
age = input(" Please enter your age ")
print(name)
print(age)

# Overwriting a variable
name = "James"
print(name)
name = "bond"
print(name)

# Exercise

# create a variable called first_name and last_name
# create a variable called full_name and display full_name

first_name = input("Please enter your first name: ")
last_name = input("Please enter your last name: ")
full_name = first_name + last_name
display_full_name = (first_name + " " + last_name + "," + " ")
age = (str(input("Please enter your age: ")))
adress = input("Please enter your adress: ")

x = "Hello "
y = "you are "
z = " years old and live at "


print( x + display_full_name + y + age + z + adress )



# Python operators

x = 10
y = 11

print(x == y) # Checking the values as Boolean resulting True or False
print(x != y) # Checking the values as Boolean resulting True or False

print(x > y)

print(x < y)

print(x <= y)

print(x >= y)

# Lets check a real life example now to understand it better

age = 18

print(age < 19)

print(3 % 9) # Modulus gives the remainder


print("Hello world")

print('Hello world')

# What is the bet practice and why?
# Using double quotes is better practice
# Why? lets see an example

print('\'Ugnes\'s class is eng 67') # single quotes

print("Ugne's class is eng 67") # Double quotes

# Strings, indexing, casting, slicing, concatenation

greeting_welcome = "Hello world"

welcome_user = input("Please enter your name ")

print(" Dear " + welcome_user + " welcome on board") # concatenation

# H E L L O W O R L D
# 0 1 2 3 4 5 6 7 8 9
#-9                -1

print(len(greeting_welcome))
# indexing

# lets move onto STRING slicing

hi = "Hello world"

print(hi[0]) # This will return the index H because in python the 1st character is the 0 index.

print(hi[10]) or print(hi[-1]) # Use either to obtain the last index of the hi variable

print(hi[0:5]) # This can be used when you want to select a world to print in this case the word is HELLO

print(hi[6:11]) # This can be used when you want to select a world to print in this case the word is WORLD

print(hi[-6:-1]) # An example of how we can also use negative indexes to pull information from the string

remove_white_space = "remove the space at the end of a string     "
print(len(remove_white_space))

print(len(remove_white_space.strip())) # We can use strip() to get rid of any spaces at the end of a string

# Boolean values within DATA types

use_text = "heres's SOME text with lot's of text"

 count() # counts the substring within the string
print(use_text.count("text"))

# Brings everything to lowercase lower()
print(use_text.lower())

# Brings everything to uppercase UPPER()
print(use_text.upper())

# Bring the first letter to uppercase of a sentence capitalize() - MAINLY USED IN REAL WORLD
print(use_text.capitalize())

# Replacing text in the string
print(use_text.replace("with", ",")) # How you can use replace() to replace anything in a string

print(use_text.startswith("h")) # Boolean value is presented weather the first letter is h or not