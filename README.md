# The_Jungle_Game

https://github.com/user-attachments/assets/a2ddbc77-e30d-435c-93e4-3d2499c864a9

## Description:
Jungle Chess is a two-player strategy board game implemented using Pygame. The game features two players (red and blue). The objective is to move one of your pieces to the opponent's den.

## Installation:
1. Ensure you have Python installed on your system.
2. Install Pygame library if you haven't already:
    ```bash
    pip install pygame
    ```
3. Clone or download this repository.

## Usage:
1. Navigate to the directory where the script is located.
2. Run the script:
    ```bash
    python The_Jungle_Game.py
    ```

## How to Play:

### Game Setup:
- The game board is 7 columns by 10 rows.
- Red and Blue teams have the following animals: Elephant, Lion, Tiger, Leopard, Wolf, Dog, Cat, Mouse.
- The strength of an animal is sorted as follows from strongest to weakest: Elephant, Lion, Tiger, Leopard, Wolf, Dog, Cat, Mouse. For example, Cat can defeat Mouse, Dog can defeat both Cat and Mouse, and so on. But only Elephant can defeat everyone except Mouse and Mouse can only defeat Elephant.
- In order to defeat an opponent's animal, you have to be 1 square near the target and use your turn to move to the square of your target (only up, down, right, and left).
- Initial positions for Red and Blue teams are predefined on the board.

### Game Rules:


1. **Turns**:
    - Red team starts the game.
    - Turns alternate between the Red and Blue teams.
2. **Movement**:
    - Click on an animal to select it.
    - Click on a valid destination to move the selected animal which is 1 square up, 1 square down, 1 square right or 1 square left.
3. **Winning the Game**:
    - Move one of your animal to the opponent's den located at (3,0) for Red and (3,8) for Blue to win.

### Board Elements:
- **Protected Cave (6 Gray Squares)**: If your animal enters one of the Protected Caves, that animal is protected, and your opponent cannot defeat it even if they have a stronger animal 1 square near you.
- **Den (Red Squares)**: If any animal reaches the opponent's den, then they win.
- **River (12 Blue Squares)**: Only Wolf,Dog and Mouse can access this area.
