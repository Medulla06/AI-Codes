import sys
from collections import deque

# The Travelling Salesman Problem using Breadth First Search (BFS)
n = 5
g = [[0,12,10,19,8],
        [12,0,3,7,6],
        [10,3,0,2,20],
        [19,7,2,0,4],
        [8,6,20,4,0]]

def tsp(graph,root):
    queue = deque([(root, [root])])
    min_cost = sys.maxsize

    while queue:
        current_node, path = queue.popleft()

        if len(path) == len(graph):
            total_cost = sum(graph[path[i-1]][path[i]] for i in range(1,n))
            total_cost += graph[path[-1]][path[0]] #return to start
            min_cost = min(min_cost, total_cost)
        
        else:
            for next_node in range(n):
                if next_node not in path:
                    queue.append((next_node, path + [next_node]))

    return min_cost

print(tsp(g,0))
