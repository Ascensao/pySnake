# food.py
import pygame
from pygame import Rect
from settings import Settings
import random

class Food:
    def __init__(self):
        self.settings = Settings()
        self.rect = self.place_food()

    def place_food(self):
        return Rect(random.randint(0, self.settings.screen_width - self.settings.food_size),
                    random.randint(0, self.settings.screen_height - self.settings.food_size),
                    self.settings.food_size, self.settings.food_size)

    def draw(self, screen):
        pygame.draw.rect(screen, self.settings.food_color, self.rect)

    def reset(self):
        self.rect = self.place_food()
