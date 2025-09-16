import random
from typing import List, Tuple, Dict
from config import COLORS, CODE_LENGTH


def generate_code() -> List[str]:
    code = []
    for _ in range(CODE_LENGTH):
        color = random.choice(COLORS)
        code.append(color)
    return code


def check_code(guess: List[str], real_code: List[str]) -> Tuple[int, int]:
    if len(guess) != len(real_code):
        return 0, 0
    
    correct_pos = 0
    incorrect_pos = 0
    
    real_color_counts: Dict[str, int] = {}
    for color in real_code:
        real_color_counts[color] = real_color_counts.get(color, 0) + 1
    
    guess_color_counts: Dict[str, int] = {}
    
    for i, (guess_color, real_color) in enumerate(zip(guess, real_code)):
        if guess_color == real_color:
            correct_pos += 1
            real_color_counts[guess_color] -= 1
        else:
            guess_color_counts[guess_color] = guess_color_counts.get(guess_color, 0) + 1
    
    for guess_color, count in guess_color_counts.items():
        if guess_color in real_color_counts:
            incorrect_pos += min(count, real_color_counts[guess_color])
    
    return correct_pos, incorrect_pos