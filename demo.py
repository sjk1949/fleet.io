import pygame
from math import *
from vec import *
from fleet import *

class Game:

    def __init__(self):
        # pygame setup
        pygame.init()
        self.screen = pygame.display.set_mode((1000, 600))
        self.clock = pygame.time.Clock()
        self.running = True

    def run(self):
        while self.running:
            # poll for events
            # pygame.QUIT event means the user clicked X to close your window
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            # fill the screen with a color to wipe away anything from last frame
            self.screen.fill("skyblue")

            # RENDER YOUR GAME HERE

            # flip() the display to put your work on screen
            pygame.display.flip()

            self.clock.tick(60)  # limits FPS to 60

        pygame.quit()

    pass

class Player:

    def __init__(self):
        self.craft = Craft("Test",1000,0,0,0)

    def Update(self):
        keys = pygame.key.get_pressed()
        if keys[K_UP]:
            self.craft.P = 100
        else:
            self.craft.P = 0
        if keys[K_LEFT]:
            self.craft.angle += 1
        if keys[K_RIGHT]:
            self.craft.angle -= 1

    pass

if __name__ == '__main__':
    game = Game()
    game.run()