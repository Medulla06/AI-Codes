import sys

# The Travelling Salesman Problem using Depth First Search (DFS)
n = 5
g = [[0,12,10,19,8],
        [12,0,3,7,6],
        [10,3,0,2,20],
        [19,7,2,0,4],
        [8,6,20,4,0]]

def tsp(graph,root):
    stack = [(root,[root])]
    min_cost = sys.maxsize

    while stack:
        current_node, path = stack.pop()
        
        if len(path) == n:
            total_cost = sum(graph[path[i-1]][path[i]] for i in range(1,n))
            total_cost += graph[path[-1]][path[0]] #return to start
            min_cost = min(min_cost, total_cost)

        else:
            for next_node in range(n):
                if next_node not in path:
                    stack.append((next_node, path + [next_node]))
    
    return min_cost

print(tsp(g,0))



