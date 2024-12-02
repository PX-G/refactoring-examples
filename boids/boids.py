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
