import pygame

def check_winner(markers):
    # Lignes
    for row in markers:
        s = sum(row)
        if s == 3:
            return 1
        if s == -3:
            return 2

    # Colonnes
    for col in range(3):
        s = markers[0][col] + markers[1][col] + markers[2][col]
        if s == 3:
            return 1
        if s == -3:
            return 2

    # Diagonales
    diag1 = markers[0][0] + markers[1][1] + markers[2][2]
    diag2 = markers[0][2] + markers[1][1] + markers[2][0]

    if diag1 == 3 or diag2 == 3:
        return 1
    if diag1 == -3 or diag2 == -3:
        return 2

    return 0

def is_draw(markers):
    for row in markers:
        if 0 in row:
            return False
    return check_winner(markers) == 0

def draw_end_screen(screen, message):
    font = pygame.font.SysFont(None, 45)
    screen.fill((255, 255, 200))
    text = font.render(message, True, (0, 0, 255))
    screen.blit(text, (20, 120))
