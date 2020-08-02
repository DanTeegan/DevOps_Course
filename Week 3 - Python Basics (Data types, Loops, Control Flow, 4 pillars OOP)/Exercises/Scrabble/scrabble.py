


pointers1 = ['a', 'e', 'i', 'o', 'u', 'l', 'n', 'r', 's', 't']
pointers2 = ['d', 'g']
pointers3 = ['b', 'c', 'm', 'p']
pointers4 = ['f', 'h', 'v', 'w', 'y']
pointer5 = ['k']
pointer8 = ['j', 'x']
pointers10 = ['q', 'z']

# I then used a function to assign the numerical values to the pointer values, 0 being the default
def scrabble_calc(word):
    value = 0

    # So, if a letter in the word argument falls in the 1 pointers list, add 1 to values
    for letter in word:
        if letter in pointers1:
            value += 1
        # So, if a letter in the word argument falls in the 2 pointers list, add 2 to values etc
        elif letter in pointers2:
            value += 2
        elif letter in pointers3:
            value += 3
        elif letter in pointers4:
            value += 4
        elif letter in pointer5:
            value += 5
        elif letter in pointer8:
            value += 8
        elif letter in pointers10:
            value += 10
    return value

# this is where i enter the value for what word i want to scrabble calculate and the result is printed in the console
print(scrabble_calc("laptop"))