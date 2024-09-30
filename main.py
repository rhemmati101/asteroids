import pygame
from player import Player
from constants import *

def main():
    print("Starting asteroids!")

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    
    clock = pygame.time.Clock()
    dt = 0

    while True:
        # returns if window is closed
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        # update object positions
        player.update(dt)
        # draw to screen
        screen.fill("black")
        player.draw(screen)
        # print screen
        pygame.display.flip()

        dt = clock.tick(60)/1000





if __name__ == "__main__":
    main()
