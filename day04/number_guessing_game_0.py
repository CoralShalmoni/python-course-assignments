import random

number = random.randint(1, 20)
guess = int(input("Guess a number between 1 and 20: "))

if guess < number:
    print("Too small!")
elif guess > number:
    print("Too big!")
else:
    print("Correct!")
