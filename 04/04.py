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

 
def solve():
    with open("inpp") as file:
        content = list(file.read().split("\n"))

        draws = [int(value) for value in content.pop(0).split(",")]
        content.pop(0) # Drop empty line at start
        bingos = []
        tmp = []
        for row in content:
            print(f"Row: {row}")
            if row != "":
                row_list = row.split(" ")
                tmp.append([int(r) for r in row_list if r != ""])
            else:
                bingos.append(tmp)
                tmp = []

        
        #print(bingos)
        print(f"Match with: {draws}")

        # Convert to np.matrix
        bingos = [np.matrix(bb) for bb in bingos]

        for i in range(len(draws)):
            match = np.array(draws[:i])
            for board in bingos:
                if has_bingo(board, match):
                    print(f"Current Match: {match}")
                    print(f"Board: {board} haz bingo!")
                    # "highligh value"
                    # get sum
                    # => solve
                    exit(1)


print("Starting!")
solution = solve()

print(f"Solution:")