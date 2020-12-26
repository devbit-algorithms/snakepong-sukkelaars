import pygame
from playfield import Playfield

class Snake():
    def __init__(self, surface):
        self.__x = 300
        self.__y = 200        
        self.__update_screen()
        self.__surface = surface

    def __update_screen(self):
        pygame.display.flip()

    def update_snake(self):
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_UP]: self.__y -= 1
        if pressed[pygame.K_DOWN]: self.__y += 1
        if pressed[pygame.K_LEFT]: self.__x -= 1
        if pressed[pygame.K_RIGHT]: self.__x += 1
        pygame.draw.rect(self.__surface, (0, 128, 255), pygame.Rect(self.__x, self.__y, 10, 100))
