import pygame
import random
from .config import LAND_SIZE

class WorldEngine:

    def __init__(self, grid_max_x, grid_max_y, width, height) -> None:
        self.grid_max_x = grid_max_x
        self.grid_max_y = grid_max_y
        self.width = width
        self.height = height
        self.world = self.create_world()
        self.tiles = self.load_images()
    

    def create_world(self):

        world = []

        for grid_x in range(self.grid_max_x):
            world.append([])
            for grid_y in range(self.grid_max_y):
                world_land = self.grid_to_land(grid_x, grid_y)
                world[grid_x].append(world_land)


        return world


    # we convert grid position to rect land tile            
    def grid_to_land(self, grid_x, grid_y):

        #rect vertices
        rect = [
            (grid_x * LAND_SIZE, grid_y * LAND_SIZE),
            (grid_x * LAND_SIZE + LAND_SIZE, grid_y * LAND_SIZE),
            (grid_x * LAND_SIZE + LAND_SIZE, grid_y * LAND_SIZE + LAND_SIZE),
            (grid_x * LAND_SIZE , grid_y * LAND_SIZE + LAND_SIZE)
        ]

        # creating the isometric poly
        iso_poly = [self.land_to_iso(x, y) for x, y in rect]

        min_x = min([x for x, y in iso_poly])
        min_y = min([y for x, y in iso_poly])

        r = random.randint(1, 100)

        if r <= 5:
            tile = "tree"
        elif r <= 10:
            tile = "rock"
        else:
            tile = ""

        #output dict for the land to add more data later
        output = {
            "grid": [grid_x, grid_y],
            "rect": rect,
            "iso_poly": iso_poly,
            "render_pos": [min_x, min_y],
            "tile": tile
        }

        return output
    
    def land_to_iso(self, x, y):
        #convert x y cordinates to isometric
        iso_x = x - y
        iso_y = (x + y)/2
        return iso_x, iso_y
    
    def load_images(selft):
        block = pygame.image.load("game/assets/tiles/block.png")
        tree = pygame.image.load("game/assets/tiles/tree.png")
        rock = pygame.image.load("game/assets/tiles/rock.png")

        return {"block": block, "tree": tree, "rock": rock}