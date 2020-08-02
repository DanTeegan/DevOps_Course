# dictionaries

# What is a dictionary? - Data collection
# It is a bit more dynamic than tuples or lists.
# How? very useful tool within any coding language
# Simple concept of KEY VALUE PAIRS

# Syntax - to create a dictionaries we use {}

# Let's now create an example to learn by doing
            #       KEY       VALUE
student_record = { "name": "Daniel",
                   "stream": "DevOps",
                   "completed_lessons": 5,
                   "completed_lessons_names": ["strings", "tuples", "variables"]
}
for student in student_record:
    print(student, ":", student_record[student])
print(student_record)
print(type(student_record))

print(sorted(student_record))
print(student_record.values())
student_record["completed_lessons_names[1]"] = 3
new_list = student_record["completed_lessons_names"]

print(new_list)

# Add 2 topics that we have covered
student_record["completed_lessons_names"].append("Lists")
student_record["completed_lessons_names"].append("built-in methods")

# display the list
print(student_record)

print(student_record["stream"]) # to fetch the value of stream

print(student_record["completed_lessons_names"][1])

print(student_record["completed_lessons_names"][2]) # Using index of 2 to draw the string variables

print(student_record["name"]) # drawing the name variable from the dictionary

