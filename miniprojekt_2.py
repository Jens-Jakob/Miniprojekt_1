import pygame as pg
import random
from collections import deque

class Maze:
    def __init__(self, screen, size):
        self.screen = screen
        self.size = size
        self.grid_values = [[0 for _ in range(40)] for _ in range(40)]
        self.start_pos = (-1, 0)
        self.end_pos = (35, 31)

    def draw_grid(self):
        for y in range(0, 1000, 25):
            pg.draw.line(self.screen, (255, 255, 255), (0, y), (1000, y))
        for x in range(0, 1000, 25):
            pg.draw.line(self.screen, (255, 255, 255), (x, 0), (x, 1000))

    def draw_colored_squares(self, num_squares, color):
        colored_squares = set()
        buffer_zone = [(0, 0), (-1, 0), (1, 0), (0, -1), (0, 1)] 
        while len(colored_squares) < num_squares:
            x, y = random.randrange(40), random.randrange(40)
            if (x, y) not in colored_squares and (x, y) not in buffer_zone and (x, y) != self.end_pos:
                colored_squares.add((x, y))
                pg.draw.rect(self.screen, color, (x * 25, y * 25, 25, 25))
                self.grid_values[x][y] = 1

    def draw_start_end_positions(self):
        pg.draw.rect(self.screen, (0, 255, 0), (0 * 25, self.start_pos[1] * 25, 25, 25))
        pg.draw.rect(self.screen, (0, 255, 0), (self.end_pos[0] * 25, self.end_pos[1] * 25, 25, 25))

class BFS:
    def find_path(grid, start, end):
        rows, cols = len(grid), len(grid[0])
        visited = [[False for _ in range(cols)] for _ in range(rows)]
        parent = [[None for _ in range(cols)] for _ in range(rows)]

        queue = deque([start])
        visited[start[0]][start[1]] = True

        while queue:
            x, y = queue.popleft()
            for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < rows and 0 <= ny < cols and not visited[nx][ny] and grid[nx][ny] == 0:
                    visited[nx][ny] = True
                    parent[nx][ny] = (x, y)
                    queue.append((nx, ny))
                    if (nx, ny) == end:
                        return BFS.get_path(parent, start, end)
        return []

    def get_path(parent, start, end):
        path = []
        while end != start:
            path.append(end)
            end = parent[end[0]][end[1]]
        path.reverse()
        return path

class Game:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode((1000, 1000))
        pg.display.set_caption("Mazerunner")
        self.maze = Maze(self.screen, (25, 25))
        self.running = True

    def run(self):
        self.maze.draw_grid()
        self.maze.draw_colored_squares(250, (255, 255, 0))
        self.maze.draw_colored_squares(250, (0, 0, 255))
        self.maze.draw_start_end_positions()
        path = BFS.find_path(self.maze.grid_values, self.maze.start_pos, self.maze.end_pos)

        if path:
            for i in range(1, len(path)):
                x1, y1 = path[i - 1]
                x2, y2 = path[i]
                pg.draw.line(self.screen, (255, 20, 147), (x1 * 25 + 12, y1 * 25 + 12), (x2 * 25 + 12, y2 * 25 + 12), 3)

        pg.display.flip()

        while self.running:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.running = False
        pg.quit()

if __name__ == "__main__":
    game = Game()
    game.run()
