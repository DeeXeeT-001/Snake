import pygame

# Initialize Pygame
pygame.init()

width = 600
screen = pygame.display.set_mode((width, width))

# Setting the caption
pygame.display.set_caption("Snake Game")
# icon = pygame.image.load('./Blegh')


def mainLoop():
    global screen

    running = True
    screen.fill((0, 0, 0))

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

    pygame.display.update()


mainLoop()
