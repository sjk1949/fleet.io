import pygame
from math import *
from vec import *
from fleet import *

(width,height) = (1000,600)

def posToScreen(pos):
    result = Vec()
    result.x = pos.x+width/2
    result.y = -pos.y+height/2
    return result

class Game:

    def __init__(self):
        # pygame setup
        pygame.init()
        self.screen = pygame.display.set_mode((width,height))
        self.clock = pygame.time.Clock()
        self.running = True
        #game content
        self.players = []
        self.render = []

    def run(self):
        while self.running:
            # poll for events
            # pygame.QUIT event means the user clicked X to close your window
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            # fill the screen with a color to wipe away anything from last frame
            self.screen.fill("skyblue")

            #Update
            for player in self.players:
                player.Update()
            for render in self.render:
                render.Update()

            # RENDER YOUR GAME HERE
            for render in self.render:
                self.screen.blit(render.newimage,(render.screenPos.x,render.screenPos.y))

            # flip() the display to put your work on screen
            pygame.display.flip()

            self.clock.tick(30)  # limits FPS to 60

        pygame.quit()

    pass

class Player:

    def __init__(self,craft):
        self.craft = craft

    def Update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            self.craft.P = self.craft.Pmax
            print("up")
        else:
            self.craft.P = 0
        if keys[pygame.K_LEFT]:
            self.craft.angle += 0.4
        if keys[pygame.K_RIGHT]:
            self.craft.angle -= 0.4
        self.craft.Update()

    pass

class Render:

    def __init__(self,object,image):
        self.object = object
        self.pos = self.object.pos
        self.angle = self.object.angle
        self.image = pygame.image.load(image)
        #图形相关
        self.screenPos = posToScreen(self.pos)
        self.length = 200#界面中图形长度
        width = self.image.get_height()
        length = self.image.get_width()
        self.width = self.length*width/length
        self.image = pygame.transform.smoothscale(self.image,(self.length,self.width))
        self.newimage = pygame.transform.rotate(self.image,self.angle)

    def Update(self):
        #图像更新
        self.pos = self.object.pos
        self.angle = self.object.angle
        self.screenPos = posToScreen(self.pos)
        self.newimage = pygame.transform.rotate(self.image,self.angle)

if __name__ == '__main__':
    game = Game()
    craft = Craft("Test",100000,2000,0,0)
    craftRender = Render(craft,"./picture/craft1.png")
    player = Player(craft)
    game.players.append(player)
    game.render.append(craftRender)
    game.run()