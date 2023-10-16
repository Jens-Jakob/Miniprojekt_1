import pygame as pg
import random

# Initialize Pygame
pg.init()

# Set up the display
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
    

def firkanter_gul():
    for _ in range(200):
        size = 25,25
        starting_pos = (random.randrange(0,1000,25) ,random.randrange(0,1000,25))
        rect = starting_pos,size
        pg.draw.rect(screen,(255,255,0),rect)
        pg.display.flip()
 
firkanter_gul()

def firkanter_hvid():
    pass


running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False


   
    

pg.quit()
