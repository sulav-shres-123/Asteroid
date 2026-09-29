import pygame
from constants import *
from logger import log_state
from player import *
from asteroid import * 
from asteroidfield import *
from logger import log_event
import sys
from shot import *


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    print(f'Starting Asteroids with pygame version: {pygame.version.ver}')
    print(f'Screen width: {SCREEN_WIDTH}')
    print(f'Screen height: {SCREEN_HEIGHT}') 

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group() 

    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2) 
    clock = pygame.time.Clock() 
    dt = 0.0

    asteroids = pygame.sprite.Group()
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    asteroidfield = AsteroidField()
    
    shots = pygame.sprite.Group() 
    Shot.containers = (shots, drawable, updatable)

    while True: 
        log_state()
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT: 
                return 

        updatable.update(dt)
        for j in asteroids: 
            if j.collides_with(player) == True: 
                log_event("player_hit")
                print("Game over!")
                sys.exit()
        screen.fill("black")
        #player.draw(screen)
        for i in drawable:
            i.draw(screen)
        pygame.display.flip() 
        dt = clock.tick(60)/1000
        #player.update(dt)
if __name__ == "__main__":
    main()
