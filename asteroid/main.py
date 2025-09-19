import pygame
from player import Player
from constants import *





pygame.init()

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    updatable = pygame.sprite.Group()
    drawables = pygame.sprite.Group()

    Player.containers = (updatable, drawables)

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    clock = pygame.time.Clock()

    dt = 0

    player = Player(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)



    while True:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        

        screen.fill((0, 0, 0))
        
        updatable.update(dt)
        for sprite in drawables:
            sprite.draw(screen)
        
        pygame.display.flip()
        dt = clock.tick(60) / 1000  # Limit to 60 FPS and get delta time in seconds
 



if __name__ == "__main__":
    main()
