def dfs(a, b, c, depth=0, steps=None):
    if steps is None:
        steps = []  # Initialize steps list if not provided
    
    if depth >= 2 ** 3:
        return False
    
    if len(b) == 3:
        print(steps)
        return True
    
    if len(a):
        n = a.pop()
        
        if not len(b) or b[-1] > n:
            if dfs(a, b + [n], c, depth+1, steps + ["A to B"]):
                return True
        
        if not len(c) or c[-1] > n:
            if dfs(a, b, c + [n], depth+1, steps + ["A to C"]):
                return True
        
        a.append(n)
    
    if len(b):
        n = b.pop()
        
        if not len(a) or a[-1] > n:
            if dfs(a + [n], b, c, depth+1, steps + ["B to A"]):
                return True
        
        if not len(c) or c[-1] > n:
            if dfs(a, b, c + [n], depth+1, steps + ["B to C"]):
                return True
        
        b.append(n)
    
    if len(c):
        n = c.pop()
        
        if not len(a) or a[-1] > n:
            if dfs(a + [n], b, c, depth+1, steps + ["C to A"]):
                return True
        
        if not len(b) or b[-1] > n:
            if dfs(a, b + [n], c, depth+1, steps + ["C to B"]):
                return True
        
        c.append(n)
    
    return False

print("Tower of Hanoi Solution using DFS: ")
start_state = [3, 2, 1]
goal_state = []

if not dfs(start_state, goal_state, []):
    print("No solution found.")
