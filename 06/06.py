import numpy as np

with open("input") as file:
    fish = [int(f) for f in file.read().split(",")]

    for day in range(80):
        fish = (np.array(fish) - 1).tolist()

        # Check up on dem fish
        new_fish = []
        for i in range(len(fish)):
            if fish[i] < 0:
                new_fish.append(8)
                fish[i] = 6
        fish.extend(new_fish)

print(len(fish))