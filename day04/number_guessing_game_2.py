import random

number = random.randint(1, 20)

while True:
    guess = input("Guess a number between 1 and 20 (or 'x' to exit): ")
    if guess == 'x':
        print("Goodbye!")
        break
    guess = int(guess)
    if guess < number:
        print("Too small!")
    elif guess > number:
        print("Too big!")
    else:
        print("Correct!")
        break
