def IDS(a, b, target):
    depth = 0
    while True:
        result = DLS(a, b, target, depth)
        if result != "No Solution":
            return result
        depth += 1

def DLS(a, b, target, depth):
    stack = []
    visited = set()
    stack.append((0, 0, 0))

    while stack:
        current_state = stack.pop()
        visited.add((current_state[1], current_state[2]))
        print((current_state[1], current_state[2]))

        if (current_state[1] == target and current_state[2]==0) or (current_state[2] == target and current_state[1]==0):
            return current_state[0], current_state[1], current_state[2]

        if current_state[0] < depth:
            next_states = generateNextStates(current_state[1:], a, b)
            for next_state in next_states:
                if (next_state[0], next_state[1]) not in visited:
                    stack.append((current_state[0] + 1, next_state[0], next_state[1]))

    return "No Solution"


def generateNextStates(state, a, b):
    next_states = []
    next_states.append((a, state[1]))  # Fill J1
    next_states.append((state[0], b))  # Fill J2
    next_states.append((0, state[1]))  # Empty J1
    next_states.append((state[0], 0))  # Empty J2
    pour_amt = min(state[0], b - state[1])  # Pour from J1 to J2
    next_states.append((state[0] - pour_amt, state[1] + pour_amt))
    pour_amt = min(state[1], a - state[0])  # Pour from J2 to J1
    next_states.append((state[0] + pour_amt, state[1] - pour_amt))
    return next_states


J1, J2, target = 3, 5, 1
print("Path using IDS: ")
IDS(J1, J2, target)
