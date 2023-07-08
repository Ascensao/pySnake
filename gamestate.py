import pygame
import sys
from snake import Snake
from food import Food

class GameState:
    def __init__(self, settings):
        self.settings = settings
        self.snake = Snake()
        self.food = Food()
        self.game_over = False

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
        for segment in self.snake.segments[1:]:  # Check for collision with self
            if self.snake.segments[0].colliderect(segment):
                self.game_over = True  # Set game over to True if collision with self
        screen.fill(self.settings.bg_color)
        self.snake.draw(screen)
        self.food.draw(screen)
        self.draw_score(screen)
        if self.game_over:
            font = pygame.font.Font(None, 36)
            text = font.render("You Lost", True, (255, 255, 255))
            text_rect = text.get_rect(center=(self.settings.screen_width // 2, self.settings.screen_height // 2))
            screen.blit(text, text_rect)

    def draw_score(self, screen): 
        font = pygame.font.Font(None, 36)
        score = self.snake.length - 1  # Calculate score as snake length - 1
        text = font.render(f"Score: {score}", True, (255, 255, 255))
        screen.blit(text, (self.settings.screen_width - 120, 20))  # Display score in the top right corner

    def reset(self):
        self.snake.reset()
        self.food.reset()
        self.game_over = False
