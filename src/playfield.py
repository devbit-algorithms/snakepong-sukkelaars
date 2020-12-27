# Imports necessary for running this file
import pygame

# Initialize the pygame environment and its components/modules
pygame.init()



# Classes
class Playfield:
    def __init__(self, surface):
        self.__surface = surface

        pygame.display.set_caption("SnakePong")
        WHITE = (255, 255, 255)
        BLACK = (0, 0, 0)
        pygame.draw.rect(self.__surface, BLACK, pygame.Rect(0, 0, 1200, 800))
        pygame.draw.rect(self.__surface, WHITE, pygame.Rect(150, 100, 900, 20)) #top border
        pygame.draw.rect(self.__surface, WHITE, pygame.Rect(150, 100, 20, 600)) #left border
        pygame.draw.rect(self.__surface, WHITE, pygame.Rect(150, 700, 920, 20)) #bottom border
        pygame.draw.rect(self.__surface, WHITE, pygame.Rect(1050, 100, 20, 600)) #right border

    def __update_screen(self):
        pygame.display.flip()

    def __getSurface(self):
        return self.__surface
    
    def getSurface(self):
        return self.__getSurface()

