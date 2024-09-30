import pygame
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
from constants import *

def main():
    print("Starting asteroids!")

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = (updatable)
    Shot.containers = (updatable, drawable, shots)
    
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    asteroid_field = AsteroidField()

    dt = 0

    while True:   # lol
        # returns if window is closed
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        # update object positions
        for obj in updatable:
            obj.update(dt)
        
        # collision detection
        for asteroid in asteroids:
            if asteroid.collides_with(player):
                print("Game over!")
                return
            for shot in shots:
                if asteroid.collides_with(shot):
                    asteroid.split()
                    shot.kill()

        # draw to screen
        screen.fill("black")
        for obj in drawable:
            obj.draw(screen)
        # print screen
        pygame.display.flip()

        dt = clock.tick(60)/1000



if __name__ == "__main__":
    main()
