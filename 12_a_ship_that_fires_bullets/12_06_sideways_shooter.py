#sideways shooter

import pygame
import sys

pygame.init()


screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Sideways Shooter")


background_color = (0, 0, 225)
bullet_color = (255, 0, 0)


class Ship:
    def __init__(self, screen):
        self.screen = screen
        self.image = pygame.image.load("code_jam/media/spaceship.png")
        self.image = pygame.transform.scale(self.image, (60, 60))
        self.rect = self.image.get_rect()

    
        self.rect.left = 5
        self.rect.centery = screen.get_rect().centery

        self.speed = 5

    def move(self, keys):
        if keys[pygame.K_UP] and self.rect.top > 0:
            self.rect.y -= self.speed

        if keys[pygame.K_DOWN] and self.rect.bottom < 600:
            self.rect.y += self.speed

        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.speed

        if keys[pygame.K_RIGHT] and self.rect.right < 800:
            self.rect.x += self.speed        

        rotated_image = pygame.transform.rotate(self.image, 100 * (self.rect.centery - screen.get_rect().centery) / screen.get_rect().centery)

    def draw(self):
        self.screen.blit(self.image, self.rect)



class Bullet:
    def __init__(self, screen, ship):
        self.screen = screen
        self.rect = pygame.Rect(0, 0, 15, 5)
        self.image = pygame.image.load("code_jam/media/bullet.png")

        
        self.rect.midleft = ship.rect.midright

        self.speed = 5

    def move(self):
        self.rect.x += self.speed

    def draw(self):
        pygame.draw.rect(self.screen, bullet_color, self.rect)



ship = Ship(screen)
bullets = [Bullet(screen, ship)]  


while True:
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                new_bullet = Bullet(screen, ship)
                bullets.append(new_bullet)

    
    keys = pygame.key.get_pressed()
    ship.move(keys)

    
    for bullet in bullets[:]:
        bullet.move()

        
        if bullet.rect.left > screen.get_rect().right:
            bullets.remove(bullet)

    
    screen.fill(background_color)
    ship.draw()

    for bullet in bullets:
        bullet.draw()

    
    pygame.display.flip()
