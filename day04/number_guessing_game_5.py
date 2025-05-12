import random

number = random.randint(1, 20)
debug = False
move_mode = False

while True:
    if debug:
        print(f"(Debug) The number is: {number}")
    guess = input("Guess (x=exit, s=show, d=debug, m=move): ")
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
    elif guess == 'm':
        move_mode = not move_mode
        print(f"Move mode {'on' if move_mode else 'off'}")
        continue
    guess = int(guess)
    if guess < number:
        print("Too small!")
    elif guess > number:
        print("Too big!")
    else:
        print("Correct!")
        break
    if move_mode:
        number += random.choice([-2, -1, 0, 1, 2])
        number = max(1, min(20, number))  # Keep in bounds
