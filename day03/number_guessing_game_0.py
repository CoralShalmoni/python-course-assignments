import random

# Generating random number
secret_number = random.randint(1, 20)

# User makes a guess
guess = int(input("Guess a number between 1 and 20: "))

# Checking the guess
if guess < secret_number:
    print("Too low!")
elif guess > secret_number:
    print("Too high!")
else:
    print("Correct! You guessed it!")
