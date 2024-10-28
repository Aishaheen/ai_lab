import heapq
goal_state = [['', '', ''], ['', '', ''], ['', '', '']]
input_goal_state = []
moves = [(0, 1, 'right'), (1, 0, 'down'), (0, -1, 'left'), (-1, 0, 'up')]
def heuristic(state):
    h = 0
    for i in range(3):
        for j in range(3):
            if state[i][j] != goal_state[i][j] and state[i][j] != ' ':
                h += 1
    return h
def is_valid(x, y):
    return 0 <= x < 3 and 0 <= y < 3
def print_board(matrix):
    for row in matrix:
        print(' | '.join(str(num) if num != ' ' else " " for num in row))
        print('-' * 9)
def astar(initial_state):
    open_list = [(heuristic(initial_state), 0, initial_state, [])]
    closed_set = set()
    while open_list:
        _, g, current_state, path = heapq.heappop(open_list)        
        if current_state == goal_state:
            return path        
        closed_set.add(tuple(map(tuple, current_state)))
        zero_x, zero_y = 0, 0
        for i in range(3):
            for j in range(3):
                if current_state[i][j] == ' ':
                    zero_x, zero_y = i, j
        for move_x, move_y, move_dir in moves:
            new_x, new_y = zero_x + move_x, zero_y + move_y
            if is_valid(new_x, new_y):
                new_state = [list(row) for row in current_state]
                new_state[zero_x][zero_y], new_state[new_x][new_y] = new_state[new_x][new_y], new_state[zero_x][zero_y]
                if tuple(map(tuple, new_state)) not in closed_set:
                    h = heuristic(new_state)
                    new_path = path + [(new_state, move_dir, h)]  # Include heuristic in the path
                    heapq.heappush(open_list, (g + 1 + h, g + 1, new_state, new_path))
    return None

def input_to_matrix(input_data):
    return [input_data[:3], input_data[3:6], input_data[6:]]
initial_state = [['', '', ''], ['', '', ''], ['', '', '']]
input_initial_state = []
while True:
    print("Enter the initial state with 9 unique comma-separated elements: ")
    c = input().split(',')  # Take input as strings without converting to integers
    remove_duplicates = set(c)
    if len(remove_duplicates) != 9 or ' ' not in remove_duplicates:
        print("Enter space to represent a blank tile and 8 unique values.")
    else:
        initial_state = input_to_matrix(c)
        break
while True:
    print("Enter the goal state : ")
    c = input().split(',')
    remove_duplicates = set(c)
    if len(remove_duplicates) != 9 or ' ' not in remove_duplicates:
        print("Enter space to represent a blank tile and 8 unique values.")
    else:
        goal_state = input_to_matrix(c)
        break
path = astar(initial_state)
if path is not None:
    for step, (state, direction, h) in enumerate(path):
        g = step + 1  # Step number corresponds to g(x)
        
        print(f'Step {g}: heuristic value: f(x) = {g - 1} + {h}')
        print(f'Move the 0 to {direction}')
        print_board(state)
        print()
    print("Solution found!")
else:
    print('No solution found.')