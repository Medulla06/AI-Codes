import heapq
import numpy as np
import matplotlib.pyplot as plt
import random
import math


class Node:
    def __init__(self, x, y, parent=None):
        self.x = x
        self.y = y
        self.parent = parent
        # Heuristic Cost
        self.g = 0 
        self.h = 0  
        self.f = 0  

    def __lt__(self, other):
        return self.f < other.f

def heuristic(node, goal):
    # Manhattan distance 
    # return math.sqrt((node.x - goal.x)**2 + (node.y - goal.y)**2)
    return abs(node.x - goal.x) + abs(node.y - goal.y)

def get_neighbors(node, grid_map):
    neighbors = []
    # Right, Left, Down, Up
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]  
    for dx, dy in directions:
        nx, ny = node.x + dx, node.y + dy
        if 0 <= nx < len(grid_map) and 0 <= ny < len(grid_map[0]) and grid_map[nx][ny] == 0:
            neighbors.append(Node(nx, ny))
    return neighbors

def reconstruct_path(current_node):
    path = []
    while current_node is not None:
        path.append((current_node.x, current_node.y))
        current_node = current_node.parent
    return path[::-1]

def visualize_path(ax, grid_map, start, goal, constraint, closed_set, open_list, path, current_node, title):
    ax.clear()
    ax.imshow(grid_map, cmap='gray_r', origin='lower')

    for x, y in closed_set:
        ax.text(y, x, 'X', color='red', ha='center', va='center', fontsize=10)

    for node in open_list:
        ax.text(node.y, node.x, 'O', color='blue', ha='center', va='center', fontsize=10)

    if path:
        path_x, path_y = zip(*path)
        ax.plot(path_y, path_x, color='red', linewidth=2)

    ax.text(start[1], start[0], 'S', color='green', ha='center', va='center', fontsize=12)
    ax.text(goal[1], goal[0], 'G', color='purple', ha='center', va='center', fontsize=12)
    if constraint:
        if constraint[2] == 'left':
            ax.text(constraint[1], constraint[0], 'C', color='yellow', ha='center', va='center', fontsize=12)
        elif constraint[2] == 'right':
            ax.text(constraint[1], constraint[0], 'C', color='blue', ha='center', va='center', fontsize=12)

    ax.text(current_node.y, current_node.x, 'X', color='orange', ha='center', va='center', fontsize=12)
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.grid(True)
    ax.set_title(title)
    plt.pause(0.001)

def a_star(grid_map, start, goal, constraint=None):
    start_node = Node(start[0], start[1])
    goal_node = Node(goal[0], goal[1])

    open_list = []
    closed_set = set()

    heapq.heappush(open_list, start_node)

    fig, ax = plt.subplots(figsize=(10, 10))

    while open_list:
        current_node = heapq.heappop(open_list)

        if current_node.x == goal_node.x and current_node.y == goal_node.y:
            path = reconstruct_path(current_node)
            visualize_path(ax, grid_map, start, goal, constraint, closed_set, open_list, path, current_node, 'A* Algorithm Visualization')
            plt.show()
            return path

        closed_set.add((current_node.x, current_node.y))

        for neighbor in get_neighbors(current_node, grid_map):
            if (neighbor.x, neighbor.y) in closed_set:
                continue

            if constraint and neighbor.x == constraint[0] and neighbor.y == constraint[1]:
                if constraint[2] == 'left':
                    neighbor.g = current_node.g + 10  # Discourage path
                elif constraint[2] == 'right':
                    neighbor.g = current_node.g + 1  # Allow path
            else:
                neighbor.g = current_node.g + 1

            neighbor.h = heuristic(neighbor, goal_node)
            neighbor.f = neighbor.g + neighbor.h
            neighbor.parent = current_node

            heapq.heappush(open_list, neighbor)

        visualize_path(ax, grid_map, start, goal, constraint, closed_set, open_list, [], current_node, 'A* Algorithm Visualization')

    plt.show()

    return None

def dijkstra(grid_map, start, goal, constraint=None):
    start_node = Node(start[0], start[1])
    goal_node = Node(goal[0], goal[1])

    open_list = []
    closed_set = set()

    heapq.heappush(open_list, start_node)

    fig, ax = plt.subplots(figsize=(10, 10))

    while open_list:
        current_node = heapq.heappop(open_list)

        if current_node.x == goal_node.x and current_node.y == goal_node.y:
            path = reconstruct_path(current_node)
            visualize_path(ax, grid_map, start, goal, constraint, closed_set, open_list, path, current_node, 'Dijkstra Plot')
            plt.show()
            return path

        closed_set.add((current_node.x, current_node.y))

        for neighbor in get_neighbors(current_node, grid_map):
            if (neighbor.x, neighbor.y) in closed_set:
                continue

            if constraint and neighbor.x == constraint[0] and neighbor.y == constraint[1]:
                if constraint[2] == 'left':
                    neighbor.g = current_node.g + 10  # Discourage path
                elif constraint[2] == 'right':
                    neighbor.g = current_node.g + 1  # Allow path
            else:
                neighbor.g = current_node.g + 1

            neighbor.parent = current_node

            heapq.heappush(open_list, neighbor)

        visualize_path(ax, grid_map, start, goal, constraint, closed_set, open_list, [], current_node, 'Dijkstra Plot')

    plt.show()

    return None

def get_points_from_user(grid_map):
    fig, ax = plt.subplots(figsize=(8, 8))
    ax.imshow(grid_map, cmap='gray_r', origin='lower')
    ax.set_title('Click on three points: Start, End, Constraint')
    
    points = []

    def onclick(event):
        if len(points) < 3:
            x, y = int(event.ydata), int(event.xdata)
            
            if grid_map[x][y] != 1:
                if event.button == 1:
                    ax.plot(y, x, 'ro' if len(points) == 0 else ('go' if len(points) == 1 else 'yo'), markersize=8)
                    points.append((x, y, 'left')) 
                elif event.button == 3:
                    ax.plot(y, x, 'bo', markersize=8) 
                    points.append((x, y, 'right'))
                    
                if len(points) == 1:
                    ax.legend(['Start'], loc='upper left')
                elif len(points) == 2:
                    ax.legend(['Start', 'End'], loc='upper left')
                elif len(points) == 3:
                    ax.legend(['Start', 'End', 'Constraint'], loc='upper left')
                    
                plt.draw()
            else:
                ax.text(3.5, -1, 'Cannot select here!', color='black', ha='center', va='center', fontsize=12)
                plt.draw()

    def onkey(event):
        if event.key == 'q':
            plt.close(fig)

    fig.canvas.mpl_connect('button_press_event', onclick)
    fig.canvas.mpl_connect('key_press_event', onkey)
    ax.text(3.5, 10, 'Press q to exit', fontsize=12)
    plt.show()

    return points

grid_map = np.random.choice([0, 1], size=(25, 25), p=[0.8, 0.2])

points = get_points_from_user(grid_map)
print("Selected points:", points)
start = points[0]
goal = points[1]
constraint = points[2]

path1 = a_star(grid_map, start, goal, constraint)
print("Path using A*:", path1)

path2 = dijkstra(grid_map, start, goal)
print("Path using Dijkstra:", path2)
