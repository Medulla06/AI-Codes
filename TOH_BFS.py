from collections import deque

def Hanoi_bfs(a, b, c):
    q = deque([[a, b, c, []]])
    
    solved = False
    
    while q:
        # State
        a, b, c, steps = q.popleft()
        
        if len(b) == 3:
            return steps
        
        if len(a):
            n = a[-1]  # Select the top disk from peg A
            if len(b) == 0 or b[-1] > n:
                new_a = a[:-1]  # Create a copy of peg A without the top disk
                new_b = b + [n]  # Create a copy of peg B with the new disk
                q.append([new_a, new_b, c, steps + ["A to B"]])
            
        if len(b):
            n = b[-1]  # Select the top disk from peg B
            if len(a) == 0 or a[-1] > n:
                new_a = a + [n]  # Create a copy of peg A with the new disk
                new_b = b[:-1]  # Create a copy of peg B without the top disk
                q.append([new_a, new_b, c, steps + ["B to A"]])
            
            if len(c) == 0 or c[-1] > n:
                new_b = b[:-1]  # Create a copy of peg B without the top disk
                new_c = c + [n]  # Create a copy of peg C with the new disk
                q.append([a, new_b, new_c, steps + ["B to C"]])
        
        if len(c):
            n = c[-1]  # Select the top disk from peg C
            if len(a) == 0 or a[-1] > n:
                new_a = a + [n]  # Create a copy of peg A with the new disk
                new_c = c[:-1]  # Create a copy of peg C without the top disk
                q.append([new_a, b, new_c, steps + ["C to A"]])

            if len(b) == 0 or b[-1] > n:
                new_b = b + [n]  # Create a copy of peg B with the new disk
                new_c = c[:-1]  # Create a copy of peg C without the top disk
                q.append([a, new_b, new_c, steps + ["C to B"]]) 

    return None

print("Tower of Hanoi Solution using BFS: ")
start_state = [3, 2, 1]
goal_state = []

solution = Hanoi_bfs(start_state, goal_state, [])

if solution:
    print("Solution found!")
    for move in solution:
        print(move)
else:
    print("No solution found.")
