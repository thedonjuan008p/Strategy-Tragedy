import pygame, sys
from pygame.locals import *
vec = pygame.math.Vector2

velocidad = 2
class Personaje:

    def __init__(self, PosX, PosY):
        self.Pos = vec(PosX,PosY)
        self.Vel = vec(2,0)
        self.Acc = vec(0,0)
        self.WalkCount = 4
        self.draw_quieto = self.get_image("personaje/personaje-principal.png", True)
        self.isJumping = False
        self.JumpCount = 10
        self.right = False
        self.left = False
        self.lastDir = "Right"

        #Carga de Sprites
        self.xixf = []
        for i in range(1,23):
            if i < 10:
              p = "0"+str(i)
            else:
                p = str(i)
            draw = self.get_image(f"personaje/corriendo/personaje-corriendo00{p}.png", True)
            self.xixf.append(draw)
        self.Rxixf = []
        for i in range(0,22):
            draw = pygame.transform.flip(self.xixf[i], True, False)
            self.Rxixf.append(draw)

    def get_image(self, filename, transparent=False, conv=False):
        try:
            image = pygame.image.load(filename)
        except pygame.error:
            raise SystemExit
        if transparent:
            color = image.get_at((0, 0))
            image.set_colorkey(color, RLEACCEL)
        if conv:
            image = image.convert()
        return image

    def teclado(self):

        self.Acc = vec(0,0.5)


        self.Acc.x += self.Vel.x * (-0.12)
        self.Vel.y += self.Acc.y
        self.Pos.y += self.Vel.y + 0.5*self.Acc.y
        

        teclado = pygame.key.get_pressed()

        if self.Pos.y > 566:
            self.Pos.y = 566

        if teclado[K_RIGHT] :
            self.Pos.x += velocidad
            #self.Acc.x+= 0.5
            self.right = True
            self.left = False
            self.lastDir = "Right"

        if teclado[K_LEFT] :
            self.Pos.x -= velocidad
            #self.Acc.x+= -0.5
            self.left = True
            self.right = False
            self.lastDir = "Left"
            
        if not (teclado[K_RIGHT] or teclado[K_LEFT]):
            self.right = False
            self.left = False

        if teclado[K_SPACE]:
            self.Vel.y = -12

    def movimiento(self, screen):


        if self.WalkCount + 1 >= 66:
            self.WalkCount = 0
        if self.right:
            screen.blit(self.xixf[self.WalkCount//3], (self.Pos.x, self.Pos.y))
            self.WalkCount += 2
        if self.left:
            screen.blit(self.Rxixf[self.WalkCount//3], (self.Pos.x, self.Pos.y))
            self.WalkCount += 2
        if (self.left or self.right) == False and self.lastDir == "Right":
            screen.blit(self.draw_quieto, (self.Pos.x, self.Pos.y) )
        if (self.left or self.right) == False and self.lastDir == "Left":
            screen.blit(pygame.transform.flip(self.draw_quieto,True, False), (self.Pos.x, self.Pos.y) )

        return