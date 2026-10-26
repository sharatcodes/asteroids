import pygame
from circleshape import CircleShape
from constants import SHOT_RADIUS

class Shot(CircleShape):
    def __init__(self, x: float, y: float, radius: float = SHOT_RADIUS) -> None:
        super().__init__(x, y, radius)

    def draw(self, screen: pygame.Surface) -> None:
        color = "white"
        position = self.position
        radius = self.radius
        pygame.draw.circle(screen, color, position, radius)

    def update(self, dt: float) -> None:
        self.position += (self.velocity * dt)

