def print_tower(rods):
    max_height = max(len(rod) for rod in rods.values())
    for i in range(max_height, 0, -1):
        for rod in ['A', 'B', 'C']:
            if len(rods[rod]) >= i:
                print(f" {rods[rod][i-1]:^3} ", end="")
            else:
                print("  |  ", end="")
        print()
    print("------" * 3)
    print("  A     B     C  \n")

def TowerOfHanoi(n, from_rod, to_rod, aux_rod, rods, step):
    if n == 0:
        return step

    step = TowerOfHanoi(n-1, from_rod, aux_rod, to_rod, rods, step)
    
    disk = rods[from_rod].pop()
    rods[to_rod].append(disk)
    
    step += 1
    print(f"Step {step}: Move disk {disk} from rod {from_rod} to rod {to_rod}")
    print_tower(rods)

    step = TowerOfHanoi(n-1, aux_rod, to_rod, from_rod, rods, step)

    return step

if __name__ == "__main__":
    N = int(input("Enter the number of disks: "))
    
    rods = {
        'A': list(reversed(range(1, N+1))),  
        'B': [],  
        'C': []  
    }
    
    print("Initial Tower:")
    print_tower(rods)
    
    total_steps = TowerOfHanoi(N, 'A', 'C', 'B', rods, step=0)
    
    print(f"Total steps: {total_steps}")
    print("Goal reached: All disks have been moved to rod C!")