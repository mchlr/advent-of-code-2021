import numpy as np

with open("input") as file:
    positions = np.array([int(value) for value in file.read().split(",")])
    low = min(positions)
    max = max(positions)

    results = {}
    for candidate in range(low, (max+1)):
        check = np.array([candidate]*len(positions))
        cost = positions - check
        results[candidate] = sum([(c*-1) if c < 0 else c for c in cost.tolist() ])


best = min(results, key=results.get)
print(f"Solution: {results[best]}")