from typing import List
from config import TRIES, CODE_LENGTH
from game_logic import generate_code, check_code
from user_interface import (
    display_welcome,
    get_user_guess,
    display_result,
    display_win,
    display_game_over
)


def play_game() -> None:
    display_welcome()
    code: List[str] = generate_code()
    
    for attempts in range(1, TRIES + 1):
        guess: List[str] = get_user_guess()
        correct_pos: int
        incorrect_pos: int
        correct_pos, incorrect_pos = check_code(guess, code)
        
        if correct_pos == CODE_LENGTH:
            display_win(attempts)
            break
        
        display_result(correct_pos, incorrect_pos)
    else:
        display_game_over(code)


if __name__ == "__main__":
    play_game()