import pygame
from pygame.locals import *
from grid import draw_grid

screen = pygame.display.set_mode((300, 300))
pygame.display.set_caption("TicTacToe")
pygame.init()


running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
            
    draw_grid(screen)
    pygame.display.update()

pygame.quit()