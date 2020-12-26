import pygame
pygame.init()

class Playfield:
    def __init__(self):
        screen = pygame.display.set_mode((1200, 800))
        screen.fill((0, 0, 0))
        pygame.display.set_caption("SnakePong")
        WHITE = (255, 255, 255)
        BLACK = (0, 0, 0)
        pygame.draw.rect(screen, BLACK, pygame.Rect(0, 0, 1000, 700))
        pygame.draw.rect(screen, WHITE, pygame.Rect(0, 0, 1000, 20))
        pygame.draw.rect(screen, WHITE, pygame.Rect(0, 0, 20, 1000))
        pygame.draw.rect(screen, WHITE, pygame.Rect(0, 700, 1000, 20))
        pygame.draw.rect(screen, WHITE, pygame.Rect(1000, 0, 20, 700))
        self.__update_screen()

    def __update_screen(self):
        pygame.display.flip()

