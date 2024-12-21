from circleshape import CircleShape
import pygame
from constants import *
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def update(self,dt):
        self.position += (self.velocity * dt)

    def draw(self,screen):
        pygame.draw.circle(screen,"white",self.position,self.radius,2)
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return 
        
        random_angle = random.uniform(20,50)
        new_asteroid_vector1 = self.velocity.rotate(random_angle)
        new_asteroid_vector2 = self.velocity.rotate(-random_angle)
        
        new_radius = self.radius - ASTEROID_MIN_RADIUS

        new_asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
        new_asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)

        new_asteroid1.velocity = new_asteroid_vector1 * 1.2
        new_asteroid2.velocity = new_asteroid_vector2 * 1.2

