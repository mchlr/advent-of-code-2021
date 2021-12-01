with open("input") as file:
    content = list(file.read().split("\n"))

    # Parse input to use sum
    for i in range(len(content)):
        content[i]=int(content[i])

    lastSum = None
    increases = 0
    for i in range(0, len(content)-2):
        a = sum(content[i:i+3])

        if lastSum is not None:
            if a > lastSum:
                print(a)
                print(lastSum)
                increases += 1
        lastSum = a

print(f"Solution: {increases}")


