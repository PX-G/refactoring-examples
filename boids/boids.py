"""
A deliberately bad implementation of 
[Boids](http://dl.acm.org/citation.cfm?doid=37401.37406)
for use as an exercise on refactoring.
This code simulates the swarming behaviour of bird-like objects ("boids").
"""
import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation

import random

# Constants with default parameters
NUM_BOIDS = 50
WIDTH, HEIGHT = 500, 600
NEARBY_RADIUS = 100
ALIGN_RADIUS = 100
COHESION_FACTOR = 0.01
SEPARATION_FACTOR = 1.0
ALIGNMENT_FACTOR = 0.125

class Boid:
    """Class representing a single boid in the flock.

    Attributes:
        x (float): The x-coordinate of the boid.
        y (float): The y-coordinate of the boid.
        vx (float): The velocity of the boid in the x-direction.
        vy (float): The velocity of the boid in the y-direction.
    """
    
    def __init__(self, x, y, vx, vy):
        """Initialize a boid with position and velocity.

        Args:
            x (float): Initial x-coordinate of the boid.
            y (float): Initial y-coordinate of the boid.
            vx (float): Initial velocity in the x-direction.
            vy (float): Initial velocity in the y-direction.
        """
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy

    def update(self):
        """Update the boid's position based on its current velocity."""
        self.x += self.vx
        self.y += self.vy

def create_boids(num_boids):
    """Create a list of boids with random starting positions and velocities.

    Args:
        num_boids (int): The number of boids to create.

    Returns:
        list: A list of Boid objects.
    """
    return [Boid(np.random.uniform(-450, 50.0), 
                 np.random.uniform(300.0, 600.0),
                 np.random.uniform(0, 10.0), 
                 np.random.uniform(-20.0, 20.0))
            for _ in range(num_boids)]

def apply_cohesion(boids, boid):
    """Adjust the boid's velocity towards the average position of nearby boids.

    Args:
        boids (list): A list of all boids in the simulation.
        boid (Boid): The current boid being adjusted.
    """
    center_x = np.mean([b.x for b in boids])
    center_y = np.mean([b.y for b in boids])
    boid.vx += (center_x - boid.x) * COHESION_FACTOR
    boid.vy += (center_y - boid.y) * COHESION_FACTOR

def apply_separation(boids, boid):
    """Adjust the boid's velocity to avoid crowding nearby boids.

    This behavior prevents boids from getting too close to one another.

    Args:
        boids (list of Boid): The list of all boids in the simulation.
        boid (Boid): The boid to be adjusted.
    """
    for other in boids:
        if boid is not other and (boid.x - other.x) ** 2 + (boid.y - other.y) ** 2 < NEARBY_RADIUS ** 2:
            boid.vx += (boid.x - other.x) * SEPARATION_FACTOR
            boid.vy += (boid.y - other.y) * SEPARATION_FACTOR

def apply_alignment(boids, boid):
    """Adjust the boid's velocity to align with nearby boids.

    Args:
        boids (list): A list of all boids in the simulation.
        boid (Boid): The current boid being adjusted.
    """
    nearby_boids = [b for b in boids if b is not boid and 
                    (boid.x - b.x) ** 2 + (boid.y - b.y) ** 2 < ALIGN_RADIUS ** 2]
    
    if nearby_boids:
        avg_vx = np.mean([b.vx for b in nearby_boids])
        avg_vy = np.mean([b.vy for b in nearby_boids])
        boid.vx += (avg_vx - boid.vx) * ALIGNMENT_FACTOR
        boid.vy += (avg_vy - boid.vy) * ALIGNMENT_FACTOR

def update_boids(boids):
    """Update all boids by applying the flocking behaviors and updating positions."""
    for boid in boids:
        apply_cohesion(boids, boid)
        apply_separation(boids, boid)
        apply_alignment(boids, boid)
        boid.update()

if __name__ == "__main__":
    # Initialize the boids and visualization components
    boids = create_boids(NUM_BOIDS)