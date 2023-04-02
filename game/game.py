import pygame
import sys

class Game:

    def __init__(self, screen, clock) -> None:
        self.screen = screen
        self.clock = clock
        self.width, self.hight = self.screen.get_size()

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
         self.screen.fill("orange")
         pygame.display.flip()