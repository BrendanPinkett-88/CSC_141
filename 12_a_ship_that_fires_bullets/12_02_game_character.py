import pygame
import sys

class GameCharacter:
    def __init__(self, screen):
        self.screen = screen

    
        self.image = pygame.image.load("code_jam/media/spaceship.png")


        self.rect = self.image.get_rect()


        self.rect.center = screen.get_rect().center

    def draw_character(self):
        self.screen.blit(self.image, self.rect)


pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Game Character")

background_color = (0, 0, 255)


character = GameCharacter(screen)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill(background_color)

    character.draw_character()

    pygame.display.flip()