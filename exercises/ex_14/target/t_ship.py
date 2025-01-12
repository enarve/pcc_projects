import pygame

class Ship:
    """A class to manage the ship."""

    def __init__(self, ai_game):
        """Initialize the ship and set its starting position."""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # Load the ship image and get its rect.
        self.image = pygame.image.load('exercises/ex_14/target/new_ship.bmp')
        self.rect = self.image.get_rect()

        self.ship_speed = 10

        # Start each new ship at the bottom center of the screen.
        self.rect.midleft = self.screen_rect.midleft

        # Store a float for the ship's exact horizontal position.
        self.y = float(self.rect.y)

        # Movement flag; start with a ship that's not moving
        self.moving_down = False
        self.moving_up = False

    def update(self):
        """Update the ship's position based on the movement flag."""
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.ship_speed
        if self.moving_up and self.rect.top > 0:
            self.y -= self.ship_speed

        # Update rect object from self.y
        self.rect.y = self.y

    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        """Center the ship on the screen."""
        self.rect.midleft = self.screen_rect.midleft
        self.y = float(self.rect.y)