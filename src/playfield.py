# Imports necessary for running this file
import pygame

# Initialize the pygame environment and its components/modules
pygame.init()
pygame.font.init()



# Classes
class Playfield:
    def __init__(self, surface, username, score):
        #Initialize variables
        self.__surface = surface
        self.__username = username
        self.__score = score

        # Making the playfield
        pygame.display.set_caption("SnakePong - The Game")
        WHITE = (255, 255, 255)
        BLACK = (0, 0, 0)

        pygame.draw.rect(self.__surface, BLACK, pygame.Rect(0, 0, 1200, 800))
        pygame.draw.rect(self.__surface, WHITE, pygame.Rect(150, 100, 900, 20)) #top border
        pygame.draw.rect(self.__surface, WHITE, pygame.Rect(150, 100, 20, 600)) #left border
        pygame.draw.rect(self.__surface, WHITE, pygame.Rect(150, 700, 920, 20)) #bottom border
        pygame.draw.rect(self.__surface, WHITE, pygame.Rect(1050, 100, 20, 600)) #right border
        self.__draw_score_username()

    def __update_screen(self):
        pygame.display.flip()

    def __getSurface(self):
        return self.__surface

    def __draw_score_username(self):
        font = pygame.font.SysFont('Comic Sans MS', 50)
        text = font.render('Welcome {0}, this is your current score: {1}'.format(self.__username, self.__score), False, (255,255,255))
        self.__surface.blit(text, (10,10))
    
    def getSurface(self):
        return self.__getSurface()

