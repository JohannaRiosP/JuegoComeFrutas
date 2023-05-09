import pygame, random


class Comelon(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("hambriento.jpg").convert()
        self.image.set_colorkey(Black)
        self.rect = self.image.get_rect()

    def update(self):
        self.rect.y += 1
        if self.rect.y > 600:
            self.rect.y = -10
            self.rect.x = random.randrange(800)


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("salvador.jpg").convert()
        self.image.set_colorkey(Black)
        self.rect = self.image.get_rect()

    def update(self):
        mouse_pos = pygame.mouse.get_pos()
        player.rect.x = mouse_pos[0]
        player.rect.y = 400


class Laser(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("espada-laser.jpg").convert()
        self.image.set_colorkey(Black)
        self.rect = self.image.get_rect()

    def update(self):
        # self.rect.y -= 5
        mouse_pos = pygame.mouse.get_pos()
        laser.rect.x = mouse_pos[0]
        laser.rect.y = 350


White = (255, 255, 255)
Black = (0, 0, 0)

pygame.init()

screen = pygame.display.set_mode([800, 500])
clock = pygame.time.Clock()

done = False
score = 0
background = pygame.image.load("tierra_frutal.jpg").convert()

all_sprites_list = pygame.sprite.Group()
comelon_list = pygame.sprite.Group()
laser_list = pygame.sprite.Group()

for i in range(30):
    comelon = Comelon()
    comelon.rect.x = random.randrange(880)
    comelon.rect.y = random.randrange(450)

    comelon_list.add(comelon)
    all_sprites_list.add(comelon)

player = Player()
all_sprites_list.add(player)

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            laser = Laser()
            laser.rect.x = player.rect.x + 45
            laser.rect.x = player.rect.x - 20
            all_sprites_list.add(laser)
            laser_list.add(laser)

    all_sprites_list.update()

    for laser in laser_list:
        comelon_hit_list = pygame.sprite.spritecollide(laser, comelon_list, True)
        for comelon in comelon_hit_list:
            all_sprites_list.remove(laser)
            laser_list.remove(laser)
            score += 1
            print(score)
        if laser.rect.y < -10:
            all_sprites_list.remove(laser)
            laser_list.remove(laser)
    screen.blit(background, [0, 0])
    all_sprites_list.draw(screen)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()