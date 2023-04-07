import pygame
import sys
from game.worldEngine import WorldEngine
from game.config import *
from game.ui import *


class Game:

    def __init__(self, screen, clock) -> None:
        self.screen = screen
        self.clock = clock
        self.width, self.height = self.screen.get_size()
        self.world = WorldEngine(10, 10, self.width, self.height)

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
         self.screen.blit(self.world.empty_tiles, (0,0))
         #drawing the grid
         for x in range(self.world.grid_max_x):
              for y in range(self.world.grid_max_y):
                #    sq = self.world.world[x][y]["rect"]

                #    rect = pygame.Rect(sq[0][0], sq[0][1], LAND_SIZE, LAND_SIZE)
                #    pygame.draw.rect(self.screen, "white", rect, 1)

                   #draw tiles
                   render_position = self.world.world[x][y]["render_pos"]
                   #self.screen.blit(self.world.tiles["block"], (render_position[0] + self.width/2, render_position[1] + self.height/4 ))
                   #draw tree/rock
                   tile = self.world.world[x][y]["tile"]
                   if tile != "":
                        self.screen.blit(self.world.tiles[tile],
                                        (render_position[0] + self.width/2,
                                        render_position[1] + self.height/4 - (self.world.tiles[tile].get_height() - LAND_SIZE)))


                #    poly = self.world.world[x][y]["iso_poly"]
                #    #adding offset
                #    poly = [(x + self.width/2, y + self.height/4) for x, y in poly]
                #    pygame.draw.polygon(self.screen, "red", poly, 1)
         draw_text(self.screen, str(int(self.clock.get_fps())), "white", 25, (200,0) )

         pygame.display.flip()