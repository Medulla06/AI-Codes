from collections import deque

# Two Jug Problem using DFS 
def BFS(a,b,target):
    m={}
    isSolvable = False
    path = []
    q =deque()
    q.append((0,0))
    
    while (len(q)>0):
        u = q.popleft()
        if ((u[0],u[1]) in m): #visited state
            continue
        if ((u[0] > a or u[1] > b or u[0] < 0 or u[1] < 0)):
            continue
        
        path.append([u[0],u[1]]) #solution path
        m[(u[0],u[1])] = 1 #visited state
        
        if (u[0] == target or u[1]==target):
            isSolvable = True
            
            if (u[0]==target):
                if (u[1]!=0):
                    path.append([u[0],0])
            
            else: 
                if (u[0]!=0):
                    path.append([0,u[1]])
            
            for i in range(len(path)):
                print("(",path[i][0],path[i][1],")")
            break
    
        q.append([u[0],b]) #Fill J2
        q.append([a,u[1]]) #Fill J1

        for amt in range(max(a,b)+1):
        
            # Pour from J2 to J1
            c = u[0] + amt
            d = u[1] - amt
        
            if (c==a or (d==0 and d>=0)):
                q.append([c,d])
        
            # Pour from J1 to J2 
            c = u[0] - amt
            d = u[1] + amt
        
            if ((c==0 and c>=0) or d==b):
                q.append([c,d])
            
        q.append([a,0]) # Empty J2
        q.append([0,b]) # Empty J1
    
    if (not isSolvable):
        print("No solution")
        
J1,J2,target = 3,5,1
print("Path using BFS: ")
BFS(J1,J2,target)

# Two Jug Probelm using DFS Algorith
def DFS(a,b,target):
    stack = []
    stack.append((0,0))
    visited = set()
    
    while stack:
        current_state=stack.pop()
        visited.add(current_state)
        print(current_state)
        
        if (current_state[0] == target and current_state[1]==0) or (current_state[1] == target and current_state[0]==0):
            return current_state
            
        next_states = generateNextStates(current_state,a,b)
        for next_state in next_states:
            if next_state not in visited:
                stack.append(next_state)
        
    return "No Solution"

def generateNextStates(state,a,b):
    next_states = []
    next_states.append((a,state[1])) #Fill J1
    next_states.append((state[0],b)) #Fill J2
    next_states.append((0,state[1])) #Empty J1
    next_states.append((state[0],0)) #Empty J2
    pour_amt = min(state[0],b-state[1]) # Pour from J1 to J2
    next_states.append((state[0]-pour_amt,state[1]+pour_amt))
    pour_amt = min(state[1],a-state[0]) # Pour from J2 to J1
    next_states.append((state[0]+ pour_amt,state[1]- pour_amt))
    
    return next_states
    
print("Path using DFS: ")
print(DFS(J1,J2,target))

#Two Jug Problem using IDS
def IDS(a,b,target):
    depth = 0
    while True:
        result = DLS(a,b,target,depth)
        if result!="No Solution":
            return result
        depth+=1
        
def DLS(a,b,target,depth):
    stack = []
    visited = set()
    stack.append((0,0,0))
    
    while stack:
        current_state = stack.pop()
        visited.add((current_state[1],current_state[2]))
        print((current_state[1],current_state[2]))
        
        if (current_state[1] == target and current_state[2]==0) or (current_state[2] == target and current_state[1]==0):
            return current_state[0],current_state[1],current_state[2]
            
        if current_state[0] < depth:
            next_states = generateNextStates(current_state[1:],a,b)
            for next_state in next_states:
                if (next_state[0],next_state[1]) not in visited:
                    stack.append((current_state[0]+1,next_state[0],next_state[1]))
            
    return "No Solution"
    
print("Path using IDS: ")
IDS(J1,J2,target)
