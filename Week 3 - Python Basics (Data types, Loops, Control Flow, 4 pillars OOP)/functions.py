# What is a function?

# Why should we use a function

# What is the benefit - REUSABLE block of code

# D R Y - Do Not Repeat Yourself

# What functions have we used so far? - print(), type(), str(), int()

# Syntax: def name_of_function with () and :

# Create a function to greet
# def greeting():
#     return "Hello world"
    # pass # pass will skip the function, tells the python operator to skip the function, no errors will apear.

# print(greeting()) # We can use print to call the function

#def test():
  #  pass # Pass will skip the methods and there will be no outcome.
         # Pass is used in created or building a unit test.

# Methods with parameters/arguments

# def add_values():
#     return 4 + 4 # We can return anything - Strings, int with + operator
#
# print(add_values())


# def add_values(number1, number2): # Passing the function an argument of 2 numbers
#     return number1 + number2 # This returns the values of Number1 + Number2
#
# print(add_values(4,9)) # Print will then return the value of the numbers passed into the argument

# Divide function
def divide_values(number1, number2): # Passing the function an argument of 2 numbers
    return number1 / number2 # This returns the values of Number1 + Number2
#
print(divide_values(4,9)) # Print will then return the value of the numbers passed into the argument


# create a function with two args to return a subtraction of the 2 values given

def subtract(num1, num2):
    return num1 - num2
print(subtract(10,2))

# create a function with two args to return a division of the 2 values given

def divide(num1, num2):
    return num1 / num2
print(divide(100,10))

# create a function with two args to return a remainder of  of the 2 values given

def remainder(num1, num2):
    return num1 % num2
print(remainder(100,7))

# create a function with two args to return a * of the 2 values given

def multiply(num1, num2):
    return num1 * num2
print(multiply(10,7))


# User input multiply

num1 = int(input("Please enter a number"))
num2 = int(input("Please enter a 2nd number"))

def multiply (num1, num2):
    return num1 * num2

print(multiply(num1, num2))

# User input divide

num1 = int(input("Please enter a number"))
num2 = int(input("Please enter a number"))
def divide(num1, num2):
    return num1 / num2
print(divide(num1, num2))


# User input add
num1 = int(input("Please enter a number"))
num2 = int(input("Please enter a number"))
def add(num1, num2):
    return num1 + num2
print(add(num1, num2))

def multi_args(*multiargs): # Here we have given multiple arguments

    for args in multiargs: # This will iterate through the arguments
        print(args)
    return args # Return will end the function

print(multi_args(1, 2, 2, 3, 3, 4, 4, 5, ))

