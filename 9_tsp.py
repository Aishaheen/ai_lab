from sys import maxsize
from itertools import permutations

def travellingSalesmanProblem(graph, s, V):
    vertex = [i for i in range(V) if i != s]
    min_path = maxsize
    next_permutation = permutations(vertex)
    all_paths = []
    all_shortest_paths = []

    for perm in next_permutation:
        current_pathweight = 0
        k = s
        path = [s + 1]
       
        for j in perm:
            current_pathweight += graph[k][j]
            k = j
            path.append(j + 1)
       
        current_pathweight += graph[k][s]
        path.append(s + 1)
        all_paths.append((path, current_pathweight))

        # Update the shortest paths
        if current_pathweight < min_path:
            min_path = current_pathweight
            all_shortest_paths = [path]
        elif current_pathweight == min_path:
            all_shortest_paths.append(path)

    return all_paths, all_shortest_paths, min_path

def get_integer_input(prompt, min_value=None, max_value=None):
    while True:
        user_input = input(prompt).strip()
        if user_input.isdigit():
            value = int(user_input)
            if (min_value is None or value >= min_value) and (max_value is None or value <= max_value):
                return value
            else:
                print(f"Please enter a value between {min_value} and {max_value}.")
        else:
            print("Invalid input. Please enter a valid integer.")

if __name__ == "__main__":
    V = get_integer_input("Enter the number of cities: ", min_value=1)
    graph = []
   
    for i in range(V):
        while True:
            try:
                row = list(map(int, input(f"Distance for city {i + 1}: ").strip().split(',')))
                if len(row) != V:
                    print(f"Please enter exactly {V} values.")
                    continue
                graph.append(row)
                break
            except ValueError:
                print("Invalid input. Please enter numeric values only, separated by commas.")
   
    s = get_integer_input(f"Enter the starting city (1 to {V}): ", min_value=1, max_value=V) - 1

    all_paths, all_shortest_paths, min_path = travellingSalesmanProblem(graph, s, V)

    print(f"\nTotal number of paths: {len(all_paths)}")
    for i, (path, cost) in enumerate(all_paths, start=1):
        path_str = " -> ".join(map(str, path))
        if cost == min_path:
            print(f"*Path {i}: {path_str}, Cost: {cost}*")
        else:
            print(f"Path {i}: {path_str}, Cost: {cost}")

    
    print(f"\nAll shortest paths with the minimum cost ({min_path}):")
    for i, path in enumerate(all_shortest_paths, start=1):
        path_str = " -> ".join(map(str, path))
        print(f"*Shortest Path {i}: {path_str}*")