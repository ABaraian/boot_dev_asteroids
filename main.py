import pygame
import sys
from player import Player
from  constants import *
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    

    Player.containers = (updateable,drawable)
    Asteroid.containers = (asteroids,updateable,drawable)
    AsteroidField.containers = (updateable)
    
    actual_player = Player(SCREEN_WIDTH/2,SCREEN_HEIGHT/2)
    asteroid_field = AsteroidField()
    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0,0,0))

        for thing in updateable:
            thing.update(dt)
        for thing in asteroids:
            if thing.collision(actual_player):
                sys.exit("Game over!")
        for thing in drawable:
            thing.draw(screen)
        
        pygame.display.flip()
        dt = clock.tick(60)/1000

if __name__ == "__main__":
    main()