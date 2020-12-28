# Imports necessary for running this file
import pygame
from playfield import Playfield
from entities import Snake, Ball, Food, Paddle
from tkinter import messagebox, Tk

# Initialize the pygame environment and its components/modules
pygame.init()



# Classes
class Game:
    def __init__(self, surface, username):
        #Initialize variables
        self.__clock = pygame.time.Clock()
        self.__surface = surface
        self.__isRunning = True
        self.__username = username

        surface.fill((0,0,0))

        self.__ball = Ball(self.__surface)
        self.__score = self.__ball.get_score()
        self.__playfield = Playfield(self.__surface, self.__username, self.__score)
        self.__surface = self.__playfield.getSurface()
        self.__snake = Snake(self.__surface,self.__isRunning)
        self.__food = Food(self.__surface)
        self.__paddle = Paddle(self.__surface)



    def keeprunning(self):

        while self.__isRunning:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        self.__isRunning = False

            if self.__snake.game_over():
                self.__isRunning = False
                Tk().wm_withdraw() #to hide the main window
                messagebox.showinfo('GAME OVER - You a dead snake bruv','I admit that I touched myself/walls :\'(')
            elif self.__snake.get_head().colliderect(self.__food.show_food()):
                self.__snake.set_length()
                self.__food.update_food()
            elif self.__paddle.get_paddle().colliderect(self.__ball.get_ball()):
                self.__ball.bounce()
            for segment in self.__snake.get_snake():
                if segment.colliderect(self.__ball.get_ball()):
                    self.__ball.bounce()
            
            self.__surface.fill((0,0,0))
            self.__score = self.__ball.get_score()
            Playfield(self.__surface, self.__username, self.__score)
            self.__snake.update_snake()
            self.__food.look_for_food()
            self.__paddle.update_paddle()
            self.__ball.update_ball()
            pygame.display.flip()
            self.__clock.tick(60)
