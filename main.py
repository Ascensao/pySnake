# main.py
import pygame
from settings import Settings
from gamestate import GameState

def main():
    pygame.init()
    pygame.display.set_caption("pySnake Game")
    settings = Settings()
    screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))
    game_state = GameState(settings)
    clock = pygame.time.Clock()

    while True:
        game_state.check_events()
        game_state.update_screen(screen)
        pygame.display.flip()
        if game_state.game_over:
            # Display "You Lost!" in red
            screen.fill(settings.bg_color)
            font = pygame.font.Font(None, 36)
            text = font.render("You Lost !", True, (255, 0, 0))
            text_rect = text.get_rect(center=(settings.screen_width // 2, settings.screen_height // 2))
            screen.blit(text, text_rect)
            pygame.display.flip()
            pygame.time.wait(1500)  # Wait for 1.5 seconds

            # Display countdown
            for i in range(3, 0, -1):
                screen.fill(settings.bg_color)
                text = font.render(f"Game starting in {i} ...", True, (255, 255, 255))
                text_rect = text.get_rect(center=(settings.screen_width // 2, settings.screen_height // 2))  # Recalculate text position
                screen.blit(text, text_rect)
                pygame.display.flip()
                pygame.time.wait(1000)
            game_state.reset()
        clock.tick(15)

if __name__ == "__main__":
    main()
