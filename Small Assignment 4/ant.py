import pygame as pg
import random
from vector import Vector
from settings import clamp
from pygame.sprite import Sprite, Group

# Ant class
class Ant(pg.sprite.Sprite):
    def __init__(self, x, y, game, settings, screen):
        super().__init__()
        self.game = game
        self.screen = screen
        self.settings = settings
        self.image = pg.image.load('images/Ship.png')

        self.last_time_dir_changed = pg.time.get_ticks()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.posn = Vector(x, y)
        self.last_x_vel = random.randint(-1, 1)
        self.last_y_vel = random.randint(-1, 1)
        self.last_changed = random.randint(0, 1) # used to simulate momentum
        self.vel = Vector(self.last_x_vel, self.last_y_vel)

        self.cargo = 0
        self.going_to_base = False

    def collect(self):
        self.image = pg.image.load('images/Ship_Powered_2.png')
        self.rect = self.image.get_rect()
        self.cargo += 1
        self.go_to_base()

    def go_to_base(self):
        self.last_x_vel = self.last_y_vel = 1
        self.going_to_base = True

    def collide_edge_boundary(self):
        screen_rect = self.screen.get_rect()
        return self.rect.right >= screen_rect.right - 20 or self.rect.left <= screen_rect.left

    def collide_bottom_or_top_boundary(self):
        screen_rect = self.screen.get_rect()
        return self.rect.bottom >= screen_rect.bottom - 20 or self.rect.top <= screen_rect.top

    def adjust_movement(self):
        if self.going_to_base:
            if self.posn.x == self.settings.screen_width/2:
                self.last_x_vel = 0
            if self.posn.y == self.settings.screen_height/2:
                self.last_y_vel = 0

        else:
            if pg.time.get_ticks() > self.last_time_dir_changed + 50:
                self.last_time_dir_changed = pg.time.get_ticks()
                if self.last_changed & random.randint(0, 1):
                    self.last_x_vel += random.randint(-1, 1)
                    self.last_changed = not self.last_changed
                else:
                    self.last_y_vel += random.randint(-1, 1)
                    self.last_changed = not self.last_changed

                if self.last_x_vel > 1:
                    self.last_x_vel = 1
                if self.last_x_vel < -1:
                    self.last_x_vel = -1

                if self.last_y_vel > 1:
                    self.last_y_vel = 1
                if self.last_y_vel < -1:
                    self.last_y_vel = -1


        if self.collide_edge_boundary():
            self.last_x_vel *= -1

        if self.collide_bottom_or_top_boundary():
            self.last_y_vel *= -1

        self.vel = Vector(self.last_x_vel, self.last_y_vel)

    def update(self):
        # Move the ant
        self.adjust_movement()

        self.posn += self.vel
        self.posn, self.rect = clamp(self.posn, self.rect, self.settings)
        self.draw()

    def draw(self):
        image = self.image
        rect = image.get_rect()
        rect.left, rect.top = self.rect.left, self.rect.top
        self.screen.blit(image, rect)

