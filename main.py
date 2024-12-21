import pygame
import sys
from player import Player
from  constants import *
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
def main():

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    #ITERABLE GROUP OBJECTS
    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updateable,drawable)
    Asteroid.containers = (asteroids,updateable,drawable)
    AsteroidField.containers = (updateable)
    Shot.containers = (updateable,drawable,shots)
    actual_player = Player(SCREEN_WIDTH/2,SCREEN_HEIGHT/2)
    asteroid_field = AsteroidField()
    dt = 0

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        screen.fill((0,0,0))

        for obj in updateable:
            obj.update(dt)

        for obj in asteroids:
            if obj.collision(actual_player):
                sys.exit("Game over!")
            for shot in shots:
                if obj.collision(shot):
                    pygame.sprite.Sprite.kill(shot)
                    obj.split()
                    #pygame.sprite.Sprite.kill(obj)

        for obj in drawable:
            obj.draw(screen)
        
        pygame.display.flip()
        dt = clock.tick(60)/1000

if __name__ == "__main__":
    main()