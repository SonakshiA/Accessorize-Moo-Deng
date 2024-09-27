import pygame
import random

# Initialize Pygame
pygame.init()

# Set up display
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("What Should Moo Deng Wear?")

background_image = pygame.image.load('moodeng.jpg')
background_image = pygame.transform.scale(background_image, (WIDTH, HEIGHT))

# Define speed
FALLING_SPEED = 20

# Shape class
class Shape:
    def __init__(self, x, y, size,shape):
        self.x = x
        self.y = y
        self.size = size
        self.shape = shape

    def draw(self, screen):
        image = pygame.image.load(self.shape + '.png')  # Replace 'crown.png' with your image file
        image = pygame.transform.scale(image, (200, 150))  # Resize the crown to a reasonable size
        screen.blit(image, (int(self.x), int(self.y)))

    def fall(self):
        self.y += FALLING_SPEED
        # Reset position if it falls below the screen
        if self.y - self.size > HEIGHT:
            self.y = -self.size
            self.shape = random.choice(['crown','bow','cap','beach_hat','hat','cowboy'])


# Initialize the object (position, size, and color)
shape = Shape(WIDTH//2-110, -50, 50, random.choice(['crown','bow','cap','beach_hat','hat','cowboy']))

# Main game loop
running = True
paused = False
clock = pygame.time.Clock()

while running:
    screen.blit(background_image, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            paused = not paused

    # Update the shape's position and draw it
    if not paused:
        shape.fall()
    shape.draw(screen)

    # Update the display
    pygame.display.flip()

    # Cap the frame rate at 60 frames per second
    clock.tick(60)

# Quit Pygame
pygame.quit()
