data = '''
2199943210
3987894921
9856789892
8767896789
9899965678
'''

def check_up(x_index, y_index, input):
    if y_index > 0:
        return input[y_index][x_index] < input[y_index-1][x_index] 
    else: 
        return True

def check_down(x_index, y_index, input):
    if y_index < len(input) - 1:
        return input[y_index][x_index] < input[y_index+1][x_index] 
    else: 
        return True

def check_right(x_index, y_index, input):
    if x_index > 0:
        return input[y_index][x_index] < input[y_index][x_index-1] 
    else: 
        return True

def check_left(x_index, y_index, input):
    if x_index < (len(input[0]) - 1):
        return input[y_index][x_index] < input[y_index][x_index+1] 
    else: 
        return True


with open("input") as file:

    #input = [list(d) for d in data.split("\n") if d]
    input = [list(d) for d in file.read().split("\n") if d]
    input = [[int(val) for val in inner] for inner in input]

    sol = 0
    for y_idx in range(len(input)):
        for x_idx in range(len(input[y_idx])):
            up = check_up(x_idx, y_idx, input)
            down = check_down(x_idx, y_idx, input)
            right = check_right(x_idx, y_idx, input)
            left = check_left(x_idx, y_idx, input)

            if up and down and right and left:
                sol += (input[y_idx][x_idx] + 1)

    print(f"Solution: {sol}")