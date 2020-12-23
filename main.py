import pygame
import math
import random
import tkinter as tk
from tkinter import messagebox
from pygame import surface
from pygame.constants import K_DOWN, K_LEFT, K_RIGHT, K_UP
from pygame.time import Clock

# Initialize Pygame
pygame.init()

width = 600
screen = pygame.display.set_mode((width, width))
rows = 20

# Setting the caption
pygame.display.set_caption("Snake")
# icon = pygame.image.load('./Blegh')


class cube:
    pass


class snake:
    body = []
    turns = {}

    def __init__(self, color, pos):
        self.color = color
        self.head = cube(pos)
        self.body.append(self.head)

        # To move in one direction only
        self.dirnX = 0
        self.dirnY = 1

    def move(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            keys = pygame.key.get_pressed()

            for key in keys:
                if keys[K_LEFT]:
                    self.dirnX = -1
                    self.dirnY = 0
                    self.turns[self.head.pos[:]] = [self.dirnX, self.dirnY]

                elif keys[K_RIGHT]:
                    self.dirnX = 1
                    self.dirnY = 0
                    self.turns[self.head.pos[:]] = [self.dirnX, self.dirnY]

                elif keys[K_UP]:
                    self.dirnX = 0
                    self.dirnY = 1
                    self.turns[self.head.pos[:]] = [self.dirnX, self.dirnY]

                elif keys[K_DOWN]:
                    self.dirnX = -0
                    self.dirnY = -1
                    self.turns[self.head.pos[:]] = [self.dirnX, self.dirnY]

        for i, c in enumerate(self.body):
            p = c.pos[:]


def drawGrid(w, row, surface):
    # Grid size
    sizeBtwn = w // row

    x = 0
    y = 0

    for l in range(row):

        # Adds line in rows and column in each iteration of loop
        x += sizeBtwn
        y += sizeBtwn

        # For vertical line
        pygame.draw.line(surface, (255, 255, 255), (x, 0), (x, w))

        # For horizontal line
        pygame.draw.line(surface, (255, 255, 255), (0, y), (w, y))


def redrawScreen(surface):
    global rows, width

    surface.fill((0, 0, 0))
    drawGrid(width, rows, screen)
    pygame.display.update()


def mainLoop():
    global screen
    pygame.time.delay(100)
    s = snake((255, 0, 0), (10, 10))
    running = True
    clock = pygame.time.Clock()

    while running:
        pygame.time.delay(50)
        clock.tick(10)
        redrawScreen(screen)


mainLoop()
