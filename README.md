# Asteroids Game

## Overview
This project is a simple implementation of the classic **Asteroids** game using the **Pygame** library. The game involves controlling a spaceship (player) to avoid and shoot asteroids. The player scores points by destroying asteroids, which split into smaller ones upon collision. The game ends when the player collides with an asteroid.

---

## Features
- **Player-controlled spaceship**: Move and shoot to destroy asteroids.
- **Asteroids**: Asteroids split into smaller pieces upon being hit by a shot.
- **Asteroid Field**: Automatically generates an initial set of asteroids.
- **Collision Detection**: Realistic collisions between the player, shots, and asteroids.
- **Game Over Condition**: The game ends when the player collides with an asteroid.
- **Smooth Gameplay**: Frame rate capped at 60 FPS for a smooth experience.

---

## Setup Instructions

### Prerequisites
- Python 3.8 or higher
- **Pygame** library

### Installation
1. Clone or download the repository to your local machine.
2. Install the required library:
   ```bash
   pip install pygame
   ```
3. Ensure the following files are present in the same directory as `main.py`:
   - `constants.py`: Defines game constants such as screen dimensions, player radius, etc.
   - `circleshape.py`: Base class for circular game objects (e.g., player, asteroid).
   - `player.py`: Contains the `Player` class for player control and behavior.
   - `asteroid.py`: Contains the `Asteroid` class for asteroid behavior and splitting.
   - `asteroidfield.py`: Manages the creation and management of multiple asteroids.
   - `shot.py`: Contains the `Shot` class for projectiles fired by the player.

### Run the Game
1. Open a terminal in the project directory.
2. Run the game with:
   ```bash
   python main.py
   ```

---

## Gameplay Instructions

### Objective
Survive as long as possible by avoiding and destroying asteroids.

### Controls
Controls (e.g., movement and shooting) are defined in the `Player` class. Check or update `player.py` for specific keybindings.

### Rules
- The game ends when the player collides with an asteroid.
- Shots fired by the player destroy asteroids. Destroyed asteroids split into smaller pieces until they reach their smallest size.

---

## Code Overview

### Key Components
- **Main Game Loop**  
  Handles user input, updates game objects, detects collisions, and renders the game screen.
- **Game Objects**  
  - **Player**: Represents the player's spaceship.  
  - **Asteroid**: Represents the asteroids in the game; splits into smaller pieces when shot.  
  - **Shot**: Represents projectiles fired by the player.  
  - **AsteroidField**: Automatically generates and manages multiple asteroids.

### Object Containers
- **Updatable**: Game objects that need to update their state each frame.
- **Drawable**: Game objects that need to be rendered on the screen.
- **Shots**: Group of projectiles fired by the player.
- **Asteroids**: Group of asteroids in the game.
- **AsteroidField**: Manages the initial and ongoing creation of asteroids.

### Collision Detection
Checks for:
1. Collisions between asteroids and shots.
2. Collisions between asteroids and the player.

---

## Customization
- **Game Constants**: Modify values in `constants.py` to adjust screen size, player speed, asteroid size, etc.
- **Asteroid Behavior**: Adjust asteroid splitting logic or starting positions in `asteroid.py` and `asteroidfield.py`.
- **Player Controls**: Customize movement and shooting in `player.py`.

---

## Known Issues & Limitations
- Currently, the game has no scoring system or level progression.
- No main menu or pause functionality.
- Collision handling does not include advanced physics (e.g., bouncing off walls or each other).

---

## Future Enhancements
- Add a scoring system.
- Implement levels with increasing difficulty.
- Add player lives or shields.
- Include sound effects and background music.
- Develop a main menu and pause functionality.

---

## Credits
Developed with the **Pygame** library for building 2D games in Python.

Enjoy playing Asteroids! 🚀
