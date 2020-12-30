# Imports
from entities import Snake, Ball, Paddle, Food
import pygame

# Global variables
pygame.init()
surface = pygame.display.set_mode((1200, 800))


# Testing the Snake
def test_snake_creation():
    snake = Snake(surface, True)
    all_directions = [(0, 1), (0, -1), (-1, 0), (1, 0)]
    assert snake.get_head_position() == (600, 400)
    assert snake.get_direction() in all_directions
    assert snake.get_length() == 15

def test_turning_snake():
    snake = Snake(surface, True, True)
    snake.update_snake(True)
    assert snake.get_direction() == (1,0)
    assert snake.get_head_position() == (602, 400)

def test_eating_food():
    snake = Snake(surface, True)
    assert snake.get_length() == 15
    snake.set_length()
    assert snake.get_length() == 20

def test_game_over():
    snake = Snake(surface, True)
    tooHigh_x = snake.get_head_position()[0] + 1000
    tooHigh_y = snake.get_head_position()[1] + 1000
    assert snake.game_over(True, tooHigh_x) == True
    assert snake.game_over(True, 500, tooHigh_y) == True
    # isRunning false meaning the game has stopped
    snake = Snake(surface, False)
    assert snake.game_over() == True

# Testing the Ball
def test_ball_creation():
    ball = Ball(surface)
    assert ball.get_current_position() == (400,400)
    assert ball.get_score() == 0

def test_moving_ball():
    ball = Ball(surface)
    for i in range(0, 10):
        oldDirection = ball.get_current_position()
        ball.update_ball()
        pygame.display.flip()
        assert ball.get_current_position() != oldDirection

# Testing the Paddle
def test_paddle_creation():
    paddle = Paddle(surface)
    assert paddle.get_current_position() == (220,350)

def test_moving_paddle():
    paddle = Paddle(surface)
    for i in range(0, 10):
        oldPosition = paddle.get_current_position()
        paddle.update_paddle()
        pygame.display.flip()
        assert paddle.get_current_position() != oldPosition

# Testing the Food
def test_creating_food():
    food = Food(surface)
    assert food.get_food_location() != None

def test_cooking_new_food():
    food = Food(surface)
    for i in range(0, 10):
        oldPosition = food.get_food_location()
        food.update_food()
        pygame.display.flip()
        assert food.get_food_location() != oldPosition

    