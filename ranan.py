import pygame
import random
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 600

SNAKE_SIZE = 20
SNAKE_SPEED = 20

FOOD_SIZE = 20
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

class Snake:
    def __init__(self):
        self.body = [(0, 0)]
        self.direction = "right"

    def move(self):
        if self.direction == "right":
            new_head = (self.body[0][0] + SNAKE_SPEED, self.body[0][1])
        elif self.direction == "left":
            new_head = (self.body[0][0] - SNAKE_SPEED, self.body[0][1])
        elif self.direction == "up":
            new_head = (self.body[0][0], self.body[0][1] - SNAKE_SPEED)
        elif self.direction == "down":
            new_head = (self.body[0][0], self.body[0][1] + SNAKE_SPEED)
        self.body.insert(0, new_head)
        self.body.pop()

class Food:
    def __init__(self):
        self.x = random.randrange(0, WINDOW_WIDTH - FOOD_SIZE, FOOD_SIZE)
        self.y = random.randrange(0, WINDOW_HEIGHT - FOOD_SIZE, FOOD_SIZE)

    def draw(self, surface):
        pygame.draw.rect(surface, RED, (self.x, self.y, FOOD_SIZE, FOOD_SIZE))





