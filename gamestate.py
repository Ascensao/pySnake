# gamestate.py
import pygame
import sys
from snake import Snake
from food import Food

class GameState:
    def __init__(self, settings):
        self.settings = settings
        self.snake = Snake()
        self.food = Food()

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.snake.direction = 'up'
                elif event.key == pygame.K_DOWN:
                    self.snake.direction = 'down'
                elif event.key == pygame.K_LEFT:
                    self.snake.direction = 'left'
                elif event.key == pygame.K_RIGHT:
                    self.snake.direction = 'right'

    def update_screen(self, screen):
        self.snake.move()
        if self.snake.segments[0].colliderect(self.food.rect):
            self.snake.grow()
            self.food = Food()
        screen.fill(self.settings.bg_color)
        self.snake.draw(screen)
        self.food.draw(screen)
