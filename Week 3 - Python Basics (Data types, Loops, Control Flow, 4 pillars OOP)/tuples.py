# What is a tuple
# same as lists but are IMMUTABLE
# WHY Tuples -  To store the data that would not need changing I.E. Date of brith, passport number, etc..

# Syntax of Tuple: we use () to create a Tuple

dob = ("Name", "DOB", "Passport No")
print(dob)

print(dob.__len__()) # This will return the total number of data in the Tuple

# Convert the tuple into a list

dob_list = list(dob) # This will convert the tuple into a list
print(dob_list) # This is just to check weather the tuple has been converted
print(type(dob_list)) # We use type() to verify that the tuple has been converted to a list

# add your name into the string at 0 index

dob_list.insert(0, "Daniel") # This is used to add Daniel into the 0 index

dob_list[0] = "Daniel" # This will replace the 0th index with the string Daniel

# display the list
print(dob_list)
