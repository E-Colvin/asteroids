import pygame
import random
from logger import log_event
from circleshape import CircleShape
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS, ASTEROID_MAX_RADIUS

class Asteroid(CircleShape):
    def __init__(self,x ,y ,radius):
        super().__init__(x,y,radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white",self.position,self.radius,LINE_WIDTH)

    def update(self, dt):
        self.position += self.velocity*dt

    def split(self):
        self.kill()
        if self.radius < ASTEROID_MIN_RADIUS:
            return
        else:
            log_event("asteroid_split")
            angle = random.uniform(20,50)
            child_1 = self.spawn_child(angle)
            child_2 = self.spawn_child(-angle)

    def spawn_child(self,angle):
        child_velocity = self.velocity.rotate(angle)
        child_radius = self.radius - ASTEROID_MIN_RADIUS
        child = Asteroid(self.position[0],self.position[1],child_radius)
        child.velocity = child_velocity*1.2
            