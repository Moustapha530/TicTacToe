import pygame
from pygame.locals import *

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("TicTacToe")
pygame.init()

running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

    pygame.display.update()

pygame.quit()