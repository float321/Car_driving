import pygame
import os
import sys


pygame.init()
size = width, height = 600, 95
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Car_drive')


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    # если файл не существует, то выходим
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    if colorkey is not None:
        image = image.convert()
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image


class Car(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__(all_sprites)

        self.image = load_image('car2.png')
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0
        self.flag = True

    def update(self, *args, **kwargs):
        if self.flag:
            self.rect.x += 1
            if self.rect.x == 450:
                self.flag = False
                self.image = pygame.transform.flip(self.image, True, False)
        else:
            self.rect.x -= 1
            if self.rect.x == 0:
                self.flag = True
                self.image = pygame.transform.flip(self.image, True, False)


if __name__ == '__main__':

    running = True
    all_sprites = pygame.sprite.Group()
    clock = pygame.time.Clock()
    Car()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill('White')

        all_sprites.update()
        all_sprites.draw(screen)

        clock.tick(120)
        pygame.display.flip()
    pygame.quit()
