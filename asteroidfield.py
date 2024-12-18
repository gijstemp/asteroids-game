import pygame
import random
from asteroid import Asteroid
from constants import *

class AsteroidField(pygame.sprite.Sprite):
    """
    Represents a field of asteroids that spawn at the edges of the screen and move in random directions.
    Handles asteroid spawning, updating, and velocity adjustments.
    """

    # Defines the edges of the screen and corresponding spawn logic
    edges = [
        [
            pygame.Vector2(1, 0),  # Rightward velocity
            lambda y: pygame.Vector2(-ASTEROID_MAX_RADIUS, y * SCREEN_HEIGHT),  # Left edge spawn
        ],
        [
            pygame.Vector2(-1, 0),  # Leftward velocity
            lambda y: pygame.Vector2(
                SCREEN_WIDTH + ASTEROID_MAX_RADIUS, y * SCREEN_HEIGHT  # Right edge spawn
            ),
        ],
        [
            pygame.Vector2(0, 1),  # Downward velocity
            lambda x: pygame.Vector2(x * SCREEN_WIDTH, -ASTEROID_MAX_RADIUS),  # Top edge spawn
        ],
        [
            pygame.Vector2(0, -1),  # Upward velocity
            lambda x: pygame.Vector2(
                x * SCREEN_WIDTH, SCREEN_HEIGHT + ASTEROID_MAX_RADIUS  # Bottom edge spawn
            ),
        ],
    ]

    def __init__(self):
        """
        Initializes the AsteroidField object.
        """
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.spawn_timer = 0.0  # Timer to control asteroid spawn rate

    def spawn(self, radius, position, velocity):
        """
        Spawns a new asteroid at the given position with the specified radius and velocity.

        Args:
            radius (float): Radius of the asteroid.
            position (pygame.Vector2): Initial position of the asteroid.
            velocity (pygame.Vector2): Velocity vector of the asteroid.
        """
        asteroid = Asteroid(position.x, position.y, radius)
        asteroid.velocity = velocity

    def update(self, dt):
        """
        Updates the asteroid field, spawning new asteroids based on a timer.

        Args:
            dt (float): Delta time for smooth updates.
        """
        self.spawn_timer += dt
        if self.spawn_timer > ASTEROID_SPAWN_RATE:
            self.spawn_timer = 0

            # Select a random edge to spawn an asteroid
            edge = random.choice(self.edges)
            speed = random.randint(40, 100)  # Random speed for the asteroid

            # Calculate velocity and position for the new asteroid
            velocity = edge[0] * speed
            velocity = velocity.rotate(random.randint(-30, 30))  # Add randomness to direction
            position = edge[1](random.uniform(0, 1))

            # Determine asteroid type and size
            kind = random.randint(1, ASTEROID_KINDS)
            self.spawn(ASTEROID_MIN_RADIUS * kind, position, velocity)
