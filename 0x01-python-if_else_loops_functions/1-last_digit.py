#!/usr/bin/python3


import random
number = random.randint(-10000, 10000)
if number < 0:
    num_last = number % -10
elif number >= 0:
    num_last = number % 10
if num_last > 5:
    print(f"Last digit of {number} is {num_last} and is greater than 5")
elif num_last == 0:
    print(f"Last digit of {number} is {num_last} and is 0")
else:
    print(f"Last digit of {number} is {num_last} and is less than 6 and not 0")
