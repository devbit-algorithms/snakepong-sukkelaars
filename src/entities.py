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
<<<<<<< HEAD
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
=======
    def __init__(self, surface):
        self.__x = 300
        self.__y = 200        
>>>>>>> f8e6b8b7d7a1fd970b95e40e2861fd96ea5dcde9
        self.__update_screen()
        self.__surface = surface

    def __update_screen(self):
        pygame.display.flip()

    def __update_snake(self):
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_UP]: self.__y -= 3
        if pressed[pygame.K_DOWN]: self.__y += 3
        if pressed[pygame.K_LEFT]: self.__x -= 3
        if pressed[pygame.K_RIGHT]: self.__x += 3
        pygame.draw.rect(self.__surface, (0, 128, 255), pygame.Rect(self.__x, self.__y, 10, 10))

    def update_snake(self):
        self.__update_snake()

class Ball:
    def __init__(self, surface):
        self.__surface = surface
        pygame.draw.circle(self.__surface, (0, 128, 255), (200, 100), 10)
