import pygame
import sys
from constants import *
from circleshape import CircleShape
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    """
    Main function to initialize and run the Asteroids game.

    Initializes the game screen, sets up game objects (player, shots, asteroids),
    and manages the game loop for updating and rendering game elements.
    """
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    
    # Initialize Pygame and create a game screen
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    # Groups to manage game objects
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    asteroidfield = pygame.sprite.Group()
    
    # Set up player
    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, PLAYER_RADIUS)
    
    # Set up shots
    Shot.containers = (shots, updatable, drawable)
    
    # Set up asteroids
    Asteroid.containers = (asteroids, updatable, drawable)
    
    # Set up asteroid field
    AsteroidField.containers = (updatable)
    AsteroidField()
    
    # Initialize clock for managing frame rate
    clock = pygame.time.Clock()
    dt = 0 # Delta time for smooth movement
    
    
    
    while True:
        # Event handling loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return  # Exit the game

        # Clear the screen
        screen.fill("black")

        # Update game objects
        for obj in updatable:
            obj.update(dt)

        # Check collisions between asteroids and shots
        for asteroid in asteroids:
            for shot in shots:
                if asteroid.collision_check(shot):
                    asteroid.split()  # Split the asteroid
                    shot.kill()       # Remove the shot

            # Check collision between asteroids and player
            if asteroid.collision_check(player):
                sys.exit("Game over!")

        # Draw game objects
        for obj in drawable:
            obj.draw(screen)

        # Update the display
        pygame.display.flip()

        # Cap the frame rate to 60 FPS
        dt = clock.tick(60) / 1000  # Delta time in seconds

# Entry point for the game
if __name__ == "__main__":
    main()