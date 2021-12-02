import numpy

with open("input") as file:
    content = list(file.read().split("\n"))

    d = 0
    h = 0
    a = 0
    for action in content:
        dir, val = action.split(" ")
        val = int(val)

        print(f"dir: {dir}, val: {val}")
        if dir == "forward":
            h += val
            d += a*val
        if dir == "down":
            a += val
        if dir == "up":
            a -= val


print("Solution")
print(d*h)
