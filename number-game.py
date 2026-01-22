import random
def number_guessing_game():
    number = random.randint(1, 100)
    attempts = 0
    print("Welcome to the Number Guessing Game!")
    print(f"I have picked a number between 1 and 100. Try to guess it! {number} ")

    while True:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1
            if guess < number:
                print("Too low! Try again.")
                break
            elif guess > number:
                print("Too high! Try again.")
                break
            else:
                print(f"Congratulations! You guessed the number in {attempts} attempts.")
                break
        except ValueError:
            print("Invalid input. Please enter an integer.")
            break

if __name__ == "__main__":
    number_guessing_game()