# Imports necessary for running this file
import pygame
from playfield import Playfield
# Initialize the pygame environment and its components/modules
pygame.init()
surface = pygame.display.set_mode((1200, 800))

class Game:
    def __init__(self):
        #MAKE THE GAME
        print('MAKE THE GAME')
        surface.fill((0,0,0))

        Playfield()
        pygame.display.flip()

    def keeprunning(self):
        done = False

        while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True
