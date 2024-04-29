import random
import math

def calculate_attack_count(board):
    n = len(board)
    attack_count = 0
    for i in range(n):
        for j in range(i+1, n):
            if board[i] == board[j] or abs(board[i] - board[j]) == j - i:
                attack_count += 1
    return attack_count

def print_board(board):
    n = len(board)
    for i in range(n):
        row = ['.'] * n
        row[board[i]] = 'Q'
        print(' '.join(row))

def nqueens_simulated_annealing(n, max_iterations, initial_temperature, cooling_rate):
    current_solution = list(range(n))
    random.shuffle(current_solution)
    current_energy = calculate_attack_count(current_solution)
    
    temperature = initial_temperature
    
    for _ in range(max_iterations):
        if current_energy == 0:
            return current_solution
        
        # Choose a random neighboring solution
        new_solution = current_solution[:]
        i, j = random.sample(range(n), 2)
        new_solution[i], new_solution[j] = new_solution[j], new_solution[i]
        new_energy = calculate_attack_count(new_solution)
        
        # Calculate the energy difference
        energy_difference = new_energy - current_energy
        
        # If the new solution is better or if it's worse but within the acceptance probability, accept it
        if energy_difference < 0 or random.random() < math.exp(-energy_difference / temperature):
            current_solution = new_solution
            current_energy = new_energy
        print(current_solution)
        # Cool down the temperature
        temperature *= cooling_rate
    
    return None  # No solution found

# Example usage:
n = 8  # Size of the chessboard (8x8 for the standard N-Queens problem)
max_iterations = 10000  # Maximum number of iterations
initial_temperature = 1000  # Initial temperature
cooling_rate = 0.95  # Cooling rate

solution = nqueens_simulated_annealing(n, max_iterations, initial_temperature, cooling_rate)
if solution:
    print("Solution found:")
    print_board(solution)
else:
    print("No solution found within the given number of iterations.")
