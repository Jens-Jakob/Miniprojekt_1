import pygame
import random
from collections import deque

# Initialize Pygame
pygame.init()

# Maze setup - 40x40 grid with values from 1 to 3
maze_size = 40
maze = [[random.randint(1, 3) for _ in range(maze_size)] for _ in range(maze_size)]

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
colors = {1: WHITE, 2: (200, 200, 200), 3: (150, 150, 150)}  # Different colors for different values

# Pygame window setup
cell_size = 20
width = height = maze_size * cell_size
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Maze Solver - Modified BFS")

# Function to draw the maze
def draw_maze():
    screen.fill(WHITE)
    for i, row in enumerate(maze):
        for j, value in enumerate(row):
            pygame.draw.rect(screen, colors[value], (j * cell_size, i * cell_size, cell_size, cell_size))
            pygame.draw.rect(screen, BLACK, (j * cell_size, i * cell_size, cell_size, cell_size), 1)

# Function to draw the path
def draw_path(path):
    print("Path:", path) 
    for cell in path:
        i, j = divmod(cell - 1, maze_size)
        pygame.draw.rect(screen, RED, (j * cell_size, i * cell_size, cell_size, cell_size))
        pygame.display.flip()
        pygame.time.wait(10)

# Function to get neighbors
def neighbors(node):
    # Convert node number back to grid coordinates
    i, j = divmod(node - 1, maze_size)
    # Possible movements: up, down, left, right
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    result = []
    for dr, dc in directions:
        new_row, new_col = i + dr, j + dc
        if 0 <= new_row < maze_size and 0 <= new_col < maze_size:
            result.append(maze[new_row][new_col])
    print(f"Neighbors of {node}: {result}")  # Debug print
    return result

# Cost function based on the value of the cell
def cost(value):
    return value

# Modified BFS algorithm to consider different costs
def modified_bfs(start, end):
    queue = deque([(0, start)])  # Store cumulative cost with node
    came_from = {start: None}
    total_cost = {start: 0}
    print(f"came_from: {came_from}") 

    while queue:
        cum_cost, current = queue.popleft()

        if current == end:
            break

        for next_node in neighbors(current):
            new_cost = cum_cost + cost(maze[divmod(next_node - 1, maze_size)[0]][divmod(next_node - 1, maze_size)[1]])
            if next_node not in total_cost or new_cost < total_cost[next_node]:
                total_cost[next_node] = new_cost
                queue.append((new_cost, next_node))
                came_from[next_node] = current

    path = []
    current_node = end
    while current_node is not None:
        path.append(current_node)
        current_node = came_from.get(current_node, None)

    path.reverse()
    return path

# Main loop
running = True
start = 1
end = maze_size * maze_size
path = modified_bfs(start, end)


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    draw_maze()
    draw_path(path)
    pygame.display.flip()

pygame.quit()
