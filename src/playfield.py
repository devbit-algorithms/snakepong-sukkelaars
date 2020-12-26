import pygame


class Playfield:
    def __init__(self):
        screen = pygame.display.set_mode((1200, 800))
        screen.fill((0, 0, 0))
        pygame.display.set_caption("SnakePong")
        WHITE = (255, 255, 255)
        BLACK = (0, 0, 0)
        pygame.draw.rect(screen, BLACK, pygame.Rect(0, 0, 1000, 700))
        pygame.draw.rect(screen, WHITE, pygame.Rect(100, 100, 900, 20)) #top border
        pygame.draw.rect(screen, WHITE, pygame.Rect(100, 100, 20, 600)) #left border
        pygame.draw.rect(screen, WHITE, pygame.Rect(100, 700, 920, 20)) #bottom border
        pygame.draw.rect(screen, WHITE, pygame.Rect(1000, 100, 20, 600)) #right border
        self.__update_screen()

    def __update_screen(self):
        pygame.display.flip()

