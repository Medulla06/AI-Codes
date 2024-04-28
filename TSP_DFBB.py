import sys

class Graph():
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for column in range(vertices)] for row in range(vertices)]
                         
    def printMST(self, parent, key):
        print("Edge \tWeight ")
        for i in range(1, self.V):
            print(parent[i], "-", i, "\t", self.graph[i][parent[i]])
    
    def minKey(self, key, mstSet):
        min_val = sys.maxsize
        min_index = -1
        for v in range(self.V):
            if key[v] < min_val and mstSet[v] == False:
                min_val = key[v]
                min_index = v
        return min_index
        
    def primMST(self):
        key = [sys.maxsize] * self.V
        parent = [-1] * self.V
        key[0] = 0
        mstSet = [False] * self.V
        parent[0] = -1 
        
        for i in range(self.V):
            u = self.minKey(key, mstSet)
            mstSet[u] = True
            
            for v in range(self.V):
                if self.graph[u][v] > 0 and mstSet[v] == False \
                and key[v] > self.graph[u][v]:
                    key[v] = self.graph[u][v]
                    parent[v] = u
        
        self.printMST(parent, key)
        return sum(key)

    def tsp_dfbb(self, start):
        min_cost = sys.maxsize
        min_path = None
        
        def dfs(node, path, visited, cost):
            nonlocal min_cost, min_path
            
            if len(path) == self.V:
                total_cost = cost + self.graph[node][start]  # Add cost to return to start
                if total_cost < min_cost:
                    min_cost = total_cost
                    min_path = path + [start]  # Add start node to complete the loop
                return
            
            for next_node in range(self.V):
                if next_node not in visited:
                    new_cost = cost + self.graph[node][next_node]
                    if new_cost < min_cost:
                        dfs(next_node, path + [next_node], visited | {next_node}, new_cost)

        dfs(start, [start], {start}, 0)
        return min_cost, min_path

if __name__ == '__main__':
    g = Graph(5)
    g.graph = [[0, 12, 10, 19, 8],
               [12, 0, 3, 7, 6],
               [10, 3, 0, 2, 20],
               [19, 7, 2, 0, 4],
               [8, 6, 20, 4, 0]]

    min_cost, min_path = g.tsp_dfbb(0)
    print(f"Minimum tour cost ", min_cost)
    print("Path:", ' -> '.join([chr(65 + node) for node in min_path]))
