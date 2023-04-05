import math

# Apply gravitacional force on all the particles on the canvas
def apply_gravity(particles, G, dt):

    # Iterate all objects
    for particle in particles:
        # Compare it with the rest of objects
        for another_particle in particles:
            if particle != another_particle:

                # Calculate distance between particles
                dx = another_particle.x - particle.x
                dy = another_particle.y - particle.y
                distance = math.sqrt(dx ** 2 + dy ** 2)

                # Skip if the particles are too close
                if distance < particle.radius:
                    continue

                # Calculate gravitational force
                f_gravity = G * particle.mass * another_particle.mass / distance ** 2

                # Calculate gravitational acceleration
                a_gravity = f_gravity / another_particle.mass

                # Calculate components of gravitational acceleration
                ax = a_gravity * dx / distance
                ay = a_gravity * dy / distance

                # Add gravitational acceleration to total acceleration
                particle.acceleration[0] += ax
                particle.acceleration[1] += ay

        # Update velocity based on acceleration and time step
        particle.velocity[0] += particle.acceleration[0] * dt
        particle.velocity[1] += particle.acceleration[1] * dt

        # Update position based on velocity and time step
        particle.update_position(dt)

        # Reset acceleration to zero for next time step
        particle.acceleration = [0, 0]