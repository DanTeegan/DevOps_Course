# What are loops

# for loops are used to iterate through Lists, Strings, Dictionaries and Tuples
# Syntax - for variable in a name of the data_collection(list,string,dictionary or tuple)

# Syntax for using a for a for loop. Indentation is crucial within python otherwise the code wont run
list_data = [1, 2, 3, 4, 5]
for data in list_data:
    if data > 4:
        break
    print(data)

# break keyword used to stop the for loops when a certain condition is not met

print(list_data[1]) # Used to display the 1st index of the variable list_data

list_data = [1, 2, 3, 4, 5]
for data in list_data:
    if data > 4:
        print("Data is correct")
    elif data < 0:
        print(" Please enter number above 0")
    print(data) # Print data block should be inline with the if block

# Create a string and loop through the string
city = "London"
for letter in city:
    print(letter)

# # Print the string in one line
name = "Daniel"
for index in name:
    in_one_line += " " + index
    if name[-1] == index:
        print(in_one_line)

# Looping through a dictionary

student_record = { "name": "Daniel",
                   "stream": "DevOps",
                   "completed_lessons": 5,
                   "completed_lessons_names": ["strings", "tuples", "variables"]
}

for x in student_record:
    print(x, ":", student_record[x])

# Exercise

# Dictionaries with employee records minimum 5 key value pairs
# Using loop iterate through the dictionary
# Display the values of and keys of the dictionary

# Differance between for and while loops
