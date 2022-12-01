"""SCRIPT"""

# BOILERPLATE
import random

# this generates a random number between 1 and 10
number = random.randint(1, 10)

TRIES = 0

# GAME LOOP
while True:

    if TRIES > 3:
        print('you lose')
        break

    guess = int(input("Guess a number between 1 and 10: "))

    # implement your logic below
    if guess == number:
        print("Correct")
        break

    if guess > number:
        print("too high")

    else:
        print("too low")

    TRIES = TRIES + 1