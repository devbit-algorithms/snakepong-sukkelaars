# Imports necessary for running this file
import pygame
import pygame_menu
from pygame import mixer
from game import Game
import json

# Initialize the pygame environment and its components/modules
pygame.init()

# Play background music
mixer.music.load('assets/menu_music.mp3')
#mixer.music.play(-1)



# The Main Menu code where players start their journey
class MainMenu:
    def __init__(self, numberOfPlayers = 0, soundsOn = True):
        # Creating the menu and setting the variables
        pygame.display.set_caption("SnakePong - The Main Menu")
        self.__surface = pygame.display.set_mode((1200, 800))
        self.__menu = pygame_menu.Menu(800, 600, 'Welcome to SnakePong!', theme=pygame_menu.themes.THEME_GREEN)
        self.__numberOfPlayers = numberOfPlayers
        self.__soundsOn = soundsOn

        # Creating the menu widgets
        self.__username = self.__menu.add_text_input('Username :', default='Player X')
        self.__menu.add_button('Settings', self.__start_settings_menu)
        self.__menu.add_button('Play', self.__start_the_game)
        self.__menu.add_button('Quit', pygame_menu.events.EXIT)
        self.__menu.center_content()

        self.__menu.mainloop(self.__surface)        # Loop is required for continues checking for events

    def __start_the_game(self):
        self.__username = self.__username.get_value()  
        game = Game(self.__surface, self.__username, self.__numberOfPlayers, self.__soundsOn)
        game.start_game()
        MainMenu()
        

    def __start_settings_menu(self):
        SettingsMenu(self.__surface, self.__soundsOn)

# The menu used for changing the settings
class SettingsMenu:
    def __init__(self, surface, soundsOn):
        # Creating the menu and setting the variables
        pygame.display.set_caption("SnakePong - The Settings Menu")
        menu = pygame_menu.Menu(800, 600, 'Welcome to SnakePong!', theme=pygame_menu.themes.THEME_SOLARIZED)
        self.__surface = surface
        self.__soundsOn = soundsOn

        # Creating the menu widgets
        self.__numberOfPlayers = menu.add_selector('Players: ', [('1 Player', 1), ('2 Players', 2)])
        menu.add_selector('Difficulty: ', [('I\'m kinda slow', 1), ('Easy', 2), ('Average', 3), ('Hard', 4), ('Lowkey a professional', 5), ('Insane #NoLife', 6)], onchange=self.__set_difficulty)
        menu.add_selector('Size of playing field: ', [('Small', 1), ('Medium', 2), ('Large', 3), ('Yo Mamah', 4)] )
        menu.add_button('Music: Press to (de-)activate music', self.__set_music)
        menu.add_button('Sounds: Press to (de-)activate sounds', self.__set_sounds)
        menu.add_button('Save settings', self.__save_settings)
        menu.add_button('Discard changes', self.__exit_settings)

        menu.mainloop(self.__surface)            # Loop is required for continues checking for events

    def __set_difficulty(self, value, difficulty):
        # Do the job here ! Can be implemented as well by changing the values of the
        # playing field or the speed/size of the snake/ball/paddle/food
        pass

    def __save_settings(self):
        # Save configuration to JSON file or other file - could be implemented
        MainMenu(self.__numberOfPlayers.get_value()[1], self.__soundsOn)

    def __exit_settings(self):
        MainMenu()

    def __set_music(self):
        if mixer.music.get_busy() == 1:
            mixer.music.stop()
        else:
            mixer.music.play()

    def __set_sounds(self):
        if self.__soundsOn:
            self.__soundsOn = False
        else:
            self.__soundsOn = True
