import sys
import pygame

class Keys:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()
        self.clock = pygame.time.Clock()

        self.screen = pygame.display.set_mode((400, 200))
        pygame.display.set_caption("Keys")

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()
            self._update_screen()
            self.clock.tick(60)

    def _check_events(self):
        """Respond to keypresses and mouse events."""
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    print(event)

    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        # self.screen.fill((0, 0, 0))
        pygame.display.flip()

if __name__ == '__main__':
    # Make a game instance, and run the game.
    game = Keys()
    game.run_game()