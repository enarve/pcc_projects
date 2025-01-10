import sys
import pygame

from character import Character

class Game:

    def __init__(self):
        self.screen = pygame.display.set_mode((1200, 800))
        self.character = Character(self)

    def run(self):
        while True:
            self.screen.fill((65, 105, 225))
            self.character.blitme()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            pygame.display.flip()

if __name__ == '__main__':
    game = Game()
    game.run()