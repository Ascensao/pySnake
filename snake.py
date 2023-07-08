# snake.py
import pygame
from pygame import Rect
from settings import Settings

class Snake:
    def __init__(self):
        self.settings = Settings()
        self.length = 1
        self.segments = [Rect(self.settings.screen_width // 2, self.settings.screen_height // 2, self.settings.snake_size, self.settings.snake_size)]
        self.direction = 'right'

    def move(self):
        head = self.segments[0].copy()
        if self.direction == 'right':
            head.move_ip(self.settings.snake_speed, 0)
        elif self.direction == 'left':
            head.move_ip(-self.settings.snake_speed, 0)
        elif self.direction == 'up':
            head.move_ip(0, -self.settings.snake_speed)
        elif self.direction == 'down':
            head.move_ip(0, self.settings.snake_speed)
        self.segments.insert(0, head)
        if len(self.segments) > self.length:
            self.segments.pop()

    def grow(self):
        self.length += 1

    def draw(self, screen):
        for segment in self.segments:
            pygame.draw.rect(screen, self.settings.snake_color, segment)
