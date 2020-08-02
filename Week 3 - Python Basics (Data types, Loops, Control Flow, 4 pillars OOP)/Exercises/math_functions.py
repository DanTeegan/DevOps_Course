# How can we use built-in python libraries

from random import random
import math # import built in modules/libraries/functions

# To generate a random number - mostly used in gambling/lottery to make it fair.
print(random())

float_num = 24.99 # Float

# round the float number
print(math.ceil(float_num)) # ceil is used to round the number up
print(math.floor(float_num)) # floor is used to round the number down
print(math.pi)

def round_up(num):
    return int(num)

print(round_up(float_num))

# Create a method that would take 1 argument

# Calculate cm into inches or vice versa


# CM to INCHES calculation (values defined)
def cm_convertion_inches(cm_value):
    return float(cm_value) * 0.3937

print(cm_convertion_inches(101.5))



# CM to INCHES calculation (User input)
num_cm = float(input("Please enter your measurment in CM: ")) # Here we ask for the user input as a float

def cm_covertion_inches(num_cm): # Creating the function that converts cm to inches
    return num_cm * 0.3937 # Taking the argument inputted by the user and multiplying by 0.3937

print(str(cm_covertion_inches(num_cm)) + " Inches") # Printing the results of the CM to INCHES convertion





def cm_to_inches(num1, num2):
    num3 = num1 + num2
    return num3/2.54

print(cm_to_inches(10, 10))