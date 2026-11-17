# keys

import pygame
import sys

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Keyboard Events")

while True:
    for event in pygame.event.get():

    
        if event.type == pygame.KEYDOWN:
            print(event.key)

        if event.type == pygame.KEYUP:
            print(event.key)      

    
        elif event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()