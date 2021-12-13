import numpy as np

data = '''
'''

def create_matrix(points, y_dim, x_dim):
    mat = np.zeros(shape=((y_dim+1), (x_dim+1)))
    for p in points:
        mat[p[0]][p[1]] = 1

    return mat

def count_uniques(points):
    haz = {}
    count = 0
    for point in points:
        str_point = f"({point[0]},{point[1]})"
        if str_point not in haz:
            count += 1
            haz[str_point] = True
    return count+1

def print_matrix(mat):
    mat.tolist()
    for row in mat:
        row_str = "["
        for val in row:
            row_str += f"{val}, "
        row_str += "]"
        print(row_str)
            

inp = [(line.split(",")) for line in data.split("\n") if line]

# prod -12:
# test -2:

folding = inp[-12:]
del inp[-12:]

# Parse into y, x
parsed = []
for line in inp:
    parsed.append([int(line[1]), int(line[0])])


# get matrix dimensions for folding
y_dim = max([line[0] for line in parsed])
x_dim = max([line[1] for line in parsed])

part = 0

# parsed is [y, x]
for fold in folding:
    instruction, index = fold[0][-5:].split("=")
    instruction = instruction.strip()

    if instruction == "y":
        for line in parsed:
            if line[0] > int(index):
                line[0] = y_dim - line[0]

        y_dim = int(index)-1
        
    elif instruction == "x":
        for line in parsed:
            if line[1] > int(index):
                line[1] = x_dim - line[1]

        x_dim = int(index)-1


    # ONLY FIRST FOLD FOR PART 1
    if part == 0:
        print(f"Solution - Part 1: {len(np.where(create_matrix(parsed, y_dim, x_dim) > 0)[0])}\n")
    part += 1
    # break

# Finish fold
print_matrix(create_matrix(parsed, y_dim, x_dim))