import pygame
from math import *
from vec import *
from fleet import *

(Width,Height) = (1000,600)

class Game:

    def __init__(self):
        # pygame setup
        pygame.init()
        self.screen = pygame.display.set_mode((Width,Height))
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

                if event.type == pygame.MOUSEWHEEL:
                    Render.scale += 0.02*event.y
                    if(Render.scale<Render.minScale):
                        Render.scale = Render.minScale
                    print(event.y,Render.scale)

            # fill the screen with a color to wipe away anything from last frame
            self.screen.fill("skyblue")

            #Update
            for player in self.players:
                player.Update()
            for render in self.render:
                render.Update()

            # RENDER YOUR GAME HERE
            for render in self.render:
                render.Render(self.screen)
                

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
        if(keys[pygame.K_w] or keys[pygame.K_UP]):
            self.craft.P = self.craft.Pmax
        else:
            self.craft.P = 0
        if(keys[pygame.K_a] or keys[pygame.K_LEFT]):
            self.craft.angle += 0.3
        if(keys[pygame.K_d] or keys[pygame.K_RIGHT]):
            self.craft.angle -= 0.3
        self.craft.Update()

    pass

class Render:
    minScale = 0.2
    scale = 1

    def __init__(self,object,image):
        self.object = object
        self.pos = self.object.pos
        self.angle = self.object.angle
        self.originImage = pygame.image.load(image)
        #图形相关
        self.screenPos = Render.posToScreen(self.pos)
        self.length = 200/Render.scale#界面中图形长度
        width = self.originImage.get_height()
        length = self.originImage.get_width()
        self.ratio = length/width
        self.image = pygame.transform.smoothscale(self.originImage,(self.length,self.width))
        self.newimage = pygame.transform.rotate(self.image,self.angle)
        self.rect = self.newimage.get_rect(center=(self.screenPos.x,self.screenPos.y))

    @property
    def width(self):
        return self.length/self.ratio

    def Update(self):
        #图像更新
        self.pos = self.object.pos
        self.angle = self.object.angle
        self.length = 200/Render.scale
        self.screenPos = Render.posToScreen(self.pos)
        self.image = pygame.transform.smoothscale(self.originImage,(self.length,self.width))
        self.newimage = pygame.transform.rotate(self.image,self.angle)
        self.rect = self.newimage.get_rect(center=(self.screenPos.x,self.screenPos.y))

    def Render(self,screen):
        screen.blit(self.newimage,self.rect)

    def posToScreen(pos):
        result = Vec()
        result.x = pos.x/Render.scale+Width/2
        result.y = -pos.y/Render.scale+Height/2
        return result

    pass

if __name__ == '__main__':
    game = Game()
    craft = Craft("Test",100000,1000,0,0)
    craft.render = Render(craft,"./picture/craft1.png")
    player = Player(craft)
    game.players.append(player)
    game.render.append(craft.render)
    game.run()