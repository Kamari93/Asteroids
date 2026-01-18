import pygame
import sys
from logger import log_event
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from logger import log_state
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    # get a new instance of GUI window:
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    updatable = pygame.sprite.Group() # Group class for managing updates
    drawable = pygame.sprite.Group() # Group class for managing drawing
    asteroids = pygame.sprite.Group() # Group class for managing asteroids
    shots = pygame.sprite.Group() # Group class for managing shots
    # This ensures that every instance of the below classes are automatically added to the above groups upon creation.
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Player.containers = (updatable, drawable)
    Shot.containers = (shots, updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()
    print(f'Starting Asteroids with pygame version: {pygame.version.ver}')
    print(f'Screen width: {SCREEN_WIDTH}')
    print(f'Screen height: {SCREEN_HEIGHT}')
    game = True
    clock = pygame.time.Clock()
    dt = 0
    while game:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        # player.draw(screen)
        for shape in drawable:
            shape.draw(screen)
        # player.update(dt)
        updatable.update(dt)
        for asteroid in asteroids:
            if asteroid.collides_with(player):
                log_event("player_hit")
                print("Game over!")
                sys.exit()
        for asteroid in asteroids:
            for shot in shots:
                if asteroid.collides_with(shot):
                    log_event("asteroid_shot")
                    # asteroid.kill()
                    asteroid.split()
                    shot.kill()
        pygame.display.flip()
        delta_time = clock.tick(60)
        convert_to_secs = delta_time / 1000
        dt = convert_to_secs
        # print(dt)

if __name__ == "__main__":
    main()
