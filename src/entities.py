# Imports necessary for running this file
import pygame
import os
from playfield import Playfield

# PyGame image library to not load an image every time
_image_library = {}
def get_image(path):
    global _image_library
    image = _image_library.get(path)
    if image == None:
        canonicalized_path = path.replace('/', os.sep).replace('', os.sep)
        image = pygame.image.load(canonicalized_path)
        _image_library[path] = image
    return image


# Initialize the pygame environment and its components/modules
pygame.init()



# Classes
class Snake():
    def __init__(self, surface, running):
        self.positions = [600, 350]     
        self.__update_screen()
        self.__surface = surface
        self.__isRunning = running

    def get_head_position(self):
        return self.positions[0]

    def __draw_snake(self, surface):
        for p in self.positions:
            r = pygame.Rect((p[0], p[1]), (20, 20))
            pygame.draw.rect(self.__surface, (0, 128, 255), r)
            pygame.draw.rect(self.__surface, (0, 128, 255), r, 1)

    def __update_screen(self):
        pygame.display.flip()

    def __update_snake(self):
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_UP]: self.positions[1] -= 3
        if pressed[pygame.K_DOWN]: self.positions[1] += 3
        if pressed[pygame.K_LEFT]: self.positions[0] -= 3
        if pressed[pygame.K_RIGHT]: self.positions[0] += 3

        self.game_over()
        self.__draw_snake(self.__surface)
       # pygame.draw.rect(self.__surface, (0, 128, 255), pygame.Rect(self.positions[0], self.positions[1], 15, 15))

    def update_snake(self):
        self.__update_snake()

    def game_over(self):
        return (self.positions[0] >= 980 or self.positions[0] < 120 or self.positions[1] >= 680 or self.positions[1] < 120)


class Ball:
    def __init__(self, surface):
        self.__surface = surface
        pygame.draw.circle(self.__surface, (0, 128, 255), (200, 100), 10)
