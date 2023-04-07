
# The idea is to create a town for every user in a country where users from the same region play toguether, 
# the town can have farms for recources, houses for workers and schools and millitary for defence/attaques. 
# I have 16 days until the deadline, if I manage one big task per day I can make it, I never used pygames before, I work with more visual IDE like unreal, I need the money so, just deal with it.
# Steps: 
# 1 pygame docs and setup + init code + setup camera + world game class
# 2 database connection and user registration and town init + resource managment 
# 3 a grid system to manage spots in the town and spawn new buildings 
# 4 input controller and setup clicks events
# 5 will see from there 

# 1 pygame setup
import pygame
from game.game import Game


def main():

    #stats
    uiMode = True
    playMode = True

    pygame.init()
    pygame.mixer.init()

    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    clock = pygame.time.Clock()
    
    
    #implement menu

    #implement game
    game = Game(screen, clock)

    while uiMode:

        # start menu
        
        while playMode:

            #Game loop
            game.run()

if __name__ == "__main__":
    main()