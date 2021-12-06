import numpy as np



with open("input") as file:
    raw = [int(f) for f in file.read().split(",")]
    fish = {}
    for value in raw:
        if value in fish:
            fish[value] += 1
        else:
            fish[value] = 1


    for day in range(256):
        ffish = {}
        new_fish = 0
        for k in fish.keys():
            k_new = k-1
            if k_new < 0:
                ffish[8] = fish[k]
                k_new = 6
            
            if k_new in ffish:
                ffish[k_new] += fish[k]    
            else:
                ffish[k_new] = fish[k]

        fish = ffish

print(f"Solution: {sum(fish.values())}")
