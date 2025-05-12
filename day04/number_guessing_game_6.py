import random

debug = False
move_mode = False

def new_game():
    return random.randint(1, 20)

number = new_game()

while True:
    if debug:
        print(f"(Debug) The number is: {number}")
    guess = input("Guess (x=exit, s=show, d=debug, m=move, n=new game): ")
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
    elif guess == 'n':
        print("Starting new game...")
        number = new_game()
        continue
    try:
        guess = int(guess)
    except ValueError:
        print("Invalid input.")
        continue
    if guess < number:
        print("Too small!")
    elif guess > number:
        print("Too big!")
    else:
        print("Correct!")
        number = new_game()
        print("New game started!")
    if move_mode:
        number += random.choice([-2, -1, 0, 1, 2])
        number = max(1, min(20, number))
