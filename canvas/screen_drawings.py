# PyGame library
import pygame
import math

# Keep on record the screen divisions
screen_divisions = {
    'num_cols': 0,
    'num_rows': 0,
    'block_width': 0,
    'block_height': 0
}

# Precalculate the grid dimensions
def pre_calc_grid(scale, screen_width, screen_height):

    # Proportional screen (16:9 aspect ratio)
    screen_divisions['num_cols'], screen_divisions['num_rows'] = 16 * scale, 9 * scale

    # Define the width and heigth of the blocks, which have equal size
    screen_divisions['block_width'] = screen_width // screen_divisions['num_cols']
    screen_divisions['block_height'] = screen_height // screen_divisions['num_rows']


# Draw the grid on the screen
def draw_grid(screen, colors):

    # Draw the grid
    for row in range(screen_divisions['num_rows']):
        for col in range(screen_divisions['num_cols']):
            block_rect = pygame.Rect(col * screen_divisions['block_width'], row * screen_divisions['block_height'], screen_divisions['block_width'], screen_divisions['block_height'])
            pygame.draw.rect(screen, colors['WHITE'], block_rect, 1)


# Show status indicator
def show_status(font, clock, screen, width, height, scale, particles):

    # Get the information to show
    # --- FPS
    fps = round(clock.get_fps())

    # Build the status text
    status_text = f"FPS: {fps} | RESOLUTION: {width}x{height} | SCALE: x{scale} | PARTICLES: {len(particles)}"
    status_ind = font.render(status_text, True, pygame.Color('white'))

    # Get size of the text
    text_rect = status_ind.get_rect()

    # Calculate dimensiones of the box that will contain the status ind.
    padding = 10
    box_width = text_rect.width + padding * 2
    box_height = text_rect.height + padding * 2

    # Create the box
    box_surface = pygame.Surface((box_width, box_height))
    box_surface.fill((0, 0, 0)) # Black box
    box_surface.set_alpha(204) # Set half transparency

    # Put the status ind. inside the box
    text_rect.center = (box_width // 2, box_height // 2)
    box_surface.blit(status_ind, text_rect)

    # Display it on the screen
    screen.blit(status_ind, (10, 10))


# Show info about the particle
def show_particle_info(screen, font, mouse_pos, particles):

    # Iterate each particle
    for particle in particles:

        # Distance of the mouse from the center of the particle.
        distance = math.sqrt((mouse_pos[0] - particle.x)**2 + (mouse_pos[1] - particle.y)**2)

        # Detect if the mouse is inside the particle
        if distance <= particle.radius:

            # Get the text info about the particle
            text = font.render(particle.get_info(), True, (255, 255, 255))

            # Size of the text
            text_rect = text.get_rect()

            # Center the box on the center of the particle
            text_rect.center = (particle.x, particle.y - 20)

            # Calculate the size of the outer rectangle
            outer_rect_size = (text_rect.width + 10, text_rect.height + 10)

            # Create the outer rectangle surface
            outer_rect_surface = pygame.Surface(outer_rect_size)

            # Draw the white border
            pygame.draw.rect(outer_rect_surface, (255, 255, 255), outer_rect_surface.get_rect(), 1)

            # Draw the black fill
            pygame.draw.rect(outer_rect_surface, (0, 0, 0), outer_rect_surface.get_rect().inflate(-6, -6))

            # Draw the inner text box onto the outer rectangle
            outer_rect_surface.blit(text, (5, 5))

            # Draw the outer rectangle onto the screen
            screen.blit(outer_rect_surface, text_rect.move(-5, -5))