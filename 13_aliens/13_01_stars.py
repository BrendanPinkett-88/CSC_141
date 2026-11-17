# stars

import pygame
import sys

class Star:
    def __init__(self, screen, x, y):
        self.screen = screen
        self.image = pygame.image.load("code_jam/media/superstar.png")
        self.image = pygame.transform.scale(self.image, (40, 40))
        self.rect = self.image.get_rect()

        self.rect.x = x
        self.rect.y = y

    def draw(self):
        self.screen.blit(self.image, self.rect)


pygame.init()


screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Grid of Stars")


stars = []


star_width = 40
star_height = 40
spacing = 20


columns = 800 // (star_width + spacing)
rows = 600 // (star_height + spacing)


for row in range(rows):
    for column in range(columns):
        x = column * (star_width + spacing)
        y = row * (star_height + spacing)

        star = Star(screen, x, y)
        stars.append(star)



while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

   
    screen.fill((0, 0, 0))

    
    for star in stars:
        star.draw()

    
    
    pygame.display.flip()