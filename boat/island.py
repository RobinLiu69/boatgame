import pygame

class Island(pygame.sprite.Sprite):
    def __init__(self, name, x, y, width, height):
        self.name = name
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.image = pygame.Surface((self.width, self.height))


