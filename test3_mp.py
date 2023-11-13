import pygame as pg
import random
from collections import deque
from queue import Queue,PriorityQueue
import heapq


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

def cost(current, next_node):
    return 1


maze = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20],
    [21, 22, 23, 24, 25]
]

queue = []
start = (maze[0][0])
end = (maze[4][4])
print(start,end)



frontier = PriorityQueue()
frontier.put(start, 0)
came_from = dict()
cost_so_far = dict()
came_from[start] = None
cost_so_far[start] = 0

while not frontier.empty():
    current = frontier.get()

    if current == end:
        break

    for next_node in neighbors(maze, current):
        new_cost = cost_so_far[current] + 1  # Assuming each step has a cost of 1
        if next_node not in cost_so_far or new_cost < cost_so_far[next_node]:
            cost_so_far[next_node] = new_cost
            priority = new_cost
            frontier.put(next_node, priority)
            came_from[next_node] = current











