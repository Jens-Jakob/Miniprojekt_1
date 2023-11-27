import pygame as pg
import random
from collections import deque

class Grid:
    def __init__(self, screen, size):
        self.screen = screen
        self.size = size
        self.grid_values = [[0 for _ in range(40)] for _ in range(40)]

    def draw_grid(self):
        start_position = (0, 0)
        end_position = (1000, 1000)
        for y in range(0, 1000, 25):
            pg.draw.line(self.screen, (255, 255, 255), (start_position[0], y), (end_position[0], y))
        for x in range(0, 1000, 25):
            pg.draw.line(self.screen, (255, 255, 255), (x, start_position[1]), (x, end_position[1]))

class Squares:
    def __init__(self, screen, grid, size):
        self.screen = screen
        self.grid = grid
        self.size = size

    def draw_squares(self, num_squares, color, value):
        colored_squares = set()
        while len(colored_squares) < num_squares:
            x = random.randrange(0, 40)
            y = random.randrange(0, 40)
            if (x, y) not in colored_squares and (x, y) != (0, 0) and (x, y) != (36, 32):
                colored_squares.add((x, y))
                rect = (x * 25, y * 25), self.size
                pg.draw.rect(self.screen, color, rect)
                self.grid.grid_values[x][y] = value


class Pathfinder:
    def __init__(self, screen, grid):
        self.screen = screen
        self.grid = grid

    def bfs(self, start, end):
        grid = self.grid.grid_values  # Access the grid values
        rows, cols = len(grid), len(grid[0])
        visited = [[False for _ in range(cols)] for _ in range(rows)]
        parent = [[None for _ in range(cols)] for _ in range(rows)]

        queue = deque([start])
        visited[start[0]][start[1]] = True

        while queue:
            x, y = queue.popleft()
            for dx, dy in [(1,0), (0,1), (-1,0), (0,-1)]:  # Directions: Right, Down, Left, Up
                nx, ny = x + dx, y + dy
                if 0 <= nx < rows and 0 <= ny < cols and not visited[nx][ny] and grid[nx][ny] == 0:
                    visited[nx][ny] = True
                    parent[nx][ny] = (x, y)
                    queue.append((nx, ny))
                    if (nx, ny) == end:
                        return parent  # Path found

        return parent  # No path found

    def get_path(self, start, end):
        parent = self.bfs(start, end)  # Use the bfs method to get the parent array
        if parent[end[0]][end[1]] is None:
            print("No path found")
            return []

        path = []
        while end != start:
            path.append(end)
            end = parent[end[0]][end[1]]
        path.reverse()
        print("path:", path)
        return path

    def draw_path(self, start_pos, end_pos):
        path = self.get_path(start_pos, end_pos)
        if path:
            for i in range(1, len(path)):
                x1, y1 = path[i - 1]
                x2, y2 = path[i]
                start_pixel = (x1 * 25 + 12, y1 * 25 + 12)
                end_pixel = (x2 * 25 + 12, y2 * 25 + 12)
                pg.draw.line(self.screen, (0, 255, 0), start_pixel, end_pixel, width=3)
    
    def draw_start_end_squares(self, start_pos, end_pos, color_start=(255, 0, 0), color_end=(255, 0, 0)):
        start_rect = (start_pos[0] * 25, start_pos[1] * 25), self.grid.size
        end_rect = (end_pos[0] * 25, end_pos[1] * 25), self.grid.size
        pg.draw.rect(self.screen, color_start, start_rect)
        pg.draw.rect(self.screen, color_end, end_rect)



class Game:
    def __init__(self):
        pg.init()
        random.seed(42)
        self.screen = pg.display.set_mode((1000, 1000))
        pg.display.set_caption("Mazerunner")
        self.grid = Grid(self.screen, (25, 25))
        self.squares = Squares(self.screen, self.grid, (25, 25))
        self.pathfinder = Pathfinder(self.screen, self.grid)

    def run(self):
        self.grid.draw_grid()
        self.squares.draw_squares(200, (255, 255, 0), 1)  # Yellow squares
        self.squares.draw_squares(200, (0, 0, 255), 2)    # Blue squares
        self.pathfinder.draw_path((0, 0), (35, 31))
        self.pathfinder.draw_start_end_squares((0, 0), (35, 31))

        pg.display.flip()
        running = True
        while running:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    running = False
        pg.quit()

# Running the game
game = Game()
game.run()


