#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if numbet >= 0
    r = abs(number) % 10
else:
    r = ((r * -1) % 10)* -1
if r == 0:
    print(f"Last digit of {number:d} is {r:d} and is 0")
elif r > 5:
    print(f"Last digit of {number:d} is {r:d} and is greater than 5")
else:
    print(f"Last digit of {number:d} is {r:d} and is less than 6 and not 0")
