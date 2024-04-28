#Tower of Hanoi Problem using BFS 
from collections import deque

def Hanoi_bfs(a,b,c):
    q= deque([[a,b,c,[]]])
    solved = False
    while q:
        a,b,c,steps = q.popleft()
        
        if len(b)==3:
            return steps
        
        if len(a):
            n = a[-1]
            if len(b) ==0 or b[-1] >n:
                new_a = a[:-1]
                new_b = b+ [n]
                q.append([new_a,new_b,c,steps + ["A to B"]])
        
        if len(b):
            n = b[-1]
            if len(a) ==0 or a[-1] >n:
                new_a = a + [n]
                new_b = b[:-1]
                q.append([new_a,new_b,c,steps + ["B to A"]])
                
            if len(c) ==0 or c[-1] >n:
                new_b = b[:-1]
                new_c = c+ [n]
                q.append([a,new_b,new_c,steps + ["B to C"]])
                
        if len(c):
            n = c[-1]
            if len(a) ==0 or a[-1] >n:
                new_a = a + [n]
                new_c = c[:-1]
                q.append([new_a,b,new_c,steps + ["B to A"]])
                
            if len(b) ==0 or b[-1] >n:
                new_b = b + [n]
                new_c = c[:-1]
                q.append([a,new_b,new_c,steps + ["C to A"]])
                
    return None

#Tower of Hanoi Solution using DFS
def Hanoi_dfs(a,b,c,depth=0,steps=None):
    if steps is None:
        steps = []
    
    if depth >= 2**3:
        return False
    
    if len(b) ==3:
        print(steps)
        return True
    
    if len(a):
        n = a.pop()

        if not len(b) or b[-1]>n:
            if Hanoi_dfs(a,b+[n],c,depth+1,steps + ["A to B"]):
                return True
        
        if not len(c) or c[-1] >n:
            if Hanoi_dfs(a,b,c+[n],depth+1,steps + ["A to C"]):
                return True
        a.append(n)
    
    if len(b):
        n = b.pop()
        
        if not len(a) or a[-1]>n:
            if Hanoi_dfs(a+[n],b,c,depth+1,steps + ["B to A"]):
                return True
        
        if not len(c) or c[-1] >n:
            if Hanoi_dfs(a,b,c+[n],depth+1,steps + ["B to C"]):
                return True
        b.append(n)  
    
    if len(c):
        n = c.pop()
        
        if not len(a) or a[-1]>n:
            if Hanoi_dfs(a+[n],b,c,depth+1,steps + ["C to A"]):
                return True
        
        if not len(b) or b[-1] >n:
            if Hanoi_dfs(a,b+[n],c,depth+1,steps + ["C to B"]):
                return True
        c.append(n) 
        
    return False
    
#Tower of Hanoi Solution using IDS 
def Hanoi_ids(a,b,c):
    states = [[a, b, c, []]]
    new_states = []
    solved = False
    level = 0
    
    while not solved and states:
        for state in states:
            a,b,c,steps = state
            if len(steps) >= (2**3):
                continue
            
            if len(b)==3:
                print(steps)
                solved=True
                return
            
            if len(a):
                n = a.pop()
                
                if len(b)==0 or b[-1]>n:
                    new_states.append([a[:],b[:]+[n],c[:],steps + ["A to B"]])
                
                if len(c)==0 or c[-1]>n:
                    new_states.append([a[:],b[:],c[:]+[n],steps + ["A to C"]])
                
                a.append(n)
            
            if len(b):
                n = b.pop()
                
                if len(a)==0 or a[-1]>n:
                    new_states.append([a[:]+[n],b[:],c[:],steps + ["B to A"]])
                
                if len(c)==0 or c[-1]>n:
                    new_states.append([a[:],b[:],c[:]+[n],steps + ["B to C"]])
                
                b.append(n)
            
            if len(c):
                n = c.pop()
                
                if len(a)==0 or a[-1]>n:
                    new_states.append([a[:]+[n],b[:],c[:],steps + ["C to A"]])
                
                if len(b)==0 or b[-1]>n:
                    new_states.append([a[:],b[:]+[n],c[:],steps + ["C to B"]])
                
                c.append(n)
                
        states = new_states
        new_states = []
        level +=1
        
print("Tower of Hanoi Solution using BFS: ")
start_state = [3,2,1]
goal_state= []
solution = Hanoi_bfs(start_state,goal_state,[])
if solution:
    print("Solution found!")
    for move in solution:
        print(move)
else:
    print("No Solution")
    
print("Tower of Hanoi Solution using DFS: ")
if not Hanoi_dfs(start_state,goal_state,[]):
    print("No Solution")
    
print("Tower of Hanoi Solution using IDS:")
start_state = [3,2,1]
goal_state= []
Hanoi_ids(start_state,goal_state,[])
