# code_jam


import pygame


pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((640, 480))
my_image = pygame.image.load("code_jam/media/basketball.png")
width = my_image.get_rect().width
height = my_image.get_rect().height


'''
my_image = pygame.transform.scale(my_image, (100, 100))
my_image = pygame.transform.rotate(my_image, 45)
my_image = pygame.transform.flip(my_image, True, False)
my_image = pygame.transform.rotozoom(my_image, 45, 1.5)
my_image = pygame.transform.smoothscale(my_image, (200, 200))
my_image = pygame.transform.scale2x(my_image)
my_image = pygame.transform.chop(my_image, (50, 50, 50, 50))
my_image = pygame.transform.laplacian(my_image)
my_image = pygame.transform.threshold(my_image, my_image, (0, 0, 0), (255, 255, 255), (255, 255, 255), 1)
'''




running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255, 255, 0))
    screen.blit(my_image, (0,0))
    rotated_image = pygame.transform.rotate(my_image, 45)
    screen.blit(rotated_image, (width//2, height//2))
    rotated_image = pygame.transform.rotate(my_image, 90)
    screen.blit(rotated_image, (width//2, height//2))
    rotated_image = pygame.transform.rotate(my_image, 135)
    screen.blit(rotated_image, (width//2, height//2))
    rotated_image = pygame.transform.rotate(my_image, 180)
    screen.blit(rotated_image, (width//2, height//2))
    pygame.display.flip()
    clock.tick(30)

    pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()


image = pygame.image.load("code_jam/media/basketball.png").convert()


rotated_image = pygame.transform.rotate(image, 180)


screen.fill((0, 0, 0))
screen.blit(rotated_image, (200, 200))
pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    clock.tick(60)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        rotated_image = pygame.transform.rotate(image, 90)
        screen.fill((0, 0, 0))
        screen.blit(rotated_image, (200, 200))
        pygame.display.flip()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT]:
        rotated_image = pygame.transform.rotate(image, -90)
        screen.fill((0, 0, 0))
        screen.blit(rotated_image, (200, 200))
        pygame.display.flip()    

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        rotated_image = pygame.transform.rotate(image, 180)
        screen.fill((0, 0, 0))
        screen.blit(rotated_image, (200, 200))
        pygame.display.flip()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_DOWN]:
        rotated_image = pygame.transform.rotate(image, 0)
        screen.fill((0, 0, 0))
        screen.blit(rotated_image, (200, 200))
        pygame.display.flip()        
    
        