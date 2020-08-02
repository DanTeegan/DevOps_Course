

# If divisible by 3 % 3 = 0
# If divisible by 5 % 5 = 0


class fizz_buzz:

    def fizz_buzz_finder(self):

        for number in range(1, 101):
            if number % 3 == 0:
                print("Fizz")
            elif number % 5 == 0:
                print("Buzz")
            elif number % 3 == 0 and number % 5 == 0:
                print("Fizz-Buzz")
            else:
                print(number)

fizzbuzz1 = fizz_buzz()
fizzbuzz1.fizz_buzz_finder()