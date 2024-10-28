from collections import defaultdict

def dfs_traversal(tree, start, target):
    visited = set()
    stack = [start]
    traversal = []

    while stack:
        node = stack.pop()
        if node in visited:
            continue
        visited.add(node)
        traversal.append(node)

        if node == target: 
            break

        stack.extend(reversed(tree[node]))  

    return traversal


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
            n = int(input("Enter the number of nodes: "))
            if n <= 0:
                print("Please enter a positive integer.")
                continue
            break
        except:
            print("Invalid choice, please enter a valid positive number.")
    
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
    start_node = l[0]
    """print("Available nodes:")
    print(l)"""

    search_node = input("\nEnter the search node: ")

    if search_node in l:
        dfs_traversal_result = dfs_traversal(tree, start_node, search_node)

        if dfs_traversal_result:
            print("Path:", '->'.join(dfs_traversal_result))
            print("Node found")
        else:
            print("Node not found in traversal.")

        print("\nTree Structure:")
        print_pyramid(tree, start_node)
    else:
        print(f"Node {search_node} not found in the tree.")

if __name__ == "__main__":
    main()