import random

guesses = 0
print("Welcome to the Number Guessing Game!")
number = random.randint(1, 10)
print("I have selected a number between 1 and 10.Can you guess what it is?")
guess_number = (input("Guess a number between 1 and 10: "))
if guess_number.isdigit():
    guess_number = int(guess_number)
    while guess_number != number:
        guesses += 1
        if guess_number < number:
            guess_number = int(input("Too low! Guess again: "))
        elif guess_number > number:
            guess_number = int(input("Too high! Guess again: "))
    guesses += 1
    print(f"Congratulations! You've guessed the number {number} in {guesses} tries.")