# Program to filter which movies you can watch based on inputted age.

# This is the input for the user.
age = int(input("Please enter your age: "))
# This block of code will print a message if the user is over 100
if age >= 100:
    print("Wooow, you are {}, you can do whatever you want".format(age))
# This block of code will print a message if the user is over 21
elif age > 21:
    print("You are {}, so you can go to Vegas and watch any film.".format(age))
# This block of code will print a message if the user is between the ages of 18-20
elif 18 <= age < 21:
    print("You are {}, so cannot go to Vegas but can watch any film.".format(age))
# This block of code will print a message if the user is between the ages of 15-17
elif 15 <= age < 18:
    print("You are {}, so the movies you can watch are U rated, PG rated, 12a rated and 15 rated.".format(age))
# This block of code will print a message if the user is between the ages of 13-17
elif 13 < age < 15:
    print("You are {}, so the movies you can watch are U rated, PG rated and 12a rated.".format(age))
# This block of code will print a message if the user is equal to 12
elif age == 12:
    print("You are {}, so the movies you can watch are U rated, PG rated and 12a rated if you have an adult with you.".format(age))
# This block of code will print a message if the user is between the ages of 4-11
elif 4 < age < 12:
    print("You are {}, so the movies you can watch are U rated and PG rated.".format(age))
# This block of code will print a message if the user is less than 3
else:
    print("goo goo gaa gaa, U rated movies only for you.")


# Employee dictionary task

employee_record = { "name": "Daniel",
                    "age": 25,
                    "stream": "DevOps",
                    "completed_lessons": 13,
                    "completed_lessons_names": ["strings", "tuples", "variables", "dictionaries", "loops"]
}
for employee in employee_record:
    print(employee,":", (employee_record[employee]))

# employee will print the key and (employee_record[employee] will print the values