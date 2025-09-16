# 🎯 Mastermind Game

A Python implementation of the classic code-breaking game Mastermind. Test your logic and deduction skills by trying to guess the secret color code!

## 🎮 Game Overview

Mastermind is a code-breaking game where players attempt to guess a secret sequence of colors. After each guess, you receive feedback about how many colors are in the correct position and how many correct colors are in the wrong positions.

### Game Rules
- The secret code consists of 4 colors
- Available colors: **R**ed, **G**reen, **B**lue, **Y**ellow, **W**hite, **O**range
- You have 10 attempts to guess the code
- After each guess, you'll receive feedback:
  - **Correct positions**: Colors that are in the right spot
  - **Incorrect positions**: Right colors but in wrong spots

## 🚀 Features

- Clean, modular code architecture
- Input validation and error handling
- Configurable game parameters
- Clear feedback system
- Professional project structure

## 📁 Project Structure

```
mastermind-game/
├── main.py              # Main game controller and entry point
├── config.py            # Game configuration and constants
├── game_logic.py        # Core game mechanics and algorithms
├── user_interface.py    # User input/output handling
└── README.md           # Project documentation
```

## 🛠️ Installation & Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/mastermind-game.git
   cd mastermind-game
   ```

2. **Run the game**
   ```bash
   python main.py
   ```

No additional dependencies required - uses only Python standard library!

## 🎯 How to Play

1. Run the game using `python main.py`
2. Enter your guess as 4 colors separated by spaces (e.g., `R G B Y`)
3. Analyze the feedback:
   - **Correct positions**: Colors in the right spot
   - **Incorrect positions**: Right colors in wrong spots
4. Use the feedback to refine your next guess
5. Win by guessing all colors in correct positions!

### Example Gameplay
```
Welcome to Mastermind, you have 10 tries to guess the code...
The valid colors are R G B Y W O
Guess: R G B Y
Correct positions: 1 | Incorrect positions: 2
Guess: R W O B
Correct positions: 2 | Incorrect positions: 1
...
```

## ⚙️ Configuration

Easily customize the game by modifying `config.py`:

```python
COLORS = ["R", "G", "B", "Y", "W", "O"]  # Available colors
TRIES = 10                               # Number of attempts
CODE_LENGTH = 4                          # Length of secret code
```

## 🏗️ Architecture

The project follows clean code principles with separation of concerns:

- **`config.py`**: Centralized configuration management
- **`game_logic.py`**: Pure functions for game mechanics
- **`user_interface.py`**: User interaction and display logic  
- **`main.py`**: Game orchestration and main loop

This modular design makes the code:
- Easy to test and maintain
- Simple to extend with new features
- Clear in its responsibilities

## 🎓 Learning Outcomes

This project demonstrates:
- **Clean Code Architecture**: Modular design with separation of concerns
- **Algorithm Implementation**: Efficient code checking logic
- **Input Validation**: Robust user input handling
- **Python Best Practices**: PEP 8 compliance, proper documentation
- **Game Development**: Logic flow and state management

## 🚀 Future Enhancements

Potential improvements for future versions:
- [ ] GUI interface using tkinter or pygame
- [ ] Difficulty levels (different code lengths)
- [ ] Multiplayer support
- [ ] Score tracking and statistics
- [ ] Timer-based challenges
- [ ] Color-blind friendly mode

## 🤝 Contributing

Feel free to fork this project and submit pull requests for any improvements!

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

---

**Built with Python 🐍 | Part of my AI Engineering Portfolio**