from collections import deque

def BFS(a, b, c):
    q = deque([[a, b, c, []]])
    
    while q:
        # State
        a, b, c, steps = q.popleft()
        
        # Check if goal state is reached
        if len(b) == 3:
            print(steps)
            break
        
        # Move a disk from peg A to peg B
        if len(a):
            n = a[-1]  # Select the top disk from peg A
            if len(b) == 0 or b[-1] > n:
                new_a = a[:-1]  # Create a copy of peg A without the top disk
                new_b = b + [n]  # Create a copy of peg B with the new disk
                q.append([new_a, new_b, c, steps + ["A -> B"]])
            
        # Move a disk from peg B to peg A
        if len(b):
            n = b[-1]  # Select the top disk from peg B
            if len(a) == 0 or a[-1] > n:
                new_a = a + [n]  # Create a copy of peg A with the new disk
                new_b = b[:-1]  # Create a copy of peg B without the top disk
                q.append([new_a, new_b, c, steps + ["B -> A"]])
        
        # Move a disk from peg B to peg C
        if len(b):
            n = b[-1]  # Select the top disk from peg B
            if len(c) == 0 or c[-1] > n:
                new_b = b[:-1]  # Create a copy of peg B without the top disk
                new_c = c + [n]  # Create a copy of peg C with the new disk
                q.append([a, new_b, new_c, steps + ["B -> C"]])
        
        # Move a disk from peg C to peg A
        if len(c):
            n = c[-1]  # Select the top disk from peg C
            if len(a) == 0 or a[-1] > n:
                new_a = a + [n]  # Create a copy of peg A with the new disk
                new_c = c[:-1]  # Create a copy of peg C without the top disk
                q.append([new_a, b, new_c, steps + ["C -> A"]])

        # Move a disk from peg C to peg B
        if len(c):
            n = c[-1]  # Select the top disk from peg C
            if len(b) == 0 or b[-1] > n:
                new_b = b + [n]  # Create a copy of peg B with the new disk
                new_c = c[:-1]  # Create a copy of peg C without the top disk
                q.append([a, new_b, new_c, steps + ["C -> B"]])

    return None

start_state = [3, 2, 1]
goal_state = []

solution = BFS(start_state, goal_state, [])

if solution:
    print("Solution found!")
    for move in solution:
        print(move)
else:
    print("No solution found.")
