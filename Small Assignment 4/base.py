import pygame as pg
from vector import Vector
from settings import clamp

class Base(pg.sprite.Sprite):

    def __init__(self, x, y, game, settings, screen):
        super().__init__()
        self.image = pg.image.load('images/k_u.png')
        self.rect = self.image.get_rect()
        self.vel = Vector(0, 0)
        self.game = game
        self.screen = screen
        self.settings = settings

        self.last_time_dir_changed = pg.time.get_ticks()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.posn = Vector(x, y)
        self.vel = Vector(0,0)

    def update(self):
        # Move the ant

        self.posn += self.vel
        self.posn, self.rect = clamp(self.posn, self.rect, self.settings)
        self.draw()

    def draw(self):
        image = self.image
        rect = image.get_rect()
        rect.left, rect.top = self.rect.left, self.rect.top
        self.screen.blit(image, rect)


