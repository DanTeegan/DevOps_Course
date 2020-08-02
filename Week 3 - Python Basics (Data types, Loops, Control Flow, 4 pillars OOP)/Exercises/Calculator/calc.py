# # Here we are importing the file name operators
# import operators
#
# # Here we are creating a class called calc
# class calc:
def user():
    print("Please choose from the options given below:")
    print("I --Insert passenger info-- I ")
    print("S ----Select passengers---- S")
    print("C -----Create manifest----- C")

    exit = True
    while exit:
        user_input = input("Please choose the function you would like to run: ")

        if (len(user_input) < 1 or len(user_input) > 1) and (user_input != "I" or "i" or "S" or "s" or "C" or "c"):
            print("ERROR: Please enter a correct option:")
            user()
        elif user_input == ("I" or "i"):
            passengers.insert_passenger_info()
        elif user_input == ("S" or "s"):
            passengers.select_passengers()
        elif user_input == ("C" or "c"):
            passengers.create_manifest()
            exit = False
            # user()

        # elif user_input == ("I" or "i"):
        #     passengers.insert_passenger_info()
        # elif user_input == ("S" or "s"):
        #     passengers.select_passengers()
        # elif user_input == ("C" or "c"):
        #     passengers.create_manifest()

user()







#








#     elif user_input != ("I" or "i" or "S" or "s" or "C" or "c"):
#         print("ERROR: Please enter a correct option:")
#
#     elif user_input == ("I" or "i"):
#         passengers.insert_passenger_info()
#     elif user_input == ("S" or "s"):
#         passengers.select_passengers()
#     elif user_input == ("C" or "c"):
#         passengers.create_manifest()
# # elif user_input == ("Q" or "q"):
#
# while True:
#     try:
#         if len(user_input) < 1 or len(user_input) > 1:
#             raise ValueError
#         break
#     except ValueError:
#         print("ERROR: Please enter a correct option:")
#
#
