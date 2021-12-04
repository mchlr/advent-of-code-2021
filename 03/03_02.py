import posixpath
import numpy as np
import collections

def match(rows, col_idx, is_co2):
    if 1 < len(rows):
        # Make average for col at col_idx
        avg = round(np.matrix(rows).mean(axis=0).tolist()[0][col_idx]+0.01)
        if is_co2:
            avg = 1-avg

        for i in range(len(rows)):
            if rows[i][col_idx] != avg:
                del rows[i][:]

        # Actually remove deletet elems
        rows = [x for x in rows if x]

        col_idx += 1
        return match(rows, col_idx, is_co2)
    else:
        # Winning number
        return rows[0]


with open("input") as file:
    content = list(file.read().split("\n"))

    # Convert input
    mat_tmp = []
    for raw in content:
        mat_tmp.append([int(char) for char in raw])
    mat = np.matrix(mat_tmp)
    print(f"Got shape: {mat.shape[0]}x{mat.shape[1]}")

    oxy = match(mat.tolist(), 0, False)
    co2 = match(mat.tolist(), 0, True)

print(f"oxy: {oxy}")
print(f"co2: {co2}")

print(f"Solution: {int(''.join([str(i) for i in oxy]), 2) * int(''.join([str(i) for i in co2]), 2)}")