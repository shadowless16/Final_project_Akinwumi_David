import random

def number_guessing_game():

    print("Welcome to the Number Guessing Game!")

    secret_number = random.randint(1, 100)

    while True:
        guess = input("Enter your guess: ")

        if not guess.isdigit():
            print("Please enter a valid number.")
            continue

        guess = int(guess)

        if guess == secret_number:
            print(f"Congratulations! You guessed the number {secret_number} correctly!")
            break
        elif guess < secret_number:
            print("Too low. Try a higher number.")
        else:
            print("Too high. Try a lower number.")

number_guessing_game()
