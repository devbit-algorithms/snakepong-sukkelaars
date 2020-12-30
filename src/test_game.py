# Imports
from game import Game
import pygame

# Global variables
pygame.init()
surface = pygame.display.set_mode((1200, 800))


# Testing the Game
def test_creating_game():
    game = Game(surface, "Noah", 0, True)
    assert game.get_username() == "Noah"
    assert game.get_numberOfPlayers() == 0

# It is rather difficult to test every little aspect of the game
# since it watches/listens for so many things that it would be more
# of a hassle to write the code for testing than actually running the
# game and looking for errors/bugs manually

# That's why we decided that the game was made through trial&error
# and less testing