import random
import sys

def number_guessing_game():
    number = random.randint(1, 100)
    attempts = 0
    print("Welcome to the Number Guessing Game!")
    print(f"I have picked a number between 1 and 100. Try to guess it! {number}")

    while True:
        if len(sys.argv) < 2:
            print("No guess provided. Please run the script with a number argument.")
            break

        try:
            guess = int(sys.argv[1])
        except ValueError:
            print("Invalid guess. Please provide an integer as an argument.")
            break

        attempts += 1

        if guess < number:
            print("Too low! Try a higher number.")
        elif guess > number:
            print("Too high! Try a lower number.")
        else:
            print(f"Congratulations! You guessed the number in {attempts} attempts.")
            break

        print("To try again, run the script again with a new guess.")
        break  # Exit after one guess since this is per-run guess

if __name__ == "__main__":
    number_guessing_game()