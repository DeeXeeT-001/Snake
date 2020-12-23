import pygame
import math
import random
import tkinter as tk
from tkinter import messagebox
from pygame import surface

from pygame.time import Clock

# Initialize Pygame
pygame.init()

width = 600
screen = pygame.display.set_mode((width, width))
rows = 20

# Setting the caption
pygame.display.set_caption("Snake")
# icon = pygame.image.load('./Blegh')


def drawGrid(w, row, surface):
    sizeBtwn = w // row

    x = 0
    y = 0

    for l in range(row):
        x += sizeBtwn
        y += sizeBtwn

        pygame.draw.line(surface, (255, 255, 255), (x, 0), (x, w))
        pygame.draw.line(surface, (255, 255, 255), (0, y), (w, y))


def redrawScreen(surface):
    global rows, width

    surface.fill((0, 0, 0))
    drawGrid(width, rows, screen)
    pygame.display.update()


def mainLoop():
    global screen
    pygame.time.delay(100)
    # s = snake((255, 0, 0), (10, 10))
    running = True
    clock = pygame.time.Clock()

    while running:
        pygame.time.delay(50)
        clock.tick(10)
        redrawScreen(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False


mainLoop()
