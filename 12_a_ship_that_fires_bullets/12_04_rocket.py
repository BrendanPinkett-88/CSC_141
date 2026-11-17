# rocket

import pygame
import sys

class Rocket:
    def __init__(self, screen):
        self.screen = screen

        
        self.image = pygame.image.load("code_jam/media/spaceship.png")
        self.rect = self.image.get_rect()

        
        self.rect.center = screen.get_rect().center

        
        self.speed = 5

    def move(self, keys):
        # Move left
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.speed

        # Move right
        if keys[pygame.K_RIGHT] and self.rect.right < 800:
            self.rect.x += self.speed

        # Move up
        if keys[pygame.K_UP] and self.rect.top > 0:
            self.rect.y -= self.speed

        # Move down
        if keys[pygame.K_DOWN] and self.rect.bottom < 600:
            self.rect.y += self.speed

    def draw_rocket(self):
        self.screen.blit(self.image, self.rect)



pygame.init()


screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Rocket Game")


background_color = (0, 0, 0)


rocket = Rocket(screen)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    
    keys = pygame.key.get_pressed()

    
    rocket.move(keys)

    
    screen.fill(background_color)
    rocket.draw_rocket()

    
    pygame.display.flip()