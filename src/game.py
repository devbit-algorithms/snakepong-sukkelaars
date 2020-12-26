# Imports necessary for running this file
import pygame
from playfield import Playfield
from entities import Snake, Ball

# Initialize the pygame environment and its components/modules
pygame.init()



# Classes
class Game:
    def __init__(self, surface):
        self.__clock = pygame.time.Clock()
        self.__surface = surface
        self.__isRunning = True
        #MAKE THE GAME
        print('MAKE THE GAME')
        surface.fill((0,0,0))

        self.__playfield = Playfield(self.__surface)
        self.__surface = self.__playfield.getSurface()
        self.__snake = Snake(self.__surface,self.__isRunning)

    def keeprunning(self):

        while self.__isRunning:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        self.__isRunning = False

            if self.__snake.game_over():
                self.__isRunning = False 
            self.__surface.fill((0,0,0))
            Playfield(self.__surface)
            self.__snake.update_snake()
            self.__ball = Ball(self.__surface)
            pygame.display.flip()
            self.__clock.tick(60)
