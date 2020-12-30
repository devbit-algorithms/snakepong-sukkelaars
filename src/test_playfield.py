# Imports
from playfield import Playfield
import pygame

# Global variables
pygame.init()
surface = pygame.display.set_mode((1200, 800))


# Testing the Playfield
def test_creating_playfield():
    playfield = Playfield(surface, "Noah", 7)
    assert playfield.get_surface() == surface
    assert playfield.get_username() == "Noah"
    assert playfield.get_score() == 7