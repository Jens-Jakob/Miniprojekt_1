import pygame
import heapq

# Set up Pygame
pygame.init()

# Maze setup
maze = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20],
    [21, 22, 23, 24, 25]
]

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Pygame window setup
cell_size = 25
width = len(maze[0]) * cell_size
height = len(maze) * cell_size
screen = pygame.display.set_mode((1000, 1000))
pygame.display.set_caption("Maze Solver")

# Function to draw the maze
def draw_maze():
    screen.fill(WHITE)
    for i, row in enumerate(maze):
        for j, cell in enumerate(row):
            pygame.draw.rect(screen, BLACK, (j * cell_size, i * cell_size, cell_size, cell_size), 1)
            font = pygame.font.Font(None, 36)
            text = font.render(str(cell), True, BLACK)
            screen.blit(text, (j * cell_size + 10, i * cell_size + 10))

# Function to draw the path
def draw_path(path):
    for node in path:
        i, j = divmod(node - 1, len(maze[0]))
        pygame.draw.rect(screen, RED, (j * cell_size, i * cell_size, cell_size, cell_size))
        pygame.display.flip()
        pygame.time.wait(100)

# Function to get neighbors
def neighbors(maze, node):
    row, col = None, None
    for i, row_values in enumerate(maze):
        if node in row_values:
            row, col = i, row_values.index(node)
            break

    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    result = []


    for dr, dc in directions:
        new_row, new_col = row + dr, col + dc
        if 0 <= new_row < len(maze) and 0 <= new_col < len(maze[0]):
            result.append(maze[new_row][new_col])

    return result

# Function to get cost
def cost(current, next_node):
    return 1

# Pygame loop
running = True
start = maze[0][0]
end = maze[-1][-1]

frontier = []
heapq.heappush(frontier, (0, start))
came_from = dict()
cost_so_far = dict()
came_from[start] = None
cost_so_far[start] = 0

while running and frontier:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    current_cost, current = heapq.heappop(frontier)

    if current == end:
        break

    for next_node in neighbors(maze, current):
        new_cost = cost_so_far[current] + cost(current, next_node)
        if next_node not in cost_so_far or new_cost < cost_so_far[next_node]:
            cost_so_far[next_node] = new_cost
            priority = new_cost
            heapq.heappush(frontier, (priority, next_node))
            came_from[next_node] = current

    draw_maze()
    pygame.display.flip()
    pygame.time.wait(100)

# Reconstruct the path
path = []
current_node = end
while current_node is not None:
    path.append(current_node)
    current_node = came_from[current_node]

path.reverse()

draw_path(path)

pygame.quit()
