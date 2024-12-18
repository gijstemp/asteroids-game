import pygame
from circleshape import CircleShape

class Shot(CircleShape):
    """
    The Shot class represents a projectile fired by the player or other entities in the game.
    It inherits from the CircleShape class and handles movement and rendering of the projectile.
    """

    def __init__(self, x, y, radius):
        """
        Initializes a Shot object.

        Args:
            x (float): The x-coordinate of the shot's starting position.
            y (float): The y-coordinate of the shot's starting position.
            radius (float): The radius of the shot.
        """
        super().__init__(x, y, radius)
        self.velocity = pygame.Vector2(0, 1)  # Initial velocity of the shot
        self.rotation = 0  # Rotation angle of the shot

    def draw(self, screen):
        """
        Draws the shot as a circle on the given screen.

        Args:
            screen (pygame.Surface): The screen to draw the shot on.
        """
        pygame.draw.circle(screen, "red", self.position, self.radius, width=2)

    def update(self, dt):
        """
        Updates the shot's position based on its velocity.

        Args:
            dt (float): Delta time for smooth movement.
        """
        self.position += self.velocity * dt
