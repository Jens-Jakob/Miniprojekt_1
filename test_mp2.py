import pygame as pg
import random

pg.init()

screen = pg.display.set_mode((1000, 1000))
pg.display.set_caption("Mazerunner")

def grid():
    start_position = (0, 0)
    end_position = (1000, 1000)

    for y in range(0, 1000, 25):
        pg.draw.line(screen, (255, 255, 255), (start_position[0], y), (end_position[0], y))

    for x in range(0, 1000, 25):
        pg.draw.line(screen, (255, 255, 255), (x, start_position[1]), (x, end_position[1]))

grid()

num_cells = 40
grid_values = [[0 for _ in range(num_cells)] for _ in range(num_cells)]

    
random.normalvariate()

def firkanter_gul():
    for _ in range(200):
        size = 25,25
        starting_pos = (random.randrange(0,1000,25) ,random.randrange(0,1000,25))
        rect = starting_pos,size
        pg.draw.rect(screen,(255,255,0),rect)
        grid_values[x][y] = 1
        pg.display.flip()
 
firkanter_gul()

def firkanter_blå():
    for _ in range(200):
        size = 25,25
        starting_pos = (random.randrange(0,1000,25) ,random.randrange(0,1000,25))
        rect = starting_pos,size
        pg.draw.rect(screen,(0,0,255),rect)
        grid_values[x][y] = 1
        pg.display.flip()

firkanter_blå()

def gridvalues():
    for row in grid_values:
        print(row)





running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False


   
    

pg.quit()
