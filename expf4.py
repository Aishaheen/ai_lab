from collections import deque

def Water_Jug_problem(X, Y, target):
    queue = deque()
    visited = set()
    path = {}
    actions = {}

    queue.append((0, 0))
    visited.add((0, 0))
    path[(0, 0)] = None
    actions[(0, 0)] = "Start with both jugs empty"

    while queue:
        current = queue.popleft()
        current_j1, current_j2 = current

        if current_j1 == target or current_j2 == target:
            result_path = []
            applied_rules = []
            while current:
                result_path.append(current)
                applied_rules.append(actions[current])
                current = path[current]
            return result_path[::-1], applied_rules[::-1]

        next_states = [
            ((X, current_j2), f" PRODUCTION 1 Fill Jug 1 to full"),  
            ((current_j1, Y), f" PRODUCTION 2 Fill Jug 2 to full"),
            ((0, current_j2), " PRODUCTION 3 Empty Jug 1"),
            ((current_j1, 0), "PRODUCTION 4 Empty Jug 2"),
            ((current_j1 - min(current_j1, Y - current_j2), current_j2 + min(current_j1, Y - current_j2)), 
             f" PRODUCTION 5 Pour Jug 1 into Jug 2 until it fills"),
            ((current_j1 + min(current_j2, X - current_j1), current_j2 - min(current_j2, X - current_j1)),
             f" PRODUCTION 6 Pour Jug 2 into Jug 1 until it fills"),
            ((X, current_j2 - (X - current_j1)) if current_j1 + current_j2 >= X else (current_j1 + current_j2, 0),
             f" PRODUCTION 7 Pour Jug 2 into Jug 1 until Jug 1 is full"),
            ((current_j1 - (Y - current_j2), Y) if current_j1 + current_j2 >= Y else (0, current_j1 + current_j2),
             f" PRODUCTION 8 Pour Jug 1 into Jug 2 until Jug 2 is full")
        ]

        for state, action in next_states:
            if state not in visited:
                visited.add(state)
                queue.append(state)
                path[state] = current
                actions[state] = action

    return None, None

def check(j1, j2, target):
    if j1 < target and j2 < target:
        print("Not possible: Both jugs are smaller than the target.")
        return True
    return False

def get_positive_integer(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value <= 0:
                print("Invalid input. Please enter a positive integer.")
            else:
                return value
        except ValueError:
            print("Invalid input. Please enter a valid numeric value.")

J1 = get_positive_integer("Enter the volume of Jug 1: ")
J2 = get_positive_integer("Enter the volume of Jug 2: ")
L = get_positive_integer("Enter the target volume: ")

if check(J1, J2, L):
    print("Not possible to measure the target volume.")
else:
    path, applied_rules = Water_Jug_problem(J1, J2, L)
    if path:
        print("\nSolution:")
        for i, state in enumerate(path):
            print(f"Step {i + 1}: {applied_rules[i]}")
            print(f"  Jug 1: {state[0]} , Jug 2: {state[1]} \n")
        print(f"Solution found.")
    else:
        print("No solution found.")