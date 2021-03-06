import numpy as np

def get_row_as_list(mat, idx):
    return mat[idx,:].tolist()[0]


def get_col_as_list(mat, idx):
    col = mat[:,idx].tolist()
    return [c[0] for c in col]


def has_bingo(board, match):
    # row wise bingo
    for row_idx in range(board.shape[0]):
        row = get_row_as_list(board, row_idx)
        if sum(np.isin(row, match)) == len(row):
            return True

    # col wise bingo
    for col_idx in range(board.shape[1]):
        col = get_row_as_list(board, col_idx)
        if sum(np.isin(col, match)) == len(col):
            return True
    return False


def get_mask(board, match):
    mask = []
    for row_idx in range(board.shape[0]):
        row = get_row_as_list(board, row_idx)
        mask.append([0 if val in match else 1 for val in row])
    return np.matrix(mask)
 

def solve():
    with open("input") as file:
        content = list(file.read().split("\n"))

        draws = [int(value) for value in content.pop(0).split(",")]
        content.pop(0) # Drop empty line at start
        bingos = []
        tmp = []
        for row in content:
            if row != "":
                row_list = row.split(" ")
                tmp.append([int(r) for r in row_list if r != ""])
            else:
                bingos.append(tmp)
                tmp = []

        # Convert to np.matrix
        bingos = [np.matrix(bb) for bb in bingos]

        for i in range(len(draws)):
            match = np.array(draws[:i])
            for board in bingos:
                if has_bingo(board, match):
                    mask = get_mask(board, match)
                    mat_sum = sum(np.asarray(np.multiply(mask, board)).reshape(-1))
                    return mat_sum * match[-1:]


print("Starting!")
print(f"Solution: {solve()}")