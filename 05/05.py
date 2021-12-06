def print_field(field):
    for i in range(len(field)):
        print(f"{field[i]}")

with open("inpp") as file:
    content = list(file.read().split("\n"))

    #field = [[0]*991 for i in range(991)]
    field = [[0]*10 for i in range(10)]

    print_field(field)

    for tuple in content:
        start, stop = tuple.split(" -> ")
        x1str, y1str = start.strip().split(",")
        x1 = int(x1str)
        y1 = int(y1str)

        x2str, y2str = stop.strip().split(",")
        x2 = int(x2str)
        y2 = int(y2str)
        
        # draw lines
        if x1 == x2:
            for i in range(min(y1,y2), (max(y1,y2)+1)):
                print(x1)
                field[i][x1] += 1

        if y1 == y2:
            for i in range(min(x1,x2), (max(x1,x2)+1)):
                field[y1][i] += 1

    print("Done")
    print_field(field)

    sol = 0
    for row in field:
        for val in row:
            if val > 1:
                sol += 1
    
    print(f"Solution: {sol}")

    

    



    