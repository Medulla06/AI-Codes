def knapsack(items, capacity):
    
    max_value = float('-inf')
    knapsack = []
    selected = []
    
    def heuristic(k, weight, value):
        total_weight = weight
        total_value = value
        for i in range(k, len(items)):
            if total_weight + items[i][2] <= capacity: 
                # Checking if the capacity is reached
                total_weight += items[i][2]
                total_value += items[i][1]
            
            else:
                remaining_capacity = capacity - total_weight
                total_value += (remaining_capacity / items[i][2]) * items[i][1]
                # Taking Value to weight ratio as heuristic
                break
        return total_value
    
    # Solving the 0/1 Knapsack problem using DFBB Algorithm
    def dfbb(k, weight, value):
        nonlocal max_value, knapsack
        if weight <= capacity and value > max_value:
            max_value = value
            knapsack = [item[0] for item in selected]
        if k < len(items) and heuristic(k, weight, value) > max_values:
            selected.append(items[k])
            dfbb(k + 1, weight + items[k][2], value + items[k][1] )
            selected.pop()
            dfbb(k + 1, weight, value)
            
    dfbb(0,0,0)
    return knapsack, max_value
    
items = [("item1", 1000, 10),
         ("item2", 4000, 300),
         ("item3", 5000, 1),
         ("item4", 5000, 200),
         ("item5", 2000, 100)]
         
capacity = 400

selected_items, total_value = knapsack(items, capacity)

print("Selected items ", selected_items)
print("Total Value ", total_value)
