"""SCRIPT"""

# BOILERPLATE
import random

# this generates a random number between 1 and 10
number = random.randint(1, 10)

TRIES = 0

# GAME LOOP
while True:
    guess = int(input("Guess a number between 1 and 10: "))

    # implement your logic below
