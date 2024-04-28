import sys

class Graph():
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for column in range(vertices)]
                        for row in range(vertices)]
                         
    def printMST(self, parent, key):
        print("Edge \tWeight ")
        heuristic = 0
        for i in range(1, self.V):
            print(parent[i], "-", i, "\t", self.graph[i][parent[i]])
            heuristic += self.graph[i][parent[i]]
        print("Heuristic is ", heuristic)
    
    def minKey(self, key, mstSet):
        min = sys.maxsize
        for v in range(self.V):
            if key[v] < min and mstSet[v] == False:
                min = key[v]
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
                    
        #self.printMST(parent,key)
        return sum(key)
            
    def tsp(self, start):
        open_set = [(start, [start], 0, self.primMST())]
        min_cost = sys.maxsize
        min_path = None
        
        while open_set:
            current_node, path, cost, heuristic = min(open_set, key=lambda x: x[2] + x[3])
            open_set.remove((current_node, path, cost, heuristic))
            
            if len(path) == self.V:
                total_cost = cost + self.graph[path[-1]][path[0]]
                min_cost = min(min_cost, total_cost)
                min_path = path + [path[0]]
            else:
                for next_node in range(self.V):
                    if next_node not in path:
                        next_cost = cost + self.graph[current_node][next_node]
                        next_heuristic = heuristic - self.primMST() + self.graph[current_node][next_node]
                        next_path = path + [next_node]
                        open_set.append((next_node, next_path, next_cost, next_heuristic))
            #print("Node explored: ", current_node, "Heuristic: ", heuristic)
        return min_cost, min_path

if __name__ == '__main__':
    g = Graph(5)
    g.graph = [[0,12,10,19,8],
               [12,0,3,7,6],
               [10,3,0,2,20],
               [19,7,2,0,4],
               [8,6,20,4,0]]
    #g.primMST()
    
    min_cost, min_path = g.tsp(0)
    print("Minimum cost of the Travelling Salesman Problem using A* Algorithm is", min_cost)
    print("Path:", '->'.join([chr(65 + node) for node in min_path]))
