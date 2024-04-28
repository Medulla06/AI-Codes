import numpy as np

def total_distance(route):
    d = 0.0
    n = len(route)
    for i in range(n-i):
        if route[i] < route[i+1]:
            d += (route[i+1] - route[i])
        else:
            d += (route[i] - route[i+1]) * 1.5
    return d

def error(route):
    n = len(route)
    d = total_dist(route)
    min_dist = n-1
    return d - min_dist

def adjacent(route, rnd):
    n = len(route)
    result = np.copy(route)
    i = rnd.randint(n)
    j = rnd.randint(n)
    tmp = result[i]
    result[i] = result[j]
    result[j] = tmp
    return result
    
def solve(n_cities, rnd, max_iter, start_temp, alpha):
    curr_temp = start_temp
    soln = np.arrange(n_cities, dtype = np.int64)
    rnd.shuffle(soln)
    print("Guess", soln)
    
    err = error(soln)
    iteration = 0
    interval = (int) (max_iter/10)
    while iteration < max_iter and err > 0.0:
        adj_route = adjacent(soln, rnd)
        adj_err = error(adj_route)
        
        if adj_err <err:
            soln = adj_route
            err  = adj_err
        else:
            accept_p = np.exp((err = adj_err) / curr_temp)
            p = rnd.random()
            if p < accept_p:
                soln = adj_route
                err = adj_err
                
        if iteration % interval == 0:
            print("Iteration %d error = %f temp = %f", (iteration, err, curr_temp))
            
        if curr_temp < 0.0001:
            curr_temp = 0.0001
        else:
            curr_temp *= alpha
        iteration += 1
        
    return soln

def main():
    num_cities = 15
    rnd = np.random.RandomState(4)
    max_iter = 2500
    start_temp = 10000
    alpha = 0.99
    print(" The Travelling Salesman Problem with Simulated Annealing:")
    solve(num_cities, rnd, max_iter,  start_temp, alpha)
