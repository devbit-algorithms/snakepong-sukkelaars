# Imports necessary for running this file
import pygame
from playfield import Playfield
from entities import Snake, Ball, Food

# Initialize the pygame environment and its components/modules
pygame.init()



# Classes
class Game:
    def __init__(self, surface):
        self.__clock = pygame.time.Clock()
        self.__surface = surface
        self.__isRunning = True

        surface.fill((0,0,0))

        self.__playfield = Playfield(self.__surface)
        self.__surface = self.__playfield.getSurface()
        self.__snake = Snake(self.__surface,self.__isRunning)
        self.__food = Food(self.__surface)

    def keeprunning(self):

        while self.__isRunning:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        self.__isRunning = False

            if self.__snake.game_over():
                self.__isRunning = False
            elif self.__food.get_food_location()[0] - 3 <= self.__snake.get_head_position()[0] <= self.__food.get_food_location()[0] + 3:
                self.__snake.set_length()
                self.__food.update_food()
            self.__surface.fill((0,0,0))
            Playfield(self.__surface)
            self.__snake.update_snake()
            self.__food.look_for_food()
            self.__ball = Ball(self.__surface)
            pygame.display.flip()
            self.__clock.tick(60)
