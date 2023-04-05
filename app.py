# Libraries and general config
from config import *



# Function to display the window
def window():
     
    # Initialize the pygame library
    pygame.init()

    # Initialize font
    FONT = pygame.font.Font(FONT_SOURCE, FONT_SIZE)

    # Window title
    DISPLAY.set_caption(WINDOW_TITLE)

    # Size of the screen
    SCREEN = DISPLAY.set_mode((WIDTH, HEIGHT))

    return SCREEN, FONT


# Initial setup for the simulator
def initial_setup():

    # -------------- SCREEN SETUP -------------- #

    # Precalculate the grid divisions just 1 time
    screen_drawings.pre_calc_grid(SCALE, WIDTH, HEIGHT)

    # -------------- PARTICLE SPAWNER -------------- #

    # Generate some particles
    particles = particle_generator.spawn_random_particles(PARTICLES_NUM, WIDTH, HEIGHT, MIN_MASS, MAX_MASS, COLORS, SCALE, TRAILS)

    return particles


# Main loop for the program
def simulation(particles, SCREEN, FONT):

    # Variable to control the main loop
    running = True
    
    # Main loop
    while running:

        # Clean previous screen
        SCREEN.fill((0, 0, 0))


        # -------------- GRID DISPLAY -------------- #

        # Create a grid
        screen_drawings.draw_grid(SCREEN, COLORS)


        # In the file config.py you can find a lot of options to modify
        # It is not recommended to modify anything here.


        # -------------- PARTICLES INTERACTION -------------- #

        # Apply gravity to all particles
        physics.apply_gravity(particles, G, dt)

        # Despawn particles that get too far from the screen
        particle_generator.despawn_particles(particles, WIDTH, HEIGHT)

        # Redraw all of them
        for particle in particles:
            particle.draw(SCREEN)


        # -------------- PARTICLES INFORMATION -------------- #

        # Show status indicator
        screen_drawings.show_status(FONT, CLOCK, SCREEN, WIDTH, HEIGHT, SCALE, particles)

        # Show particle information on mouse hover
        mouse_pos = pygame.mouse.get_pos()
        screen_drawings.show_particle_info(SCREEN, FONT, mouse_pos, particles)


        # -------------- EVENT HANDLING -------------- #

        # event handling, gets all event from the event queue
        for event in pygame.event.get():
            # only do something if the event is of type QUIT
            if event.type == pygame.QUIT:
                # change the value to False, to exit the main loop
                running = False


        # -------------- -------------- -------------- #

        # Update full display
        DISPLAY.flip()

        # Cap FPS
        CLOCK.tick(FPS)



if __name__ == '__main__':

    # Execute the window
    SCREEN, FONT = window()

    # Setup the simulator
    particles = initial_setup()

    # Simulation loop
    simulation(particles, SCREEN, FONT)

