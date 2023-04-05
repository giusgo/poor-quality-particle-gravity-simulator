# PyGame library
import pygame
import math

# Particle class
class Particle:
    # Constructor
    def __init__(self, x, y, mass, color, scale, trail, velocity = [0, 0]):
        self.x = x
        self.y = y
        self.mass = mass
        self.color = color
        self.velocity = velocity
        self.acceleration = [0, 0]
        self.radius = int(10 * mass ** (1/3) / scale)  # adjust radius based on mass
        self.active_trail = trail
        self.trail = []


    # Method to draw the particle
    def draw(self, screen):
        # If the trail is active, draw it
        if self.active_trail == True and len(self.trail) >= 2:
            pygame.draw.lines(screen, self.color, False, self.trail, 3)

        # Draw the particle
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.radius)

    # Method to get mass and velocity of the particle
    def get_info(self):
        vel_magnitude = math.sqrt(self.velocity[0]**2 + self.velocity[1]**2)
        return f"Mass: {round(self.mass, 3)}   Speed: {round(vel_magnitude, 3)}"
    
    # Method to update particle position
    def update_position(self, dt):
        self.x += self.velocity[0] * dt
        self.y += self.velocity[1] * dt

        if self.active_trail == True:
            # Add current position to trail
            self.trail.append((self.x, self.y))
            
            # Remove oldest trail position if list is too long
            if len(self.trail) > 50:
                self.trail.pop(0)