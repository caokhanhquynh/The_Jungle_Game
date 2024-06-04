# The_Jungle_Game

## Description:
Jungle Chess is a two-player strategy board game implemented using Pygame. The game features two teams (red and blue), each controlling different animals with unique movement abilities. The objective is to capture the opponent's den or eliminate all opponent pieces.

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
- Initial positions for Red and Blue teams are predefined on the board.

### Game Rules:
1. **Turns**:
    - Red team starts the game.
    - Turns alternate between the Red and Blue teams.
2. **Movement**:
    - Click on an animal to select it.
    - Click on a valid destination to move the selected animal.
3. **Winning the Game**:
    - Capture the opponent's den located at (3,0) for Red and (3,8) for Blue.
    - Eliminate all opponent's animals.
4. **Animal Movement Abilities**:
    - Each animal has unique movement and capture abilities.

### Board Elements:
- **Protected Cave**: Gray squares [(2,0), (3,1), (4,0) for Red; (2,8), (3,7), (4,8) for Blue]
- **Den**: Red's den at (3,0) and Blue's den at (3,8)
- **Traps**: Red's traps at (2,0), (4,0), and (3,1); Blue's traps at (2,8), (4,8), and (3,7)
