# steady rain


import pygame
import sys

class Raindrop:
    def __init__(self, screen, x, y):
        self.screen = screen
        self.image = pygame.image.load("code_jam/media/raindrop.png")
        self.image = pygame.transform.scale(self.image, (30, 40))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = 3

    def fall(self):
        self.rect.y += self.speed

    def draw(self):
        self.screen.blit(self.image, self.rect)


pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Falling Raindrops")

raindrops = []

drop_width = 30
drop_height = 40
spacing = 20

columns = 800 // (drop_width + spacing)
rows = 600 // (drop_height + spacing)

# Create the rows of raindrops
for row in range(rows):
    for column in range(columns):
        x = column * (drop_width + spacing)
        y = row * (drop_height + spacing)

        raindrop = Raindrop(screen, x, y)
        raindrops.append(raindrop)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill((0, 0, 0))

    for raindrop in raindrops:
        raindrop.fall()


        if raindrop.rect.top > 600:
            raindrop.rect.y = -drop_height

        raindrop.draw()

    pygame.display.flip()