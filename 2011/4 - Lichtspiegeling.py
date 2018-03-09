def move(x, y, raster, dir):
    if dir == 0:
        y += 1
    if dir == 1:
        x += 1
    if dir == 2:
        y -= 1
    if dir == 3:
        x -= 1
    if raster[x][y] == "\\":
        if dir == 0:
            dir = 1
        elif dir == 1:
            dir = 0
        elif dir == 2:
            dir = 3
        elif dir == 3:
            dir = 2
    elif raster[x][y] == "/":
        if dir == 0:
            dir = 3
        elif dir == 1:
            dir = 2
        elif dir == 2:
            dir = 1
        elif dir == 3:
            dir = 0
    # print(f"moved to {raster[x][y]} {x} {y} {dir}")
    return x, y, dir

def kaats(x, y, raster):
    if x == 0:
        dir = 1
    elif x == len(raster) - 1:
        dir = 3
    elif y == 0:
        dir = 0
    elif y == len(raster[0]) - 1:
        dir = 2
    # else:
    #     print(f"INVALID: {x} {y}")
    x, y, dir = move(x, y, raster, dir)
    while not raster[x][y].isalpha():
        x, y, dir = move(x, y, raster, dir)
    return raster[x][y]


def r():
    size = input().split(" ")
    m = int(size[0])
    n = int(size[1])
    raster = [None] * (n + 2)
    for x in range(n + 2):
        raster[x] = [None] * (m + 2)
    for y in range(m + 2):
        line = input()
        for x in range(n + 2):
            if len(line) > x:
                raster[x][y] = line[x]
    for x in range(n + 2):
        for y in range(m + 2):
            if raster[x][y] is not None and raster[x][y].isalpha():
                # print(f"{x} {y} {raster[x][y]}")
                k = kaats(x, y, raster)
                if k != raster[x][y]:
                    return "verkeerd"
    return "correct"


for _ in range(int(input())):
    print(r())
