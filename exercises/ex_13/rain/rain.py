import sys
import pygame
from random import randint

from rain_settings import Settings
from raindrop import Raindrop

class Rain:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()

        # self.screen = pygame.display.set_mode((1200, 800))
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Rain")

        self.raindrops = pygame.sprite.Group()

        self._create_rain()

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()
            self._update_rain()
            self._update_screen()
            self._check_disappearing_raindrops()
            # print(len(self.raindrops))
            self.clock.tick(60)

    def _check_events(self):
        """Respond to keypresses and mouse events."""
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    self._check_keydown_events(event)

    def _check_keydown_events(self, event):
        """Respond to keypresses."""
        if event.key == pygame.K_q or event.key == pygame.K_ESCAPE:
            sys.exit()

    def _create_rain(self):
        """Create the fleet of aliens."""
        # Create an alien and keep adding aliens until there's no room left.
        # Spacing between aliens is one alien width and one alien height.
        raindrop = Raindrop(self)
        raindrop_width, raindrop_height = raindrop.rect.size
        
        current_x, current_y = raindrop_width, raindrop_height

        while current_y < (self.settings.screen_height - 3 * raindrop_height):
            while current_x < (self.settings.screen_width - raindrop_width):
                self._create_raindrop(current_x, current_y)
                current_x += 2 * raindrop_width
            # Finished a row; reset x value, and increment y value.
            current_x = raindrop_width
            current_y += 2 * raindrop_height

    def _create_raindrop(self, x_position, y_position):
        """Create an alien and place it in the row."""
        new_raindrop = Raindrop(self)
        # new_raindrop.x = x_position
        new_raindrop.y = y_position
        ran = 20
        new_raindrop.rect.x = x_position + randint(-ran, ran)
        new_raindrop.rect.y = y_position + randint(-ran, ran)
        self.raindrops.add(new_raindrop)

    def _update_rain(self):
        self.raindrops.update()

    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        self.screen.fill(self.settings.bg_color)
        self.raindrops.draw(self.screen)
        pygame.display.flip()

    def _check_disappearing_raindrops(self):
        for raindrop in self.raindrops.sprites():
            if raindrop.y >= self.settings.screen_height:
                raindrop.y = -raindrop.rect.height
                raindrop.rect.y = raindrop.y

if __name__ == '__main__':
    # Make a game instance, and run the game.
    ai = Rain()
    ai.run_game()