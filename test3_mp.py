import pygame as pg
import random
import sys

pg.init()

screen = pg.display.set_mode((1000, 1000))
pg.display.set_caption("Mazerunner")
size = 25, 25

def grid():
    start_position = (0, 0)
    end_position = (1000, 1000)

    for y in range(0, 1000, 25):
        pg.draw.line(screen, (255, 255, 255), (start_position[0], y), (end_position[0], y))

    for x in range(0, 1000, 25):
        pg.draw.line(screen, (255, 255, 255), (x, start_position[1]), (x, end_position[1]))


grid()
#https://www.geeksforgeeks.org/python-using-2d-arrays-lists-the-right-way/
grid_values = []
for _ in range(40):
    row = []
    for _ in range(40):
        row.append(0)
    grid_values.append(row)
list_x = []
list_y = []

def firkanter_gul():
    for _ in range(200):
        starting_pos_x = random.randrange(0, 40)
        starting_pos_y = random.randrange(0, 40)
        list_x.append(starting_pos_x)
        list_y.append(starting_pos_y)
        starting_pos = (starting_pos_x * 25, starting_pos_y * 25)
        rect = starting_pos, size
        pg.draw.rect(screen, (255, 255, 0), rect)
        grid_values[starting_pos_x][starting_pos_y] = 1


def firkanter_blå():
    for _ in range(200):
        starting_pos_x = random.randrange(0, 40)
        starting_pos_y = random.randrange(0, 40)
        list_x.append(starting_pos_x)
        list_y.append(starting_pos_y)
        starting_pos = (starting_pos_x * 25, starting_pos_y * 25)
        rect = starting_pos, size
        pg.draw.rect(screen, (0, 0, 255), rect)
        grid_values[starting_pos_x][starting_pos_y] = 2
        

    while queue:
        vertex = queue.popleft()
        visited.add(vertex)
        for neighbor in graph[vertex]:
            if neighbor not in visited:
                queue.append(neighbor)

def firkant_rød():
    for _ in range(2):
        for _ in range(10):
            size = 25, 25
            starting_pos_x = random.randrange(0, 40)
            starting_pos_y = random.randrange(0, 40)
            if grid_values[starting_pos_x][starting_pos_y] == 0:
                starting_pos = (starting_pos_x * 25, starting_pos_y * 25)
                rect = starting_pos, size
                pg.draw.rect(screen, (255, 0, 0), rect)
                list_x.append(starting_pos_x)
                list_y.append(starting_pos_y)
                grid_values[starting_pos_x][starting_pos_y] = -1
                break

firkanter_blå()
firkanter_gul()
firkant_rød()
pg.display.flip()


def gridvalues():
    for row in grid_values:
        print(row)
#gridvalues()

gridlist = []
for y in range(40):
    for x in range(40):
        gridlist.append((x, y))

grid_dict = {}
rect = (100,100),size
queue = []

running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
    for i, (x, y) in enumerate(gridlist):
        key = f"({x},{y})"
        value = grid_values[x][y]
        grid_dict[key] = value

        if  grid_values[x] ==34 and grid_dict[key] == 0:
            pg.draw.rect(screen,(0,255,0),rect)

    pg.display.flip()
pg.quit()

