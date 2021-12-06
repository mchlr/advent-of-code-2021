def print_field(field):
    for i in range(len(field)):
        print(f"{field[i]}")

with open("input") as file:
    content = list(file.read().split("\n"))

    field = [[0]*991 for i in range(991)]
    #field = [[0]*10 for i in range(10)]

    print_field(field)

    for tuple in content:
        start, stop = tuple.split(" -> ")
        x1str, y1str = start.strip().split(",")
        x1 = int(x1str)
        y1 = int(y1str)

        x2str, y2str = stop.strip().split(",")
        x2 = int(x2str)
        y2 = int(y2str)

        # draw diags
        if (max(x1,x2)-min(x1,x2)) == (max(y1,y2)-min(y1,y2)) or (x1 == y1 and x2 == y2):            
            tmp = range(x1, (x2-1), -1) if x1 > x2 else range(x1, (x2+1))
            diag_length = len(tmp)
            x_range = iter(tmp)
            y_range = iter(range(y1, (y2-1), -1) if y1 > y2 else range(y1, (y2+1)))

            for i in range(diag_length):
                x = next(x_range)
                y = next(y_range)
                field[y][x] += 1

        # draw lines
        elif x1 == x2:
            for i in range(min(y1,y2), (max(y1,y2)+1)):
                print(x1)
                field[i][x1] += 1

        elif y1 == y2:
            for i in range(min(x1,x2), (max(x1,x2)+1)):
                field[y1][i] += 1

    sol = 0
    for row in field:
        for val in row:
            if val > 1:
                sol += 1
    
    print(f"Solution: {sol}")

    

    



    