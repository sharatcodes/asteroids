import pygame
import random
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS
from logger import log_event

class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)

    def draw(self, screen: pygame.Surface) -> None:
        color = "white"
        position = self.position
        radius = self.radius
        pygame.draw.circle(screen, color, position, radius)

    def split(self) -> None:
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        log_event("asteroid_split")
        rotation = random.uniform(20, 50)
        asteroid_one_vec = self.position.rotate(rotation)
        asteroid_two_vec = self.position.rotate(-rotation)
        radius = self.radius - ASTEROID_MIN_RADIUS

        asteroid_one = Asteroid(self.position.x, self.position.y, radius)
        asteroid_one.velocity = asteroid_one_vec * 1.2
        
        asteroid_two = Asteroid(self.position.x, self.position.y, radius)
        asteroid_two.velocity = asteroid_two_vec * 1.2

    def update(self, dt: float) -> None:
        self.position += (self.velocity * dt)
