import pygame
from pygame.locals import *
from game import check_winner, is_draw, draw_end_screen
from grid import draw_grid, draw_markers, markers

pygame.init()

screen = pygame.display.set_mode((300, 300))
pygame.display.set_caption("TicTacToe")

player = 1
running = True
game_over = False
message = ""

while running:
    draw_grid(screen)
    draw_markers(screen)

    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

        if not game_over and event.type == MOUSEBUTTONUP:
            x, y = pygame.mouse.get_pos()
            row, col = y // 100, x // 100

            if markers[row][col] == 0:
                markers[row][col] = player

                winner = check_winner(markers)
                if winner:
                    game_over = True
                    message = f"Player {winner} wins!"
                elif is_draw(markers):
                    game_over = True
                    message = "Draw!"

                player *= -1

        elif game_over and event.type == KEYDOWN and event.key == K_r:
            for r in range(3):
                for c in range(3):
                    markers[r][c] = 0
            game_over = False
            player = 1

    if game_over:
        draw_end_screen(screen, message)

    pygame.display.update()

pygame.quit()
