# Imports necessary for running this file
import pygame
import random
import os
from playfield import Playfield

# Initialize the pygame environment and its components/modules
pygame.init()



# Classes
class Snake:
    def __init__(self, surface, running, isBeingTested = False, direction = (0, -1)):
        # Initialize variables
        self.__positions = [(600, 400)]
        self.length = 15
        #Only added this code for making it testable
        if isBeingTested:
            self.__direction = direction
        else:
            self.__direction = random.choice([(0, 1), (0, -1), (-1, 0), (1, 0)])
        self.__surface = surface
        self.__isRunning = running

    # Private methods/functions
    def __get_head_position(self):
        return self.__positions[0]

    def __turn_snake(self, point):
        if (point[0] * -1, point[1] * -1) == self.__direction:
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
            if len(self.__positions) > self.length:
                self.__positions.pop()

    def __draw_snake(self, surface):
        for p in self.__positions:
            block = pygame.Rect((p[0], p[1]), (20, 20))
            pygame.draw.rect(self.__surface, (0, 128, 255), block)
            pygame.draw.rect(self.__surface, (0, 128, 255), block, 1)

    def __update_snake(self):
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_UP]:
            self.__turn_snake((0, -1))
        elif pressed[pygame.K_DOWN]:
            self.__turn_snake((0, 1))
        elif pressed[pygame.K_LEFT]:
            self.__turn_snake((-1, 0))
        elif pressed[pygame.K_RIGHT]:
            self.__turn_snake((1, 0))

        self.game_over()
        self.__draw_snake(self.__surface)

    # Public methods/functions
    def update_snake(self, isBeingTested = False):
        self.__update_snake()
        #Only added this code for the tests, serves no other purpose
        if isBeingTested:
            self.__turn_snake((1,0))
        self.__move_snake()

    def get_head_position(self):
        return self.__get_head_position()

    def get_direction(self):
        return self.__direction

    def get_head(self):
        return pygame.Rect((self.__positions[0][0], self.__positions[0][1]), (20, 20))

    def get_snake(self):
        self.full_snake = []
        for pos in self.__positions:
            self.full_snake.append(pygame.Rect((pos[0], pos[1]), (20, 20)))
        return self.full_snake

    def game_over(self, isBeingTested = False, x = 0, y = 0):
        if isBeingTested:
            return (x > 1030 or y > 678)
        else:
            return (self.__get_head_position()[0] > 1030 or self.__get_head_position()[0] < 170 or self.__get_head_position()[1] > 678
                or self.__get_head_position()[1] < 122 or self.__isRunning == False)

    def set_length(self):
        self.length += 5

    def get_length(self):
        return self.length


class Ball:
    def __init__(self, surface):
        # Initialize variables
        self.score = 0
        self.__surface = surface
        self.__position = [(400, 400)]
        self.__set_velocity()
        self.__ball = pygame.Rect(self.get_current_position()[
                                  0], self.get_current_position()[1], 10, 10)

    # Private methods/functions
    def __set_velocity(self):
        self.__velocity = [random.randint(-2, 2), random.randint(-2, 2)]

    def __move_ball(self):
        newPos = ((self.get_current_position()[0] + self.__velocity[0]), (self.get_current_position()[1] + self.__velocity[1]))

        if newPos[0] < 180:
            self.__velocity[0] = -self.__velocity[0]
            self.__move_ball()
            self.score += 1
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
        self.__ball = pygame.Rect(self.get_current_position()[0], self.get_current_position()[1], 10, 10)

    def __draw_ball(self):
        self.__image = pygame.draw.rect(
            self.__surface, (0, 128, 255), self.__ball)

    # Public methods/functions
    def get_current_position(self):
        return self.__position[0]

    def update_ball(self):
        self.__move_ball()
        self.__draw_ball()

    def bounce(self):
        self.__velocity[0] = -self.__velocity[0]
        self.__velocity[1] = random.randint(-8, 8)

    def get_ball(self):
        return self.__ball

    def get_score(self):
        return self.score


class Paddle:
    def __init__(self, surface, isMultiplayer=False):
        # Initialize variables
        self.__surface = surface
        self.__position = [(220, 350)]
        self.__paddle = pygame.Rect(self.get_current_position()[
                                    0], self.get_current_position()[1], 10, 100)
        self.__newPos = self.__position[0]
        self.__isMultiplayer = isMultiplayer

    # Private methods/functions
    def __move_paddle_random(self):
        self.__direction = random.choice(
            [(0, 4), (0, -4), (0, 5), (0, -5), (0, 3), (0, -3)])
        x, y = self.__direction
        self.__newPos = (220, (self.get_current_position()[1] + (y * 2)))
        self.__check_newPos()

    def __move_paddle_multiplayer(self):
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_z]:
            self.__newPos = (220, (self.get_current_position()[1] - 4))
        elif pressed[pygame.K_s]:
            self.__newPos = (220, (self.get_current_position()[1] + 4))
        self.__check_newPos()

    def __check_newPos(self):
        if self.__newPos[1] > 600:
            self.__newPos = (220, 600)
        elif self.__newPos[1] < 120:
            self.__newPos = (220, 120)

        self.__position.insert(0, self.__newPos)
        if len(self.__position) > 1:
            self.__position.pop()

    def __draw_paddle(self):
        self.__paddle = pygame.Rect(self.get_current_position()[
                                    0], self.get_current_position()[1], 10, 100)
        pygame.draw.rect(self.__surface, (0, 128, 255), self.__paddle)

    # Public methods/functions
    def get_current_position(self):
        return self.__position[0]

    def get_paddle(self):
        return self.__paddle

    def update_paddle(self):
        if not self.__isMultiplayer:
            self.__move_paddle_random()
        else:
            self.__move_paddle_multiplayer()
        self.__draw_paddle()


class Food:
    def __init__(self, surface):
        # Initialize variables
        self.__color = (223, 163, 49)
        self.__surface = surface
        self.__create_frozen_food()
        self.__cook_food()

    # Private methods/functions
    def __create_frozen_food(self):
        self.__position = (random.randint(171, 449) * 2, random.randint(121, 299) * 2)

    def __cook_food(self):
        self.food = pygame.Rect((self.__position[0], self.__position[1]), (10, 10))
        # Drawing the food with a border
        pygame.draw.rect(self.__surface, self.__color, self.food)
        pygame.draw.rect(self.__surface, (93, 216, 228), self.food, 1)

    # Public methods/functions
    def update_food(self):
        self.__create_frozen_food()
        self.__cook_food()

    def look_for_food(self):
        self.__cook_food()

    def show_food(self):
        return self.food

    def get_food_location(self):
        return self.__position