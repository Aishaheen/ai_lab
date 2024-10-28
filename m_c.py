from collections import deque
def is_valid(state, total_m, total_c):
    m1, c1, b, m2, c2 = state
    return (0 <= m1 <= total_m and 0 <= c1 <= total_c and
            0 <= m2 <= total_m and 0 <= c2 <= total_c and
            (m1 == 0 or m1 >= c1) and (m2 == 0 or m2 >= c2))
def generate_next_state(state, boat_size, total_m, total_c):
    m1, c1, b, m2, c2 = state
    next_states = []
    if b == 0:
        for m in range(0, boat_size + 1):
            for c in range(0, boat_size + 1 - m):
                if m + c > 0 and m + c <= boat_size:
                    new_state = (m1 - m, c1 - c, 1, m2 + m, c2 + c)
                    if is_valid(new_state, total_m, total_c):
                        action = f"{m} missionaries and {c} cannibals crossed to the right"
                        next_states.append((new_state, action))
    else: 
        for m in range(0, boat_size + 1):
            for c in range(0, boat_size + 1 - m):
                if m + c > 0 and m + c <= boat_size:
                    new_state = (m1 + m, c1 + c, 0, m2 - m, c2 - c)
                    if is_valid(new_state, total_m, total_c):
                        action = f"{m} missionaries and {c} cannibals crossed to the left"
                        next_states.append((new_state, action))
    return next_states
def solve_bfs(start_state, boat_size, total_m, total_c):
    queue = deque([(start_state, [], 0)])
    visited=set()
    while queue:
        current_state, actions, moves = queue.popleft()
        if current_state in visited:
            continue
        visited.add(current_state)
        if current_state == (0, 0, 1, total_m, total_c):
            return actions
        for next_state, action in generate_next_state(current_state, boat_size, total_m, total_c):
            if next_state not in visited:
                queue.append((next_state, actions + [action], moves + 1))
    return None
def get_input(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value > 0:
                return value
            else:
                print("Please enter a positive number greater than 0.")
        except ValueError:
            print("Invalid input. Please enter a number.")
total_m = get_input("Enter the total number of missionaries: ")
total_c = get_input("Enter the total number of cannibals: ")
boat_size = get_input("Enter the size of the boat: ")
start_state = (total_m, total_c, 0, 0, 0) 
print(f"Initial State: ({total_m}M, {total_c}C, 0B) | (0M, 0C)")
solution = solve_bfs(start_state, boat_size, total_m, total_c)
s=0;
if solution:
    print("Solution path with actions:")
    current_state = start_state
    for action in solution:
        s=s+1
        m1, c1, b, m2, c2 = current_state
        print(f"Step {s}: ({m1}M, {c1}C) {'->' if b == 0 else '<-'} ({m2}M, {c2}C).\nAction: {action}")
        action_parts = action.split(' ')
        m_crossed = int(action_parts[0])
        c_crossed = int(action_parts[3])
        if b == 0:
            current_state = (m1 - m_crossed, c1 - c_crossed, 1, m2 + m_crossed, c2 + c_crossed)
        else: 
            current_state = (m1 + m_crossed, c1 + c_crossed, 0, m2 - m_crossed, c2 - c_crossed)
    print(f"Solution is found in {len(solution)} moves")
else:
    print("No solution")