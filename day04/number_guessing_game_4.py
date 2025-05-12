import random

number = random.randint(1, 20)
debug = False

while True:
    if debug:
        print(f"(Debug) The number is: {number}")
    guess = input("Guess a number between 1 and 20 (x=exit, s=show, d=debug): ")
    if guess == 'x':
        print("Goodbye!")
        break
    elif guess == 's':
        print(f"(Cheat) The number is: {number}")
        continue
    elif guess == 'd':
        debug = not debug
        print(f"Debug mode {'on' if debug else 'off'}")
        continue
    guess = int(guess)
    if guess < number:
        print("Too small!")
    elif guess > number:
        print("Too big!")
    else:
        print("Correct!")
        break
