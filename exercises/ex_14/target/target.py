import pygame

class Target:

    def __init__(self, game):
        self.screen = game.screen
        self.rect = pygame.Rect(0, 0, 100, 100)
        self.rect.topright = self.screen.get_rect().topright
        self.rect.x -= self.rect.width
        self.rect.y += self.rect.height
        self.direction = 1
        self.settings = game.settings

    def draw(self):
        pygame.draw.rect(self.screen, (200, 200, 200), self.rect)

    def update(self):
        self.rect.y += self.direction * self.settings.target_speed

    def hit_react(self):
        if self.rect.height == 100:
            self.rect.width = 50
            self.rect.height = 50
        else:
            self.rect.width = 100
            self.rect.height = 100

    def reset(self):
        self.rect.width = 100
        self.rect.height = 100