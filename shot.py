from circleshape import CircleShape
from constants import SHOT_RADIUS
import pygame


class Shot(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS)

    def draw(self, screen):
       pygame.draw.circle(screen, "green", (self.position.x, self.position.y), self.radius, width=2) 
    
    def update(self, dt):
       self.position.x += self.velocity.x * dt
       self.position.y += self.velocity.y * dt