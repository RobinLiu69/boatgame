import pygame
from boat import Boat
from setting import *
pygame.init()

def main():
    gameWindows = pygame.display.set_mode((display_width, display_height), pygame.FULLSCREEN)
    object = pygame.sprite.Group()
    Player = Boat(display_width/2, display_height/2, display_width/50/1.6, display_height/70, WHITE, object)
    object.add(Player)
    clock = pygame.time.Clock()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running=False
        keys=pygame.key.get_pressed()
        gameWindows.fill((0, 0, 0))
        object.draw(gameWindows)
        Player.move(keys)
        pygame.display.flip()
            
        clock.tick(60)

main()
pygame.quit()