import pygame
import random
from constants import *
from circleshape import CircleShape

class Asteroid(CircleShape):
    """
    Represents an asteroid in the game. Handles drawing, updating, and splitting into smaller asteroids.
    Inherits from the CircleShape class.
    """

    def __init__(self, x, y, radius):
        """
        Initializes an Asteroid object.

        Args:
            x (float): The x-coordinate of the asteroid's starting position.
            y (float): The y-coordinate of the asteroid's starting position.
            radius (float): The radius of the asteroid.
        """
        super().__init__(x, y, radius)

    def draw(self, screen):
        """
        Draws the asteroid as a blue circle on the given screen.

        Args:
            screen (pygame.Surface): The screen to draw the asteroid on.
        """
        pygame.draw.circle(screen, "blue", self.position, self.radius, width=2)

    def update(self, dt):
        """
        Updates the asteroid's position based on its velocity.

        Args:
            dt (float): Delta time for smooth movement.
        """
        self.position += self.velocity * dt

    def split(self):
        """
        Splits the asteroid into two smaller asteroids if its radius is greater than the minimum size.
        Removes the current asteroid from the game.
        """
        self.kill()  # Remove the current asteroid

        if self.radius <= ASTEROID_MIN_RADIUS:
            return  # Do not split if the asteroid is too small

        # Calculate random angle for splitting
        random_angle = random.uniform(20, 50)
        vector_1 = self.velocity.rotate(random_angle)  # Velocity vector for first new asteroid
        vector_2 = self.velocity.rotate(-random_angle)  # Velocity vector for second new asteroid

        # Calculate the radius for the new smaller asteroids
        new_radius = self.radius - ASTEROID_MIN_RADIUS

        # Create the first smaller asteroid
        asteroid_1 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid_1.velocity = vector_1 * 1.2  # Increase velocity slightly for variation

        # Create the second smaller asteroid
        asteroid_2 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid_2.velocity = vector_2 * 1.2  # Increase velocity slightly for variation
