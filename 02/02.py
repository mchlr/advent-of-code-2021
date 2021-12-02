import numpy

with open("input") as file:
    content = list(file.read().split("\n"))

    d = 0
    h = 0
    for action in content:
        dir, val = action.split(" ")
        val = int(val)

        print(f"dir: {dir}, val: {val}")
        if dir == "forward":
            h += val
        if dir == "down":
            d += val
        if dir == "up":
            d -= val


print("Solution")
print(d*h)
