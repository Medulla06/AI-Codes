from collections import deque

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
                print(path[i][0],path[i][1])
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