# ASSIGNMENT 1
import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Set up the screen
window_size = (800, 600)
screen = pygame.display.set_mode(window_size)
pygame.display.set_caption("Among Us")

# Character setup
character_image = pygame.image.load("amongUs_red.png")
character_size = (150, 150)
character = pygame.transform.scale(character_image, character_size)
character_rect = character.get_rect()
# Set the Character to the center of the screen
character_rect.center = (window_size[0] // 2, window_size[1] // 2)

# Circle properties
circle_radius = 15
circles = []
max_circles = 10

# Score
score = 0
font = pygame.font.Font(None, 36)


# Function to create circle at different positions on the screen
def create_circle():
    x = random.randint(0, window_size[0])
    y = random.randint(0, window_size[1])
    # random colors of the circle
    color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    circles.append((x, y, color))


# Function to check if the character and circles collide each other - increment the score
def check_collision():
    global score
    for circle in circles:
        circle_pos = pygame.Vector2(circle[:2])
        character_pos = pygame.Vector2(character_rect.center)
        distance = character_pos.distance_to(circle_pos)
        if distance < circle_radius + character_size[0] // 2:
            circles.remove(circle)
            score += 1


clock = pygame.time.Clock()

# Game Loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        # Quit Game
        if event.type == pygame.QUIT:
            running = False

    # Check the pressed arrow keys
    keys = pygame.key.get_pressed()
    # UP Arrow key
    if keys[pygame.K_UP] and character_rect.top > 0:
        character_rect.y -= 5
    # DOWN Arrow key
    if keys[pygame.K_DOWN] and character_rect.bottom < window_size[1]:
        character_rect.y += 5
    # LEFT Arrow key
    if keys[pygame.K_LEFT] and character_rect.left > 0:
        character_rect.x -= 5
    # RIGHT Arrow key
    if keys[pygame.K_RIGHT] and character_rect.right < window_size[0]:
        character_rect.x += 5

    # Fill screen with black color
    screen.fill((0, 0, 0))
    # Display the character
    screen.blit(character, character_rect)

    # Condition to check if the circles are less on the screen, create more
    if len(circles) < max_circles:
        create_circle()

    # Draw and display circles on the screen
    for circle in circles:
        pygame.draw.circle(screen, circle[2], circle[:2], circle_radius)

    # Function call - to check the collision
    check_collision()

    # display score
    text = font.render(f"Score: {score}", True, (255, 255, 255))
    screen.blit(text, (10, 10))

    # Update the content of the entire screen window
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
