import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Set screen dimensions
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 400


# Function to generate a random color
def random_color():
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))


# Create the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Color Changing Screen")

# Clock to control frame rate
clock = pygame.time.Clock()

# Variable to keep track of color changing
color_timer = 0
transition_duration = 2000  # 2 seconds

# Initial color
current_color = random_color()
screen.fill(current_color)

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Increment color timer
    color_timer += clock.get_time()

    # Change color gradually
    if color_timer >= transition_duration:
        color_timer = 0
        current_color = random_color()

    # Calculate transition progress
    transition_progress = min(color_timer / transition_duration, 1.0)

    # Interpolate between current and new color
    new_color = [int(current_color[i] * (1 - transition_progress) + current_color[i] * transition_progress) for i in range(3)]

    # Fill screen with new color
    screen.fill(new_color)

    # Update the display
    pygame.display.flip()

    # Limit frame rate
    clock.tick(60)

pygame.quit()
sys.exit()
