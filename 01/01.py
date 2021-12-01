import numpy

with open("input") as file:
    content = list(file.read().split("\n"))

    lastEntry = None
    increases = 1
    for i in range(len(content)):
        if i == 0:
            continue
        else:
            if content[i] > content[i-1]:
                increases += 1


print(f"Solution: {increases}")


