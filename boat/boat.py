from calculate import * 
from setting import * 
import pygame

class Boat(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, color, group):
        super().__init__(group)
        self.x = x
        self.y = y
        self.xv = 0
        self.yv = 0
        self.rotationVector = 0
        self.width = width
        self.height = height
        self.health = 10000
        self.power = 50
        self.maxStorge = 50
        self.storge = []
        self.speed = 50
        self.rotation = 90
        self.imageOriginal = pygame.Surface((self.width, self.height))
        self.imageOriginal.set_colorkey(BLACK)
        self.imageOriginal.fill(color)
        self.image = self.imageOriginal.copy()
        self.rect = self.imageOriginal.get_rect(center = (self.x, self.y))
        self.mass = self.health
        
    def move(self, keys):
        speed = 0
        if keys[pygame.K_a] and self.rotationVector <= 5:
            self.rotationVector += 0.1
        if keys[pygame.K_d] and self.rotationVector >= -5:
            self.rotationVector -= 0.1
        if keys[pygame.K_w]:
            speed = self.speed/100
        self.rotation += self.rotationVector
        self.rotate()
        V, _ = xyVelocityToOneDerectionVelocity(self.xv, self.yv)
        V += speed
        self.xv, self.yv = oneDerectionVelocityToxyVelocity(V, -self.rotation)
        self.x += self.xv
        self.y += self.yv
        self.rect = self.imageOriginal.get_rect(center = (self.x, self.y))
        return True

    def rotate(self):
        self.rotation = self.rotation%360
        self.image = pygame.transform.rotate(self.imageOriginal,self.rotation)
        # self.mask = pygame.mask.from_surface(self.image)

        center = self.rect.center
        self.rect = self.image.get_rect(center = (self.x, self.y))
        self.rect.center = center
         
        return True