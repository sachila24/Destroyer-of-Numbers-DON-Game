# Destroyer of Number (DON) Game

## Overview
Destroyer of Number (DON) is a Python-based text game where the player battles against randomly generated enemies by selecting numbers. The player's goal is to survive 20 rounds by making strategic choices to defeat enemies based on their life score.

## How It Works
- The game starts with the player being assigned a random life score.
- In each round, five random numbers (enemies) are presented to the player.
- The player selects a number to "fight." If the selected number is less than or equal to their life score, they win the round, and their life score increases.
- The game continues until the player either survives 20 rounds or is defeated.

## Features
- Randomly generated life scores and enemies.
- Dynamic difficulty scaling across multiple rounds.
- Game status and results saved to a file for future reference.

## Installation and Setup
1. Clone this repository:
    ```bash
    git clone https://github.com/sachila24/Destroyer-of-Numbers-DON-Game.git
    cd Destroyer-of-Numbers-DON-Game
    ```
2. Run the game:
    ```bash
    python main.py
    ```
    *Optionally, you can provide your player name as an argument:*
    ```bash
    python main.py YourName
    ```

## Usage
- **Start the game:** Run the `main.py` file.
- **Playing the game:** Enter a number to fight the presented enemies.
- **Winning the game:** Survive all 20 rounds by carefully selecting numbers that you can defeat.

## Example
Attempt : 1
Player1's life score is : 30
Enemies: 15 25 35 45 55
Select a number to fight: 25
Player1 killed 25


## File Structure
- **main.py:** The entry point for the game.
- **game.py:** Contains the main game logic, including enemy generation and game status.
- **file_handling.py:** Handles saving the game results to a text file.

## Contributing
Feel free to fork this project, submit issues, or create pull requests to improve the game!

## Author
- **Sachila Dissanayake**
- GitHub: [sachila24](https://github.com/sachila24)
- Email: sathmika7@gmail.com
