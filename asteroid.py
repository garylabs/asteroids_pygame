from circleshape import CircleShape
import pygame
import random

from constants import ASTEROID_MIN_RADIUS


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.velocity = pygame.Vector2(0, 0)
    
    def draw(self, screen):
       pygame.draw.circle(screen, "brown", (self.position.x, self.position.y), self.radius, width=2) 
    
    def update(self, dt):
       self.position.x += self.velocity.x * dt
       self.position.y += self.velocity.y * dt

    def split(self):
        self.kill()
        if self.radius < ASTEROID_MIN_RADIUS:
            return
        else:
            angle = random.uniform(20, 50)
            v1 = self.velocity.rotate(angle)
            v2 = self.velocity.rotate(-angle)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            n1 = Asteroid(self.position.x, self.position.y, new_radius)
            n1.velocity = v1 * 1.2
            n2 = Asteroid(self.position.x, self.position.y, new_radius)
            n2.velocity = v2 * 1.2