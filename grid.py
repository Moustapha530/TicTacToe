import pygame

markers = [[0 for _ in range(3)] for _ in range(3)]

def draw_grid(screen):
    screen.fill((255, 255, 200))

    for i in range(1, 3):
        pygame.draw.line(screen, (50, 50, 50), (0, i * 100), (300, i * 100), 5)
        pygame.draw.line(screen, (50, 50, 50), (i * 100, 0), (i * 100, 300), 5)

def draw_markers(screen):
    for y in range(3):
        for x in range(3):
            if markers[y][x] == 1:
                pygame.draw.line(screen, (255, 0, 0), (x*100+20, y*100+20), (x*100+80, y*100+80), 5)
                pygame.draw.line(screen, (255, 0, 0), (x*100+80, y*100+20), (x*100+20, y*100+80), 5)

            elif markers[y][x] == -1:
                pygame.draw.circle(screen, (0, 0, 255), (x*100+50, y*100+50), 40, 5)
