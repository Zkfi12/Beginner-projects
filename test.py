import random

def get_max_number():
    while True:
        max_number_str = input("Enter the max number for the guessing game: ")
        if max_number_str.isdigit():
            max_number = int(max_number_str)
            if max_number > 0:
                return max_number
            else:
                print("Please enter a number greater than 0.")
        else:
            print("Please enter a valid number.")

def play_guessing_game(max_number):
    random_number = random.randint(0, max_number)
    guesses = 0

    while True:
        user_guess = get_user_guess()
        guesses += 1

        if user_guess == random_number:
            print("Congratulations! You guessed the number.")
            print(f"It took you {guesses} tries to figure it out.")
            return

        print("Incorrect. Try again.")

def get_user_guess():
    while True:
        user_input = input("Guess the number: ")
        if user_input.isdigit():
            return int(user_input)
        else:
            print("Please enter a valid number.")

def play_again():
    return input("Do you want to play again? (Press 'p' to play again, or enter to end the program): ").lower() == 'p'

# Main program
while True:
    max_number = get_max_number()
    play_guessing_game(max_number)

    if not play_again():
        break
