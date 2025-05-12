import random

number = random.randint(1, 20)

while True:
    guess = input("Guess a number between 1 and 20 (x=exit, s=show): ")
    if guess == 'x':
        print("Goodbye!")
        break
    elif guess == 's':
        print(f"(Cheat) The number is: {number}")
        continue
    guess = int(guess)
    if guess < number:
        print("Too small!")
    elif guess > number:
        print("Too big!")
    else:
        print("Correct!")
        break
