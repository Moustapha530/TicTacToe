import pygame

makers = []
for i in range(3):
    makers.append([0] * 3)

def draw_grid(screen : pygame.Surface):
    bg = (255, 255, 200)  # White background
    screen.fill(bg)
    grid = (50, 50, 50)  # Dark gray grid lines
    for x in range(1, 3):
        pygame.draw.line(screen, grid, (0, x * 100), (screen.get_width(), x * 100), 5)
        pygame.draw.line(screen, grid, (x * 100, 0), (x * 100, screen.get_height()), 5)

def draw_makers(screen : pygame.Surface):
    for y in range(3):
        for x in range(3):
            if makers[y][x] == 1:
                pygame.draw.line(screen, (255, 0, 0), (x * 100 + 20, y * 100 + 20), (x * 100 + 80, y * 100 + 80), 5)
                pygame.draw.line(screen, (255, 0, 0), (x * 100 + 80, y * 100 + 20), (x * 100 + 20, y * 100 + 80), 5)
            elif makers[y][x] == -1:
                pygame.draw.circle(screen, (0, 0, 255), (x * 100 + 50, y * 100 + 50), 40, 5)