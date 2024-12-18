import pygame
from circleshape import CircleShape

class Shot(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.velocity = pygame.Vector2(0, 1)
        self.rotation = 0
        
    def draw(self, screen):
        pygame.draw.circle(screen, "red", self.position, self.radius, width=2)
        
    def update(self, dt):
        self.position += self.velocity * dt