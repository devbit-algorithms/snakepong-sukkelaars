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
class Snake:
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

    def get_head(self):
        return pygame.Rect((self.__positions[0][0], self.__positions[0][1]), (20, 20))

    def game_over(self):
        return (self.__get_head_position()[0] > 1030 or self.__get_head_position()[0] < 170 or self.__get_head_position()[1] > 678 
        or self.__get_head_position()[1] < 122 or self.__isRunning == False)

    def set_length(self):
        self.__length += 5


class Ball:
    def __init__(self, surface):
        self.__surface = surface
        self.__position = [(400, 400)]
        self.__set_velocity()

    def __set_velocity(self):
        self.__velocity = [random.randint(-4, 4), random.randint(-4, 4)]

    def get_current_position(self):
        return self.__position[0]

    def __move_ball(self):
        newPos = ((self.get_current_position()[0] + self.__velocity[0]), (self.get_current_position()[1] + self.__velocity[1]))

        if newPos[0] < 180:
            self.__velocity[0] = -self.__velocity[0]
            self.__move_ball()
        elif newPos[0] > 1030:
            self.__velocity[0] = -self.__velocity[0]
            self.__move_ball()
        elif newPos[1] > 680:
            self.__velocity[1] = -self.__velocity[1]
            self.__move_ball()
        elif newPos[1] < 125:
            self.__velocity[1] = -self.__velocity[1]
            self.__move_ball()

        self.__position.insert(0, newPos)
        if len(self.__position) > 1:
            self.__position.pop()

    def __draw_ball(self):
        self.__image = pygame.draw.circle(self.__surface, (0, 128, 255), (self.get_current_position()[0], self.get_current_position()[1]), 10)

    def update_ball(self):
        self.__move_ball()
        self.__draw_ball()
    
    def bounce(self):
        self.__velocity[0] = -self.__velocity[0]
        self.__velocity[1] = random.randint(-8,8)
        


class Paddle:
    def __init__(self, surface):
        self.__surface = surface
        self.__position = [(220, 350)]

    def __move_paddle(self):
        self.__direction = random.choice([(0, 4), (0, -4), (0, 5), (0, -5), (0, 3), (0, -3)])
        x, y = self.__direction
        newPos = ((self.get_current_position()[0] + (x * 2)), (self.get_current_position()[1] + (y * 2)))
        print(self.get_current_position())
        print(newPos)
        if newPos[1] > 600:
            newPos = ((self.get_current_position()[0] + (x * 2)), 600)
        elif newPos[1] < 120:
            newPos = ((self.get_current_position()[0] + (x * 2)), 120)

        print(newPos)

        self.__position.insert(0, newPos)
        if len(self.__position) > 1:
            self.__position.pop()

    def get_current_position(self):
        return self.__position[0]
    
    def get_paddle(self):
        return self.__paddle

    def __draw_paddle(self):
        self.__paddle = pygame.Rect(self.get_current_position()[0], self.get_current_position()[1], 10, 100)
        pygame.draw.rect(self.__surface, (0, 128, 255), self.__paddle)

    def update_paddle(self):
        self.__move_paddle()
        self.__draw_paddle()


class Food:
    def __init__(self, surface):
        self.__color = (223, 163, 49)
        self.__surface = surface
        self.__create_frozen_food()
        self.__cook_food()

    def __create_frozen_food(self):
        self.__position = (random.randint(171, 449) * 2, random.randint(121, 299) * 2)
    
    def __cook_food(self):
        self.__food = pygame.Rect((self.__position[0], self.__position[1]), (10, 10))
        pygame.draw.rect(self.__surface, self.__color, self.__food)
        pygame.draw.rect(self.__surface, (93, 216, 228), self.__food, 1)

    def update_food(self):
        self.__create_frozen_food()
        self.__cook_food()

    def look_for_food(self):
        self.__cook_food()

    def show_food(self):
        return self.__food

    def get_food_location(self):
        return self.__position
