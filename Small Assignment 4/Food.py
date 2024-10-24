import pygame as pg
import timer
import random
from settings import clamp
from vector import Vector
from pygame.sprite import Sprite, Group

# Food class
class Food(Sprite):
    food_images = [pg.transform.rotozoom(pg.image.load(f'images/Food2{n}.png'), 0, 1.0) for n in
                             range(2)]
    def __init__(self, x, y, game, settings, screen):
        super().__init__()
        self.game = game
        self.screen = screen
        self.settings = settings
        self.image = pg.image.load('images/Food20.png')
        self.rect = self.image.get_rect(center=(x, y))
        self.posn = Vector(x, y)
        self.vel = Vector(0,0)
        self.timer = timer.Timer(image_list=Food.food_images, delay=200)

    def update(self):
        # Food doesnt need to move
        # x = self.rect.x + 2 * random.randint(-1, 1)
        # y = self.rect.y + 2 * random.randint(-1, 1)
        # self.rect.x = max(0, min(x, self.settings.screen_width - self.rect.width))
        # self.rect.y = max(0, min(y, self.settings.screen_height - self.rect.height))

        self.posn, self.rect = clamp(self.posn, self.rect, self.settings)
        self.draw()

    def draw(self):
        image = self.timer.image()
        rect = image.get_rect()
        rect.left, rect.top = self.rect.left, self.rect.top
        self.screen.blit(image, rect)
