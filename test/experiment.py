import pygame
from random import randint
from pygame.math import Vector2

pygame.init()

width = 40
rows = 20

screen = pygame.display.set_mode((width * rows, width * rows))
clock = pygame.time.Clock()


class FRUIT:
    def __init__(self):
        self.x = randint(0, rows - 1)
        self.y = randint(0, rows - 1)
        self.pos = Vector2(self.x, self.y)

    def drawFruit(self):
        fruitRect = pygame.Rect(self.x * width, self.y * width, width, width)
        pygame.draw.rect(screen, (255, 0, 0), fruitRect)


class SNAKE:
    def __init__(self):
        self.body = int[Vector2(5, 10), Vector2(6, 10), Vector2(7, 10)]

    def drawSnake(self):
        for block in self.body():
            xPos = int(block.x * width)
            yPos = int(block.y * width)

            drawRect = pygame.Rect(xPos, yPos, width, width)
            pygame.draw.rect(screen, (2, 27, 252), drawRect)


fruit = FRUIT()
snake = SNAKE()
running = True


while running:

    screen.fill((81, 252, 2))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    fruit.drawFruit()
    snake.drawSnake()
    clock.tick(60)
    pygame.display.update()