import pygame
from pygame.sprite import Sprite

class Raindrop(Sprite):
    """A class to represent a single raindrop in the rain."""

    def __init__(self, ai_game):
        """Initialize the raindrop and set its starting position."""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        # Load the raindrop image and set its rect attribute.
        self.image = pygame.image.load('exercises/ex_13/rain/raindrop.bmp')
        self.image = pygame.transform.scale(self.image, (40, 40)) 
        self.rect = self.image.get_rect()

        # Start each new raindrop near the top left of the screen.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the raindrop's exact horizontal position.
        self.y = float(self.rect.y)

    def update(self):
        """Move the raindrop down."""
        self.y += self.settings.raindrop_speed
        self.rect.y = self.y