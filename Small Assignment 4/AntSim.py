# Slightly modified example for Ant Simulation
# created by Generative AI (Google)

"""
Instructions for installing Pygame: https://www.pygame.org/wiki/GettingStarted

Overview:
- Imports: Import necessary libraries (Pygame for graphics and random for ant movement).
- Initialization: Initialize Pygame, set up the game window, and define colors.
- Ant class: Create an Ant class that inherits from pygame.sprite.Sprite.
             This class defines the ant's appearance, movement, and behavior.
- Create ants: Create a group of ants and initialize their positions randomly.
- Game loop: The main game loop handles events, updates the ants' positions, and
             draws them on the screen.

Ideas for Enhancement:
- Food: Add food sources that ants can collect and bring back to a nest.
- Pheromones: Implement pheromone trails that ants follow to find food and the nest.
- Different ant types: Create different types of ants with specialized roles (e.g., workers, soldiers).
- Obstacles: Add obstacles that ants must navigate around.
- Improved movement: Make the ant movement more realistic using steering behaviors or other algorithms.
"""

import pygame
import random
import settings
import ant
import Food
import base
#
# # Initialize Pygame
# pygame.init()
#
# # Screen dimensions
# screen_width = 800
# screen_height = 600
# screen = pygame.display.set_mode((screen_width, screen_height))
# pygame.display.set_caption("Ant Simulation")

# Colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)

class AntSim:
    def __init__(self):
        pygame.init()
        self.settings = settings.Settings()
        size = self.settings.screen_width, self.settings.screen_height   # tuple
        self.screen = pygame.display.set_mode(size=size)
        pygame.display.set_caption("Ant Simulation")

        self.ants = pygame.sprite.Group()
        self.foods = pygame.sprite.Group()

    def check_collisions(self, g1, g2):
        collisions = pygame.sprite.groupcollide(g1, g2, False, True)
        if collisions:
            for Ant in collisions:
                Ant.collect()

    def play(self):
        ants = pygame.sprite.Group()
        for i in range(5):
            x = random.randint(0, self.settings.screen_width)
            y = random.randint(0, self.settings.screen_height)
            ants.add(ant.Ant(x, y, game=self, screen=self.screen, settings=self.settings))

        foods = pygame.sprite.Group()
        for i in range(3):
            x = random.randint(0, self.settings.screen_width)
            y = random.randint(0, self.settings.screen_height)
            foods.add(Food.Food(x, y, game=self, screen=self.screen, settings=self.settings))

        homebase = base.Base(self.settings.screen_width/2, self.settings.screen_height/2, game=self, settings= self.settings, screen=self.screen)

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            # Draw everything
            self.screen.fill(self.settings.bg_color)
            self.check_collisions(ants, foods)
            # Update entities
            ants.update()
            foods.update()
            homebase.update()

            pygame.display.flip()

        pygame.quit()


def main():
    sim = AntSim()
    sim.play()

if __name__ == '__main__':
    main()


    # # Create ants
    # ants = pygame.sprite.Group()
    # for i in range(10):
    #     x = random.randint(0, screen_width)
    #     y = random.randint(0, screen_height)
    #     ants.add(Ant(x, y))
    #
    # # Game loop
    # running = True
    # while running:
    #     for event in pygame.event.get():
    #         if event.type == pygame.QUIT:
    #             running = False
    #
    #     # Update ants
    #     ants.update()
    #
    #     # Draw everything
    #     screen.fill(white)
    #     ants.draw(screen)
    #     pygame.display.flip()
    #
    # pygame.quit()
