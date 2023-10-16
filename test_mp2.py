import pygame as pg
import random

pg.init()
screen = pg.display.set_mode((1000, 1000))






for _ in range(50):
    size = 25,25
    starting_pos = (random.randrange(0,1000,25) ,random.randrange(0,1000,25))
    rect = starting_pos,size
    pg.draw.rect(screen,(255,255,0),rect)
    pg.display.flip()
 



""" size=(5,5)
start_point = (0,0)

for i in range(1,100):
    start_point = (start_point[0] + i ,start_point[1] + i)
    box = (start_point[0] + i, start_point[1] + i)
    box_size = (5 + i, 5 + i)
    rect = box + box_size   
    pg.draw.rect(screen,(255,255,255),rect)
    pg.display.flip() """

running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False


pg.quit()
