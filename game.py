import pygame

def check_winner(makers):
    y = 0
    winner = 0
    for i in makers:
        if sum(i) == 3:
            winner = 1
        elif sum(i) == -3:
            winner = 2

        if makers[0][y] + makers[1][y] + makers[2][y] == 3:
            winner = 1
        elif makers[0][y] + makers[1][y] + makers[2][y] == -3:
            winner = 2

        y += 1
    if makers[0][0] + makers[1][1] + makers[2][2] == 3 and makers[2][0] + makers[1][1] + makers[0][2] == 3:
        winner = 1
    elif makers[0][0] + makers[1][1] + makers[2][2] == -3 and makers[2][0] + makers[1][1] + makers[0][2] == -3:
        winner = 2

    return winner        

def draw_winner(screen : pygame.Surface, winner):
    font = pygame.font.SysFont(None, 55)
    text = font.render(f"Player {winner} wins!", True, (0, 0, 255))
    screen.fill((255, 255, 200))
    screen.blit(text, (50, 130))