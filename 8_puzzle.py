from collections import deque 

class PuzzleState:
    def __init__(self, puzzle, moves=0, previous=None):
        self.puzzle = puzzle
        self.moves = moves
        self.previous = previous
        
    def __eq__(self, other):
        return self.puzzle == other.puzzle
    
    def __str__(self):
        return "\n".join([" ".join(map(str,row)) for row in self.puzzle])
    
    def is_goal(self,goal):
        return self.puzzle == goal.puzzle
        
    def get_possible_moves(self):
        moves = []
        row,col = self.find_empty_space()
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        for dr,dc in directions:
            new_row, new_col = row + dr, col + dc
            if 0 <= new_row < len(self.puzzle) and 0 <= new_col < len(self.puzzle[0]):
                new_puzzle = [list(row) for row in self.puzzle]
                new_puzzle[row][col], new_puzzle[new_row][new_col] = new_puzzle[new_row][new_col], new_puzzle[row][col]
                moves.append(PuzzleState(new_puzzle,self.moves + 1, self ))
        return moves
        
    def find_empty_space(self):
        for i in range(len(self.puzzle)):
            for j in range(len(self.puzzle[i])):
                if self.puzzle[i][j] == 0:
                    return i, j

def bfs(start,goal):
    visited = set()
    queue = deque([start])
    explored_states = []
    while queue:
        current = queue.popleft()
        if current.is_goal(goal):
            return current.moves, explored_states
        visited.add(str(current))
        explored_states.append(current)
        for move in current.get_possible_moves():
            if str(move) not in visited:
                queue.append(move)
                
def dfs(start,goal):
    visited = set()
    stack = deque([start])
    explored_states = []
    while stack:
        current = stack.pop()
        if current.is_goal(goal):
            return current.moves, explored_states
        visited.add(str(current))
        explored_states.append(current)
        for move in reversed(current.get_possible_moves()):
            if str(move) not in visited:
                stack.append(move)
                
def print_states(state,action=None):
    if action:
        print("Action: ", action)
    print("\n".join([" ".join(map(str, row)) for row in state.puzzle]))
    print()

start_state = PuzzleState([[1, 2, 3], [4, 0, 6], [7, 5, 8]])
goal_state = PuzzleState([[1, 2, 3], [4, 5, 0], [7, 8, 6]])

bfs_steps, bfs_explored_states = bfs(start_state, goal_state)
dfs_steps, dfs_explored_states = dfs(start_state, goal_state)

print("Start State:")
print_states(start_state)
print("Goal State:")
print_states(goal_state)

print("BFS Number of steps required:", bfs_steps)
print("BFS States: ")
for state in bfs_explored_states:
    print_states(state)

print("DFS Number of steps required:", dfs_steps)
print("DFS States: ")
for state in dfs_explored_states:
    print_states(state)
