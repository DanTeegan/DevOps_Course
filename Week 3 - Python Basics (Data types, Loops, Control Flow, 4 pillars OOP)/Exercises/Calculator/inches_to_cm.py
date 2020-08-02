

print("1 - INCHES to CM")
print("2 - CM to INCHES")

user_input = int(input("Please choose your metric conversion: "))

if user_input == 1:
    inches_to_cm = int(input("Please enter your metric in INCHES: "))
    print(str(inches_to_cm * 2.54) + ": CM")
elif user_input == 2:
    cm_to_inches = int(input("Please enter your metric in CM: "))
    print(str(cm_to_inches * 0.393701) + ": INCHES")
else:
    print("Error please enter correct value")
