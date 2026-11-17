# sideways shooter part 2

import pygame
import sys

pygame.init()


screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Sideways Shooter")


BLACK = (0, 0, 0)
WHITE = (255, 255, 255)


class Ship:
    def __init__(self):
        self.image = pygame.image.load("code_jam/media/spaceship.png")
        self.image = pygame.transform.scale(self.image, (60, 60))
        self.rect = self.image.get_rect()
        self.rect.left = 20
        self.rect.centery = 300
        self.speed = 5
        self.moving_up = False
        self.moving_down = False

    def update(self):
        if self.moving_up and self.rect.top > 0:
            self.rect.y -= self.speed

        if self.moving_down and self.rect.bottom < 600:
            self.rect.y += self.speed

    def draw(self):
        screen.blit(self.image, self.rect)



class Bullet(pygame.sprite.Sprite):
    def __init__(self, ship):
        super().__init__()
        self.image = pygame.Surface((15, 5))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.left = ship.rect.right
        self.rect.centery = ship.rect.centery
        self.speed = 8

    def update(self):
        self.rect.x += self.speed

        
        if self.rect.left > 800:
            self.kill()



class Alien(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("code_jam/media/alien.png")
        self.image = pygame.transform.scale(self.image, (40, 40))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = 2

    def update(self):
        self.rect.x -= self.speed



ship = Ship()
bullets = pygame.sprite.Group()
aliens = pygame.sprite.Group()


for row in range(10):
    for column in range(5):
        x = 450 + column * 65
        y = 30 + row * 55
        alien = Alien(60, 60)
        aliens.add(alien)


while True:

    
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                ship.moving_up = True
            elif event.key == pygame.K_DOWN:
                ship.moving_down = True
            elif event.key == pygame.K_SPACE:
                bullet = Bullet(ship)
                bullets.add(bullet)

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                ship.moving_up = False
            elif event.key == pygame.K_DOWN:
                ship.moving_down = False

    
    ship.update()
    bullets.update()
    aliens.update()

    
    pygame.sprite.groupcollide(
        bullets, aliens, True, True
    )


    for alien in aliens:
        if alien.rect.left <= ship.rect.right:
            print("Game Over!")
            pygame.quit()
            sys.exit()


    screen.fill(BLACK)

    ship.draw()
    bullets.draw(screen)
    aliens.draw(screen)

    pygame.display.flip()
