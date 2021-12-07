import numpy as np

with open("input") as file:
    positions = np.array([int(value) for value in file.read().split(",")])
    results = {}
    for candidate in range(min(positions), max(positions)+1):
        results[candidate] = 0
        for pos in positions:
            results[candidate] += sum(range(1, (max(pos,candidate)-min(pos,candidate))+1))

best = min(results, key=results.get)
print(f"Solution: {results[best]}")