import pygame
from pygame.locals import *
from grid import draw_grid, draw_makers, makers

screen = pygame.display.set_mode((300, 300))
pygame.display.set_caption("TicTacToe")
pygame.init()

player = 1  # Player 1 starts
pos = []
clicked = False
running = True

while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        elif event.type == MOUSEBUTTONDOWN and clicked == False:
            clicked = True
        elif event.type == MOUSEBUTTONUP and clicked == True:
            clicked = False
            pos = pygame.mouse.get_pos()
            if makers[pos[1] // 100][pos[0] // 100] == 0:
                makers[pos[1] // 100][pos[0] // 100] = player
                player *= -1

    draw_grid(screen)
    draw_makers(screen)
    pygame.display.update()

pygame.quit()