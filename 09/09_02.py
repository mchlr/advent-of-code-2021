data = '''
2199943210
3987894921
9856789892
8767896789
9899965678
'''

visited = []
patches = []

def has_not_visited(x_index, y_index):
    return (x_index, y_index) not in visited


def check_up(x_index, y_index, input):
    if y_index > 0:
        return input[y_index-1][x_index] < 9 and has_not_visited(x_index, y_index-1)
    else: 
        return False

def check_down(x_index, y_index, input):
    if y_index < len(input) - 1:
        return input[y_index+1][x_index] < 9 and has_not_visited(x_index, y_index+1)
    else: 
        return False

def check_right(x_index, y_index, input):
    if x_index < (len(input[0]) - 1):
        return input[y_index][x_index+1] < 9 and has_not_visited(x_index+1, y_index)
    else: 
        return False

def check_left(x_index, y_index, input):
    if x_index > 0:
        return input[y_index][x_index-1]  < 9 and has_not_visited(x_index-1, y_index)
    else: 
        return False

def go(x_index, y_index, path, input):
    visited.append((x_index, y_index))
    path.append((x_index, y_index))

    # UP
    if check_up(x_index, y_index, input):
        path.extend(go(x_index, y_index-1, path, input))
    
    # DOWN
    if check_down(x_index, y_index, input):
        xyz = go(x_index, y_index+1, path, input)
        path.extend(xyz)
    
    # RIGHT
    if check_right(x_index, y_index, input):
        path.extend(go(x_index+1, y_index, path, input))
    
    # LEFT
    if check_left(x_index, y_index, input):
        abc = go(x_index-1, y_index, path, input)
        path.extend(abc)

    return set(path)


with open("input") as file:
    # input = [list(d) for d in data.split("\n") if d]      # debug
    input = [list(d) for d in file.read().split("\n") if d] # prod
    input = [[int(val) for val in inner] for inner in input]

    for y_idx in range(len(input)):
        for x_idx in range(len(input[y_idx])):
            if has_not_visited(x_idx, y_idx):
                if input[y_idx][x_idx] == 9:
                    continue
                else:
                    newPath = go(x_idx, y_idx, [], input)
                    patches.append(newPath)

    patches.sort(key=len, reverse=True)
    sol = len(patches[0])
    for i in range(1, 3):
        sol *= len(patches[i])

    print(f"Solution: {sol}")