import pygame
import sys
from game.worldEngine import WorldEngine
from game.config import LAND_SIZE


class Game:

    def __init__(self, screen, clock) -> None:
        self.screen = screen
        self.clock = clock
        self.width, self.height = self.screen.get_size()
        self.world = WorldEngine(6, 6, self.width, self.height)

    def run(self):
        self.playing = True
        while self.playing:
            self.clock.tick(60)
            self.events()
            self.update()
            self.draw()

    def events(self):
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    # todo add popup message to confirm before exit
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.K_ESCAPE:
                     # todo add popup message to confirm before exit
                    pygame.quit()
                    sys.exit()

    def update(self):
         pass
    
    def draw(self):
         
         self.screen.fill("black")
         
         #drawing the grid
         for x in range(self.world.grid_max_x):
              for y in range(self.world.grid_max_y):
                   sq = self.world.world[x][y]["rect"]

                   rect = pygame.Rect(sq[0][0], sq[0][1], LAND_SIZE, LAND_SIZE)
                   pygame.draw.rect(self.screen, "white", rect, 1)

                   poly = self.world.world[x][y]["iso_poly"]
                   pygame.draw.polygon(self.screen, "red", poly, 1)


         pygame.display.flip()