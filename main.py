# main.py
import pygame
from settings import Settings
from gamestate import GameState

def main():
    pygame.init()
    pygame.display.set_caption("PySnake Game")
    settings = Settings()
    screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))
    game_state = GameState(settings)
    clock = pygame.time.Clock()

    while True:
        game_state.check_events()
        game_state.update_screen(screen)
        pygame.display.flip()
        clock.tick(15)

if __name__ == "__main__":
    main()
