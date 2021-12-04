import numpy as np

with open("input") as file:
    content = list(file.read().split("\n"))

    # Convert input
    mat_tmp = []
    for raw in content:
        mat_tmp.append([int(char) for char in raw])
    mat = np.matrix(mat_tmp)
    print(f"Got shape: {mat.shape[0]}x{mat.shape[1]}")

    # Do logic
    avgs = mat.mean(axis=0).tolist()[0]

    # Prepare output
    gamma = ""
    eps = ""
    for avg in avgs:
        if avg > 0.5:
            gamma += "1"
            eps += "0"
        else:
            gamma += "0"
            eps += "1"


print("Solution")
print(int(gamma, 2) * int(eps, 2))

