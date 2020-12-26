# Imports necessary for running this file
import pygame
import pygame_menu
from pygame import mixer
from game import *

# Initialize the pygame environment and its components/modules
pygame.init()
surface = pygame.display.set_mode((1200, 800))

# Play background music
mixer.music.load('assets/menu_music.mp3')
#mixer.music.play(-1)

# The Main Menu code where players start their journey
class MainMenu:
    def __init__(self):
        menu = pygame_menu.Menu(800, 600, 'Welcome to SnakePong!', theme=pygame_menu.themes.THEME_GREEN)

        # Creating the menu widgets
        menu.add_text_input('Username :', default='Player X')
        menu.add_button('Settings', self.start_settings_menu)
        menu.add_button('Play', self.start_the_game)
        menu.add_button('Quit', pygame_menu.events.EXIT)
        menu.center_content()

        menu.mainloop(surface)

    def start_the_game(self):
        game = Game()
        game.keeprunning()
        

    def start_settings_menu(self):
        SettingsMenu()
        pass

# The menu used for changing the settings
class SettingsMenu:
    def __init__(self):
        menu = pygame_menu.Menu(800, 600, 'Welcome to SnakePong!', theme=pygame_menu.themes.THEME_SOLARIZED)

        menu.add_selector('Difficulty: ', [('I\'m kinda slow', 1), ('Easy', 2), ('Average', 3), ('Hard', 4), ('Lowkey a professional', 5), ('Insane #NoLife', 6)], onchange=self.__set_difficulty)
        menu.add_selector('Size of playing field: ', [('Small', 1), ('Medium', 2), ('Large', 3), ('Yo Mamah', 4)] )
        menu.add_button('Music: Press to (de-)activate music', self.__set_music)
        menu.add_button('Sounds: Press to (de-)activate sounds', self.__set_sounds)
        menu.add_button('Save settings', self.__save_settings)
        menu.add_button('Discard changes', self.__exit_settings)

        menu.mainloop(surface)

    def __set_difficulty(self, value, difficulty):
        # Do the job here !
        pass

    def __save_settings(self):
        # Save configuration to JSON file
        MainMenu()
        pass

    def __exit_settings(self):
        MainMenu()
        pass

    def __set_music(self):
        if mixer.music.get_busy() == 1:
            mixer.music.stop()
        else:
            mixer.music.play()
        pass

    def __set_sounds(self):
        pass
