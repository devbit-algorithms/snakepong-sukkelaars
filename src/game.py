# Imports necessary for running this file
import pygame
from playfield import Playfield
from pygame import mixer
from entities import Snake, Ball, Food, Paddle
from tkinter import messagebox, Tk

# Initialize the pygame environment and its components/modules
pygame.init()



# Classes
class Game:
    def __init__(self, surface, username, numberOfPlayers, soundsOn):
        # Initialize variables
        self.__clock = pygame.time.Clock()
        self.__surface = surface
        self.__isRunning = True
        self.__username = username
        self.__numberOfPlayers = numberOfPlayers
        self.__soundsOn = soundsOn

        # Initialize the game entities
        self.__ball = Ball(self.__surface)
        self.__score = self.__ball.get_score()
        self.__playfield = Playfield(self.__surface, self.__username, self.__score)
        self.__surface = self.__playfield.getSurface()
        self.__snake = Snake(self.__surface,self.__isRunning)
        self.__food = Food(self.__surface)

        # Check if multiplayer or not
        if self.__numberOfPlayers == 0:
            self.__paddle = Paddle(self.__surface)
        else:
            self.__paddle = Paddle(self.__surface, True)

    def start_game(self):

        while self.__isRunning:
            # Check if game is being closed manually
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        self.__isRunning = False

            # Check if game is done
            if self.__snake.game_over():
                self.__isRunning = False
                mixer.music.stop()
                self.__play_gameover_sound()
                Tk().wm_withdraw()                  # Pop-up screen using tkinter library
                messagebox.showinfo('GAME OVER - You a dead snake bruv','I admit that I touched myself/walls :\'(')
            
            # Check if snake eats the food
            elif self.__snake.get_head().colliderect(self.__food.show_food()):
                self.__snake.set_length()
                self.__play_touch_sound()
                self.__food.update_food()

            # Check if the paddle touches the ball
            elif self.__paddle.get_paddle().colliderect(self.__ball.get_ball()):
                self.__ball.bounce()
                self.__play_touch_sound()

            # Check if one of the segments of the snake touches the ball
            for segment in self.__snake.get_snake():
                if segment.colliderect(self.__ball.get_ball()):
                    self.__ball.bounce()
                    self.__play_touch_sound()

            # Continously update the game with the new values/info
            self.__update_game()

    def __update_game(self):
        self.__surface.fill((0,0,0))
        self.__score = self.__ball.get_score()
        Playfield(self.__surface, self.__username, self.__score)
        self.__snake.update_snake()
        self.__food.look_for_food()
        self.__paddle.update_paddle()
        self.__ball.update_ball()
        pygame.display.flip()
        self.__clock.tick(60)

    # Check if sounds are activated or not and then play them accordingly
    def __play_touch_sound(self):
        if self.__soundsOn:
            touch = mixer.Sound("assets/touch_sound.wav")
            mixer.Sound.play(touch)

    def __play_gameover_sound(self):
        if self.__soundsOn:
            gameover = mixer.Sound("assets/game_over_sound.wav")
            mixer.Sound.play(gameover)

