import random
from newton.particle import Particle

# Spawn the particles on the screen
def spawn_random_particles(num_particles, width, height, min_mass, max_mass, colors, scale, trail):

    # Generated particles
    particles = []

    # Margin of the screen
    margin = 20

    # Area of the screen to be used
    width = width - margin * 2
    height = height - margin * 2

    # Create particles
    for i in range(num_particles):

        # Random location for a particle
        x = random.uniform(margin, width)
        y = random.uniform(margin, height)

        # Random mass
        mass = random.uniform(min_mass, max_mass)

        # Color
        color = random.choice(colors['PARTICLE_COLORS'])

        # Generate 1 particle
        particle = Particle(x, y, mass, color, scale, trail)

        particles.append(particle)

    print(Particle.__dict__)
        
    return particles


# Despawn particles that disappear from the screen
def despawn_particles(particles, width, height):

    margin = 20

    # Iterate through all particles and eliminate those that disappear from the screen
    for particle in particles:
        if (particle.x < -margin or particle.x > width + margin or
            particle.y < -margin or particle.y > height + margin):
            particles.remove(particle)
