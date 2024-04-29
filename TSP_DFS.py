import sys

# The Travelling Salesman Problem using Depth First Search (DFS)
n = 5
graph = [
    [0, 12, 10, 19, 8],
    [12, 0, 3, 7, 6],
    [10, 3, 0, 2, 20],
    [19, 7, 2, 0, 4],
    [8, 6, 20, 4, 0]
]

def tsp_dfs(graph, start):
    visited = [False] * n
    path = [start]
    min_cost = [sys.maxsize]
    iterations = [0]  # Variable to count the iterations

    def dfs(current_node, depth, cost):
        iterations[0] += 1  # Increment the iteration count
        visited[current_node] = True

        if depth == n:
            cost += graph[current_node][start]  # return to start
            min_cost[0] = min(min_cost[0], cost)
        
        else:
            for next_node in range(n):
                if not visited[next_node]:
                    new_cost = cost + graph[current_node][next_node]
                    dfs(next_node, depth + 1, new_cost)
        
        visited[current_node] = False

    dfs(start, 1, 0)
    print("Number of iterations:", iterations[0])  # Print the number of iterations
    return min_cost[0]

print("Minimum cost using DFS:", tsp_dfs(graph, 0))
