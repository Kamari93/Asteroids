from circleshape import CircleShape
from constants import LINE_WIDTH
from constants import ASTEROID_MIN_RADIUS
from logger import log_event
import random
import pygame

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen,"white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        if self.radius > ASTEROID_MIN_RADIUS:
            log_event("asteroid_split")
            # Create two smaller asteroids
            random_angle = random.uniform(20, 50)
            first_new_asteroid_movement = self.velocity.rotate(random_angle)
            second_new_asteroid_movement = self.velocity.rotate(-random_angle)
            new_radisus_smaller_asteroid = self.radius - ASTEROID_MIN_RADIUS
            first_asteroid = Asteroid(self.position.x, self.position.y, new_radisus_smaller_asteroid)
            second_asteroid = Asteroid(self.position.x, self.position.y, new_radisus_smaller_asteroid)
            first_asteroid.velocity = first_new_asteroid_movement * 1.2
            second_asteroid.velocity = second_new_asteroid_movement * 1.2
        # super().kill()
        self.kill()