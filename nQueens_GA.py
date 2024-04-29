import random

def create_board(size):
    return [random.randint(0, size-1) for _ in range(size)]

def calculate_attack_count(board):
    size = len(board)
    attack_count = 0
    for i in range(size):
        for j in range(i+1, size):
            if board[i] == board[j] or abs(board[i] - board[j]) == j - i:
                attack_count += 1
    return attack_count

def crossover(parent1, parent2):
    size = len(parent1)
    crossover_point = random.randint(1, size-1)
    child1 = parent1[:crossover_point] + parent2[crossover_point:]
    child2 = parent2[:crossover_point] + parent1[crossover_point:]
    return child1, child2

def mutate(board):
    size = len(board)
    mutated_board = board[:]
    idx = random.randint(0, size-1)
    new_pos = random.randint(0, size-1)
    mutated_board[idx] = new_pos
    return mutated_board

def genetic_algorithm(size, population_size, generations):
    population = [create_board(size) for _ in range(population_size)]
    for _ in range(generations):
        population = sorted(population, key=lambda x: calculate_attack_count(x))
        if calculate_attack_count(population[0]) == 0:
            return population[0]
        new_population = []
        for _ in range(population_size // 2):
            parent1, parent2 = random.choices(population[:population_size//2], k=2)
            child1, child2 = crossover(parent1, parent2)
            new_population.append(mutate(child1))
            new_population.append(mutate(child2))
        population = new_population
    return None

# Example usage:
size = 8  # Size of the chessboard (8x8 for the standard N-Queens problem)
population_size = 100  # Population size
generations = 1000  # Number of generations

solution = genetic_algorithm(size, population_size, generations)
if solution:
    print("Solution found:", solution)
else:
    print("No solution found within the given number of generations.")
