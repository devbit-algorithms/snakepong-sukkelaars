import pygame


class Playfield:
    def __init__(self):
        self.__surface = pygame.display.set_mode((1200, 800))

        pygame.display.set_caption("SnakePong")
        WHITE = (255, 255, 255)
        BLACK = (0, 0, 0)
        pygame.draw.rect(self.__surface, BLACK, pygame.Rect(0, 0, 1000, 700))
        pygame.draw.rect(self.__surface, WHITE, pygame.Rect(100, 100, 900, 20)) #top border
        pygame.draw.rect(self.__surface, WHITE, pygame.Rect(100, 100, 20, 600)) #left border
        pygame.draw.rect(self.__surface, WHITE, pygame.Rect(100, 700, 920, 20)) #bottom border
        pygame.draw.rect(self.__surface, WHITE, pygame.Rect(1000, 100, 20, 600)) #right border

    def __update_screen(self):
        pygame.display.flip()

    def __getSurface(self):
        return self.__surface
    
    def getSurface(self):
        return self.__getSurface()

