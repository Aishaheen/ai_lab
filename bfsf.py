from collections import defaultdict, deque

def bfs(tree, start, search):
    visited = set()
    queue = deque([start])
   
    path = []
    while queue:
        node = queue.popleft()
        if node in visited:
            continue
        visited.add(node)
        path.append(node)
        if node == search:
            return path
        for n in tree[node]:
            if n not in visited:
                queue.append(n)
    return path

def opath(tree, start, search):
    visited = set()
    queue = deque([(start, [start])]) 

    while queue:
        node, path = queue.popleft()
        if node == search:
            return path 
        visited.add(node)
        for neighbor in tree[node]:
            if neighbor not in visited:
                queue.append((neighbor, path + [neighbor]))  
    return None  

def print_pyramid(tree, start):
    def get_level(node, level=0, levels=None):
        if levels is None:
            levels = defaultdict(list)
        levels[level].append(node)
        for child in sorted(tree[node]):
            get_level(child, level + 1, levels)
        return levels
   
    levels = get_level(start)
    max_width = len(levels[max(levels)]) * 4
   
    for level in sorted(levels):
        level_nodes = levels[level]
        spacing = max_width // (2 ** (level + 1))
        line = (" " * spacing).join(f"{node:4}" for node in level_nodes)
        print(" " * (max_width // 2 - len(line) // 2) + line)

def main():
    while True:
        try:
            n = int(input("Enter the number of nodes : "))
            if n < 1 or n > 100:
                print("Please enter a number between 1 and 50.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
   
    tree = defaultdict(list)
    nodes = set()
   
    print("Enter each node and its adjacent nodes in each line:")
    for _ in range(n):
        line = input().strip().split()
        node = line[0]
        children = line[1:]
        tree[node].extend(children)
        nodes.add(node)
        nodes.update(children)
   
    if not nodes:
        print("No nodes were entered.")
        return
   
    l = list(tree.keys())
    print("Available nodes:")
    print(l)
    start_node = l[0]
    search_node = input("\nEnter the search node: ")
   
    if search_node in l:
        bfs_result = bfs(tree, start_node, search_node)
        optimal = opath(tree, start_node, search_node)
        if bfs_result:
            print("Path: ", ' -> '.join(bfs_result))
            print("Node found")
        else:
            print("Node not found")
            
        print("\nTree Structure:")
        print_pyramid(tree, start_node)
    else:
        print(f"Node {search_node} not found in the tree")    
   
if __name__ == "__main__":
    main()