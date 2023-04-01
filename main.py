
# The idea is to create a town for every user in a country where users from the same region play toguether, 
# the town can have farms for recources, houses for workers and schools and millitary for defence/attaques. 
# I have 16 days until the deadline, if I manage one big task per day I can make it, I never used pygames before, I work with more visual IDE like unreal, I need the money so, just deal with it.
# Steps: 
# 1 pygame docs and setup + init code 
# 2 database connection and user registration and town init 
# 3 a grid system to manage spots in the town and spawn new buildings 
# 4 input controller and setup clicks events
# 5 will see from there 

# 1 pygame setup
import pygame

pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # bg color I guess
    screen.fill("purple")

    # RENDER YOUR GAME HERE

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()