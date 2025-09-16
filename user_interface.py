from config import COLORS, CODE_LENGTH, TRIES


def display_welcome():
    print(f"Welcome to Mastermind, you have {TRIES} tries to guess the code...")
    print("The valid colors are", *COLORS)


def get_user_guess():
    while True:
        guess = input("Guess: ").upper().split(" ")

        if len(guess) != CODE_LENGTH:
            print(f"You must guess {CODE_LENGTH} colors.")
            continue

        for color in guess:
            if color not in COLORS:
                print(f"Invalid color: {color}. Try again.")
                break
        else:
            break

    return guess


def display_result(correct_pos, incorrect_pos):
    print(f"Correct positions: {correct_pos} | Incorrect positions: {incorrect_pos}")


def display_win(attempts):
    print(f"You guessed the code in {attempts} tries!")


def display_game_over(code):
    print(f"You've used all your tries. The code was:", *code)