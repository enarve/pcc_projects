import pygame
import sys

from t_button import Button
from target import Target
from t_ship import Ship
from t_bullet import Bullet

class TargetPractice:

    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Target")

        self.target = Target(self)
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()

        # Start Alien Invasion in an inactive state.
        self.game_active = False
        
        # Make the Play button.
        self.play_button = Button(self, "Play")

        self.hit_stats = 0

    def run(self):
        while True:
            self._check_events()
            if self.game_active:
                self.ship.update()
                self._update_bullets()
                self._update_target()
            self._update_screen()
            self.clock.tick(60)

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q or event.key == pygame.K_ESCAPE:
                    sys.exit()
                elif event.key == pygame.K_p:
                    self._start_game()
                elif event.key == pygame.K_DOWN:
                    self.ship.moving_down = True
                elif event.key == pygame.K_UP:
                    self.ship.moving_up = True
                elif event.key == pygame.K_SPACE:
                    self._fire_bullet()
            elif event.type == pygame.KEYUP:
                    self._check_keyup_events(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    self._check_play_button(mouse_pos)

    def _check_play_button(self, mouse_pos):
        """Start a new game when the player clicks Play."""
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.game_active:
            self._start_game()

    def _start_game(self):
        self.hit_stats = 0
        self.game_active = True
        self.bullets.empty()
        self.ship.center_ship()
        # Hide the mouse cursor.
        pygame.mouse.set_visible(False)

    def _end_game(self):
        self.game_active = False
        pygame.mouse.set_visible(True)

    def _check_keyup_events(self, event):
        """Respond to key releases."""
        if event.key == pygame.K_DOWN:
            self.ship.moving_down = False
        elif event.key == pygame.K_UP:
            self.ship.moving_up = False

    def _update_target(self):
        if self.target.rect.y <= 0 or self.target.rect.y + self.target.rect.height >= self.screen.get_height():
            self.target.direction *= -1
        self.target.update()

    def _fire_bullet(self):
        """Create a new bullet and add it to the bullets group."""
        if len(self.bullets) < 100 :
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        """Update position of bullets and get rid of old bullets."""
        # Update bullet positions.
        self.bullets.update()
        # Get rid of bullets that have disappeared.
        for bullet in self.bullets.copy():
            if bullet.rect.right >= self.screen.get_rect().width:
                self.bullets.remove(bullet)
                self.hit_stats += 1
                # print(len(self.bullets))
        self._check_bullet_alien_collisions()
        if self.hit_stats >= 3:
            self._end_game()

    def _check_bullet_alien_collisions(self):
        """Respond to bullet-alien collisions."""
        # Remove any bullets and aliens that have collided.
        collisions = pygame.sprite.spritecollideany(self.target, self.bullets)
        if collisions:
            self.target.hit_react()

    def _update_screen(self):
        self.screen.fill((0, 0, 0))
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.ship.blitme()
        self.target.draw()

        # Draw the play button if the game is inactive.
        if not self.game_active:
            self.play_button.draw_button()

        pygame.display.flip()

if __name__ == '__main__':
    tp = TargetPractice()
    tp.run()