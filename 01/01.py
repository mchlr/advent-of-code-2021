import numpy

with open("input") as file:
    content = list(file.read().split("\n"))

    lastEntry = None
    increases = 1
    decreases = 0
    
    print(len(content))

    for i in range(len(content)):
        if i == 0:
            continue
        else:
            if content[i] > content[i-1]:
                increases += 1
            else:
                decreases += 1
                print(f"{content[i]} < {content[i-1]} ?")

    # for entry in content:
    #     if lastEntry is not None:
    #         if entry > lastEntry:
    #             increases += 1
    #     lastEntry = entry
    
print("Me")
print(increases)

print("decreases")
print(decreases)

print(decreases + increases)

