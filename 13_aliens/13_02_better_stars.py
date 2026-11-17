# better stars

import pygame
import sys
import random


pygame.init()


screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Random Star Pattern")


star_image = pygame.image.load("code_jam/media/superstar.png")
star_image = pygame.transform.scale(star_image, (40, 40))


star_rect = star_image.get_rect()


stars = []


for i in range(30):
    x = random.randint(0, 760)
    y = random.randint(0, 560)

    star = star_rect.copy()
    star.x = x
    star.y = y

    stars.append(star)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    
    screen.fill((0, 0, 0))

    
    for star in stars:
        screen.blit(star_image, star)

    
    pygame.display.flip()
