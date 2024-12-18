import pygame

class CircleShape(pygame.sprite.Sprite):
    """
    Base class for circular game objects. Inherits from pygame.sprite.Sprite
    and provides basic functionality for position, velocity, drawing, updating,
    and collision checking.
    """

    def __init__(self, x, y, radius):
        """
        Initializes a CircleShape object.

        Args:
            x (float): The x-coordinate of the object's starting position.
            y (float): The y-coordinate of the object's starting position.
            radius (float): The radius of the circular object.
        """
        if hasattr(self, "containers"):
            super().__init__(self.containers)  # Add to sprite groups if containers are defined
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)  # Position vector
        self.velocity = pygame.Vector2(0, 0)  # Velocity vector
        self.radius = radius  # Radius of the circle

    def draw(self, screen):
        """
        Draws the object on the given screen. This method should be overridden by subclasses.

        Args:
            screen (pygame.Surface): The screen to draw the object on.
        """
        pass  # To be implemented by subclasses

    def update(self, dt):
        """
        Updates the object's state. This method should be overridden by subclasses.

        Args:
            dt (float): Delta time for smooth updates.
        """
        pass  # To be implemented by subclasses

    def collision_check(self, target):
        """
        Checks for a collision with another circular object.

        Args:
            target (CircleShape): The other object to check collision with.

        Returns:
            bool: True if this object collides with the target, False otherwise.
        """
        obj_distance = target.position.distance_to(self.position)
        return obj_distance <= self.radius + target.radius
