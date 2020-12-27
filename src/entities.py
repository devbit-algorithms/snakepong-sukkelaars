# Imports necessary for running this file
import pygame
import random
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
        self.__positions = [(600, 400)]
        self.__length = 1
        self.__direction = random.choice([(0, 1), (0, -1), (-1, 0), (1, 0)])
        self.__update_screen()
        self.__surface = surface
        self.__isRunning = running

    def __get_head_position(self):
        return self.__positions[0]

    def __turn_snake(self, point):
        if self.__length > 1 and (point[0] * -1, point[1] * -1) == self.__direction:
            pass
        else:
            self.__direction = point
    
    def __move_snake(self):
        beak = self.__get_head_position()
        x, y = self.__direction
        newBeak = ((beak[0] + (x * 2)), (beak[1] + (y * 2)))

        if len(self.__positions) > 2 and newBeak in self.__positions[2:]:
            self.__isRunning = False
            self.__update_snake()
        else:
            self.__positions.insert(0, newBeak)
            if len(self.__positions) > self.__length:
                self.__positions.pop()

    def __draw_snake(self, surface):
        for p in self.__positions:
            block = pygame.Rect((p[0], p[1]), (20, 20))
            pygame.draw.rect(self.__surface, (0, 128, 255), block)
            pygame.draw.rect(self.__surface, (0, 128, 255), block, 1)

    def __update_screen(self):
        pygame.display.flip()

    def __update_snake(self):
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_UP]:
            self.__turn_snake((0, -1))
        if pressed[pygame.K_DOWN]:
            self.__turn_snake((0 , 1))
        if pressed[pygame.K_LEFT]:
            self.__turn_snake((-1, 0))
        if pressed[pygame.K_RIGHT]:
            self.__turn_snake((1, 0))

        self.game_over()
        self.__draw_snake(self.__surface)

# Public methods
    def update_snake(self):
        self.__update_snake()
        self.__move_snake()

    def get_head_position(self):
        return self.__get_head_position()

    def game_over(self):
        return (self.__get_head_position()[0] > 1030 or self.__get_head_position()[0] < 170 or self.__get_head_position()[1] > 678 
        or self.__get_head_position()[1] < 122 or self.__isRunning == False)

    def set_length(self):
        self.__length += 4


class Ball:
    def __init__(self, surface):
        self.__surface = surface
        pygame.draw.circle(self.__surface, (0, 128, 255), (200, 100), 10)

class Food:
    def __init__(self, surface):
        self.__color = (223, 163, 49)
        self.__surface = surface
        self.__create_frozen_food()
        self.__cook_food()

    def __create_frozen_food(self):
        self.__position = (random.randint(171, 449) * 2, random.randint(121, 299) * 2)
    
    def __cook_food(self):
        food = pygame.Rect((self.__position[0], self.__position[1]), (10, 10))
        pygame.draw.rect(self.__surface, self.__color, food)
        pygame.draw.rect(self.__surface, (93, 216, 228), food, 1)

    def update_food(self):
        self.__create_frozen_food()
        self.__cook_food()

    def look_for_food(self):
        self.__cook_food()

    def get_food_location(self):
        return self.__position
