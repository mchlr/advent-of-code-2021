import numpy as np

input = '''
'''

# ALWAYS Y, X
def up(coords):
    return (coords[0]-1, coords[1])

def down(coords):
    return (coords[0]+1, coords[1])

def left(coords):
    return (coords[0], coords[1]-1)

def right(coords):
    return (coords[0], coords[1]+1)

def get_blinks(data):
    blinks = []
    for y in range(len(data)):
        for x in range(len(data[0])):
            if data[y][x] > 9:
                blinks.append((y,x))
    return blinks

def is_in(coords, data):
    for iter_coords in data:
        if coords[0]==iter_coords[0] and coords[1]==iter_coords[1]:
            return True
    return False



data = np.matrix([[int(val) for val in line] for line in [list(line) for line in input.split("\n") if line]])
moves = [
    lambda x: up(x),
    lambda x: down(x),
    lambda x: left(x),
    lambda x: right(x),
    lambda x: up(left(x)),
    lambda x: up(right(x)),
    lambda x: down(left(x)),
    lambda x: down(right(x))
]

flash_count = 0
for step in range(100):
    data = (data + 1).tolist()

    # check flashes
    haz_blinked = []
    blinks = get_blinks(data)
    while len(blinks) > 0:
        for self_coords in blinks:
            for move in moves:
                try:
                    coords = move(self_coords)
                    #
                    if coords[0] < 0 or coords[1] < 0:
                        continue

                    data[coords[0]][coords[1]] += 1
                    if data[coords[0]][coords[1]] > 9 and not (is_in(coords, haz_blinked) or is_in(coords, blinks)):
                        blinks.append((coords[0], coords[1]))
                except IndexError:
                    continue
            haz_blinked.append(self_coords)
            blinks.remove(self_coords)
    # Reset flashed ones
    for self_coords in haz_blinked:
        flash_count += 1
        data[self_coords[0]][self_coords[1]] = 0
    data = np.matrix(data)

print(f"Solution: {flash_count}")