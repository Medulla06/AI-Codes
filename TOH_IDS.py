def ids(a, b, c):
    states = [[a, b, c, []]]
    new_states = []
    solved = False
    level = 0

    while not solved and states:
        for state in states:
            a, b, c, steps = state
            
            if len(steps) >= 2 ** 3:
                continue
            
            if len(b) == 3:
                print(steps)                
                solved = True
                return
            
            if len(a):
                n = a.pop()
                
                if len(b) == 0 or b[-1] > n:
                    new_states.append([a[:], b[:] + [n], c[:], steps + ["A to B"]])
                
                if len(c) == 0 or c[-1] > n:
                    new_states.append([a[:], b[:], c[:] + [n], steps + ["A to C"]])
                
                a.append(n)
            
            if len(b):
                n = b.pop()
                
                if len(a) == 0 or a[-1] > n:
                    new_states.append([a[:] + [n], b[:], c[:], steps + ["B to A"]])
                
                if len(c) == 0 or c[-1] > n:
                    new_states.append([a[:], b[:], c[:] + [n], steps + ["B to C"]])
                
                b.append(n)
            
            if len(c):
                n = c.pop()
                
                if len(b) == 0 or b[-1] > n:
                    new_states.append([a[:], b[:] + [n], c[:], steps + ["C to B"]])
                
                if len(a) == 0 or a[-1] > n:
                    new_states.append([a[:] + [n], b[:], c[:], steps + ["C to A"]])
                
                c.append(n)
    
        states = new_states
        new_states = []
        level += 1


print("Tower of Hanoi Solution using IDS: ")
start_state = [3, 2, 1]
goal_state = []

ids(start_state, goal_state, [])
