import random

def number_guessing_game():
    # Set the range for the random number
    min_num = 1
    max_num = 100

    # Generate a random number
    random_number = random.randint(min_num, max_num)

    # Number of attempts
    attempts = 0
    max_attempts = 10

    print(f"Welcome to the Number Guessing Game!")
    print(f"Guess the number between {min_num} and {max_num}. You have {max_attempts} attempts.")

    # Game loop
    while attempts < max_attempts:
        try:
            guess = int(input("Enter your guess: "))
        except ValueError:
            print("Invalid input! Please enter a number.")
            continue
        
        attempts += 1

        if guess < random_number:
            print("Too low!")
        elif guess > random_number:
            print("Too high!")
        else:
            print(f"Congratulations! You guessed the correct number {random_number} in {attempts} attempts.")
            break

        print(f"Attempts remaining: {max_attempts - attempts}")

    if attempts == max_attempts:
        print(f"Sorry! You've used all {max_attempts} attempts. The correct number was {random_number}.")

    # Ask if the user wants to play again
    play_again = input("Do you want to play again? (yes/no): ").strip().lower()
    if play_again == 'yes':
        number_guessing_game()
    else:
        print("Thank you for playing! Goodbye.")

if __name__ == "__main__":
    number_guessing_game()
