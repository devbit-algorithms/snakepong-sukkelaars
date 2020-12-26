import pygame
from playfield import Playfield

screen = pygame.display.set_mode((1200, 800))
class Snake():
    def __init__(self):
        x = 300
        y = 200
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP: y -= 10
                elif event.key == pygame.K_DOWN: y += 10
                elif event.key == pygame.K_LEFT: x -= 10
                elif event.key == pygame.K_RIGHT: x += 10
        pygame.draw.rect(screen, (0, 128, 255), pygame.Rect(x, y, 10, 10))
        self.__update_screen()

    def __update_screen(self):
        pygame.display.flip()