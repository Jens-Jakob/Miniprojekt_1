import pygame as pg
import random

pg.init()
screen = pg.display.set_mode((1000, 1000))


size = (25, 25)
color = (255, 255, 255)



position_list = []


for _ in range(200):
    x = random.gauss(500, 500)
    y = random.gauss(500, 500)
    position_list.append((x, y))


new_position_list=[]

for i, position_new in enumerate(position_list):
    if position_list[i][0] + i - position_new[0] >= 10 or position_list[i][1] + i - position_new[1] > 10:
        new_position_list.append(position_new)

position_list = new_position_list 



for i in range(len(position_list)):
    pg.draw.rect(screen, color, (position_list[i][0] + i, position_list[i][1] + i, size[0], size[1]))



print(position_new)
print(f"\n{position_list}")

pg.display.flip()


running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False


pg.quit()
