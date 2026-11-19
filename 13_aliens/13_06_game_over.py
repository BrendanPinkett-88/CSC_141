# game over


import pygame
import sys

pygame.init()


screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Sideways Shooter")

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)


ship_hits = 0   
alien_ship_hits = 0
max_hits = 3


class Ship:
    def __init__(self):
        self.clock = pygame.time.Clock()
        self.image = pygame.image.load("code_jam/media/spaceship.png")
        self.image = pygame.transform.scale(self.image, (60, 60))
        self.rect = self.image.get_rect()
        self.rect.left = 20
        self.rect.centery = 300
        self.speed = 5
        self.moving_up = False
        self.moving_down = False
        self.clock.tick(60)

    def update(self):
        if self.moving_up and self.rect.top > 0:
            self.rect.y -= self.speed
        if self.moving_down and self.rect.bottom < 600:
            self.rect.y += self.speed
        self.clock.tick(60)

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
        aliens.add(Alien(x, y))



font = pygame.font.SysFont(None, 30)

def show_stats():
    ship_text = font.render(
        f"Ship Hits: {ship_hits}", True, WHITE
    )
    alien_text = font.render(
        f"Aliens Hitting Ship: {alien_ship_hits}",
        True, WHITE
    )
    point_text = font.render(
        f"shooting aliens: {len(aliens)}", True, WHITE
    )
    screen.blit(ship_text, (10, 10))
    screen.blit(alien_text, (10, 40))
    screen.blit(point_text, (10, 70))



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
                bullets.add(Bullet(ship))

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

    
    hit_aliens = pygame.sprite.spritecollide(
        ship, aliens, True
    )

    if hit_aliens:
        alien_ship_hits += len(hit_aliens)
        ship_hits += len(hit_aliens)


    if ship_hits >= max_hits:
        print("Game Over! The ship was hit 3 times.")
        pygame.quit()
        sys.exit()

    
    screen.fill(BLACK)

    ship.draw()
    bullets.draw(screen)
    aliens.draw(screen)
    show_stats()
    pygame.display.flip()
