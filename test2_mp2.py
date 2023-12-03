import pygame as pg
import random
from collections import deque

pg.init()
screen = pg.display.set_mode((1000, 1000))
pg.display.set_caption("Mazerunner")
size = 25, 25
random.seed(42)

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

def firkanter_yellow(num_squares):
    colored_squares = set()
    while len(colored_squares) < num_squares:
        x = random.randrange(0, 40)
        y = random.randrange(0, 40)
        if (x, y) not in colored_squares and (x, y) != (0, 0) and (x, y) != (36, 32):
            colored_squares.add((x, y))
            rect = (x * 25, y * 25), size
            pg.draw.rect(screen, (255, 255, 0), rect)
            grid_values[x][y] = 1

def firkanter_blue(num_squares):
    colored_squares = set()
    while len(colored_squares) < num_squares:
        x = random.randrange(0, 40)
        y = random.randrange(0, 40)
        if (x, y) not in colored_squares and (x, y) != (0, 0) and (x, y) != (36, 32):
            colored_squares.add((x, y))
            rect = (x * 25, y * 25), size
            pg.draw.rect(screen, (0, 0, 255), rect)
            grid_values[x][y] = 1


def firkant_red():
    size = 25, 25
    starting_pos = (25,0)
    end_pos = (875,775)
    rect_start = starting_pos, size
    rect_end = end_pos,size
    pg.draw.rect(screen, (255, 0, 0), rect_start)
    pg.draw.rect(screen, (255, 0, 0), rect_end)

num_yellow_squares = 200
num_blue_squares = 200

firkanter_blue(num_blue_squares)
firkanter_yellow(num_yellow_squares)

firkant_red()

def bfs(grid, start, end):
    rows, cols = len(grid), len(grid[0])
    visited = [[False for _ in range(cols)] for _ in range(rows)]
    parent = [[None for _ in range(cols)] for _ in range(rows)]
    
    queue = deque([start])
    visited[start[0]][start[0]] = True

    while queue:
        x, y = queue.popleft()
        for dx, dy in [(1,0), (0,1), (-1,0), (0,-1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < rows and 0 <= ny < cols and not visited[nx][ny] and grid[nx][ny] == 0:
                visited[nx][ny] = True
                parent[nx][ny] = (x, y)
                queue.append((nx, ny))
                if (nx, ny) == end:
                    return parent 

    return parent 


def get_path(parent, start, end):
    if parent[end[0]][end[1]] is None:
        print("No path found")
        return []

    path = []
    while end != start:
        path.append(end)
        end = parent[end[0]][end[1]]
    path.reverse()
    print("path:",path)
    return path

start_pos = (0, 0)  
end_pos = (35, 31) 

parent = bfs(grid_values, start_pos, end_pos)
path = get_path(parent, start_pos, end_pos)

if path:
    for i in range(1, len(path)):
        x1, y1 = path[i - 1]
        x2, y2 = path[i]
        start_pixel = (x1 * 25 + 12, y1 * 25 + 12)
        end_pixel = (x2 * 25 + 12, y2 * 25 + 12)
        pg.draw.line(screen, (0, 255, 0), start_pixel, end_pixel, width=3)




pg.display.flip()

""" def gridvalues():
    for row in grid_values:
        print(row)
gridvalues() """
running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
pg.quit()





