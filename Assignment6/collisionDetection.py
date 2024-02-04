# ASSIGNMENT 2 & 3
import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the screen
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Collision Detection - Color Change")

# Load sound file
collision_sound = pygame.mixer.Sound('collision.mp3')

# Define circle properties
circle1_pos = (100, 300)
circle1_radius = 50
circle1_color = (255, 0, 0)
circle1_velocity = [0.5, 0]

circle2_pos = (700, 300)
circle2_radius = 50
circle2_color = (0, 255, 0)
circle2_velocity = [-0.5, 0]


# Collision detection toggle button properties
button_rect = pygame.Rect(350, 100, 125, 54)
button_color = (255, 255, 0)
# Track collision detection state
collision_active = False

# Game Loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Check if the mouse click is within the button rectangle
            if button_rect.collidepoint(event.pos):
                collision_active = not collision_active  # Toggle collision detection state

    # Game Logic
    if collision_active:
        # Update circle positions based on velocity
        circle1_pos = (circle1_pos[0] + circle1_velocity[0], circle1_pos[1] + circle1_velocity[1])
        circle2_pos = (circle2_pos[0] + circle2_velocity[0], circle2_pos[1] + circle2_velocity[1])

        # Collision detection
        distance = ((circle1_pos[0] - circle2_pos[0]) ** 2 + (circle1_pos[1] - circle2_pos[1]) ** 2) ** 0.5
        if distance < circle1_radius + circle2_radius:
            # Change color of circle 1 & 2 when collision occurs
            circle1_color = (255, 165, 0)
            circle2_color = (255, 165, 0)
            # Play collision sound
            collision_sound.play()

        # Check boundaries and reset circle positions
        if circle1_pos[0] > 800 + circle1_radius:
            # Reset circle 1 position and color
            circle1_pos = (-circle1_radius, 300)
            circle1_color = (255, 0, 0)
        if circle2_pos[0] < -circle2_radius:
            # Reset circle 2 position & color
            circle2_pos = (800 + circle2_radius, 300)
            circle2_color = (0, 255, 0)

    # Fill screen with black
    screen.fill((0, 0, 0))

    # Display collision detection toggle button
    pygame.draw.rect(screen, button_color, button_rect)
    button_text = "STOP" if collision_active else "START"
    font = pygame.font.SysFont( 'Arial' , 34)
    text = font.render(button_text, True, (0, 0, 0))
    screen.blit(text, (370, 110))

    # Draw game elements
    pygame.draw.circle(screen, circle1_color, circle1_pos, circle1_radius)
    pygame.draw.circle(screen, circle2_color, circle2_pos, circle2_radius)

    # Rendering
    pygame.display.update()


pygame.quit()
sys.exit()
