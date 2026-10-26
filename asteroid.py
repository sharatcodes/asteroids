import pygame
from circleshape import CircleShape

class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)

    def draw(self, screen: pygame.Surface) -> None:
        color = "white"
        position = self.position
        radius = self.radius
        pygame.draw.circle(screen, color, position, radius)

    def update(self, dt: float) -> None:
        self.position += (self.velocity * dt)
