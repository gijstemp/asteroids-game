import pygame
from circleshape import CircleShape
from shot import Shot
from constants import *

class Player(CircleShape):
    """
    The Player class represents the player's ship in the game, inheriting from the CircleShape class.
    It manages the player's position, rotation, movement, shooting, and drawing the ship on the screen.
    """

    def __init__(self, x, y, radius):
        """
        Initializes the Player object.

        Args:
            x (float): The x-coordinate of the player's starting position.
            y (float): The y-coordinate of the player's starting position.
            radius (float): The radius of the player's ship.
        """
        super().__init__(x, y, radius)
        self.rotation = 0  # Rotation angle in degrees
        self.cooldown_timer = 0  # Cooldown timer for shooting

    def triangle(self):
        """
        Calculates the vertices of the triangular representation of the player's ship.

        Returns:
            list: A list of three pygame.Vector2 points representing the triangle's vertices.
        """
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):
        """
        Draws the player's ship as a triangle on the given screen.

        Args:
            screen (pygame.Surface): The screen to draw the ship on.
        """
        pygame.draw.polygon(screen, "white", self.triangle(), 2)

    def rotate(self, dt):
        """
        Rotates the player's ship.

        Args:
            dt (float): Delta time for smooth rotation.
        """
        self.rotation += PLAYER_TURN_SPEED * dt

    def move(self, dt):
        """
        Moves the player's ship forward or backward.

        Args:
            dt (float): Delta time for smooth movement.
        """
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def shoot(self):
        """
        Shoots a projectile (Shot) from the player's position if not on cooldown.
        """
        if self.cooldown_timer == 0:
            shot = Shot(self.position.x, self.position.y, SHOT_RADIUS)
            shot.velocity = shot.velocity.rotate(self.rotation) 
            shot.velocity *= PLAYER_SHOOT_SPEED
            self.cooldown_timer = PLAYER_SHOOT_COOLDOWN

    def update(self, dt):
        """
        Updates the player's state, including cooldown timer, movement, rotation, and shooting.

        Args:
            dt (float): Delta time for smooth updates.
        """
        if self.cooldown_timer > 0:
            self.cooldown_timer = max(self.cooldown_timer - dt, 0)

        keys = pygame.key.get_pressed()

        # Handle rotation
        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)

        # Handle movement
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)

        # Handle shooting
        if keys[pygame.K_SPACE]:
            self.shoot()
