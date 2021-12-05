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
        col = get_col_as_list(board, col_idx)
        if sum(np.isin(col, match)) == len(col):
            return True
    return False


def get_mask(board, match):
    mask = []
    for row_idx in range(board.shape[0]):
        row = get_row_as_list(board, row_idx)
        mask.append([0 if val in match else 1 for val in row])
    return np.matrix(mask)


def rekreate_match(last_num, all):
    return all[:(all.index(last_num)+1)]
 

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
        # for later matching
        bingos_lut = [board for board in bingos]
        winners = []

        for i in range(len(draws)):
            match = np.array(draws[:i+1])
            tmp_winners = []

            # Determine last winning board
            if len(match) == len(draws):
                w_obj = winners[-1:][0]
                # last board wins!
                w_board = bingos_lut[w_obj["index"]]
                w_match = rekreate_match(w_obj["last_match"][0], match.tolist())

                # Get marked/unmarked as 0/1 matrix
                mask = get_mask(w_board, w_match)
                mat_sum = sum(np.asarray(np.multiply(mask, w_board)).reshape(-1))

                return mat_sum * w_obj["last_match"][0]

            # Check for other winners
            for idx, board in enumerate(bingos):
                if type(board) is not list:
                    if has_bingo(board, match):
                            tmp_winners.append({"index": idx, "last_match":match[-1:]})
            
            # Remove winners
            for i in tmp_winners:
                bingos[i["index"]] = []
            winners.extend(tmp_winners)
            

print("Starting!")
print(f"Solution: {solve()}")