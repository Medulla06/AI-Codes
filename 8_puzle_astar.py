import heapq

# Define the goal state
goal_state = [[1, 2, 3],
              [8, 0, 4],
              [7, 6, 5]]  # 0 represents the blank space

# Define the heuristic function (Manhattan distance)
def heuristic(state):
    distance = 0
    for i in range(3):
        for j in range(3):
            if state[i][j] != 0:
                target_x = (state[i][j] - 1) // 3
                target_y = (state[i][j] - 1) % 3
                distance += abs(i - target_x) + abs(j - target_y)
    return distance

# Define a function to generate the neighbors of a given state
def get_neighbors(state):
    neighbors = []
    x, y = None, None
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                x, y = i, j
                break

    deltas = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    for dx, dy in deltas:
        new_x, new_y = x + dx, y + dy
        if 0 <= new_x < 3 and 0 <= new_y < 3:
            new_state = [row[:] for row in state]
            new_state[x][y], new_state[new_x][new_y] = new_state[new_x][new_y], new_state[x][y]
            neighbors.append(((new_x, new_y), new_state))
    return neighbors

# Define the A* algorithm
def a_star(initial_state):
    heap = [(0, initial_state, [])]
    visited = set()
    
    while heap:
        f, state, moves = heapq.heappop(heap)
        if state == goal_state:
            return [(state, move) for move in moves]
        
        visited.add(tuple(map(tuple, state)))
        
        for move, neighbor in get_neighbors(state):
            if tuple(map(tuple, neighbor)) not in visited:
                g = f + 1
                h = heuristic(neighbor)
                heapq.heappush(heap, (g + h, neighbor, moves + [move]))
    
    return None

# Test the algorithm
initial_state = [[2, 8, 3],
                 [1, 6, 4],
                 [7, 0, 5]]  # Initial state with the blank space at the bottom left

solution_states = a_star(initial_state)
if solution_states:
    print("Solution found:")
    for state, move in solution_states:
        print("Move:", move)
        for row in state:
            print(row)
        print()
else:
    print("No solution found.")
