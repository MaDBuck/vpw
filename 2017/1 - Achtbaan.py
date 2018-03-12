movement = {
    "U": 1,
    "D": -1,
    "x": [0, 1, 0, -1],
    "y": [-1, 0, 1, 0]
}
dirD = {
    "L": [3, 0, 1, 2],
    "R": [1, 2, 3, 0]
}
chars = {
    "S": [None] + ["="] + [None] * 2,
    "U": ["#", "/", "#", "\\"],
    "D": ["#", "\\", "#", "/"],
    "V": ["_"] * 4,
    "L": ["_"] * 4,
    "R": ["_"] * 4
}
for p in range(int(input())):
    m = []
    x = 0
    y = 0
    z = 0
    dir = 1
    xS = yS = zS = 0
    for s in input().split()[1]:
        if s == "D":
            z += movement[s]
        if x < 0:
            x += 1
            xS += 1
            column = []
            for ty in range(yS):
                column.append([None] * zS)
            m.insert(0, column)
        if xS <= x:
            xS += 1
            column = []
            for ty in range(yS):
                column.append([None] * zS)
            m.append(column)
        if y < 0:
            y += 1
            yS += 1
            for tx in range(xS):
                m[tx].insert(0, [None] * zS)
        if yS <= y:
            yS += 1
            for tx in range(xS):
                m[tx].append([None] * zS)
        if z < 0:
            z += 1
            zS += 1
            for tx in range(xS):
                for ty in range(yS):
                    m[tx][ty].insert(0, None)
        if zS <= z:
            zS += 1
            for tx in range(xS):
                for ty in range(yS):
                    m[tx][ty].append(None)
        m[x][y][z] = chars[s][dir]
        if s == "U":
            z += movement[s]
        if s in ["L", "R"]:
            dir = dirD[s][dir]
        x += movement["x"][dir]
        y += movement["y"][dir]
    for z in reversed(range(zS)):
        line = []
        for x in range(xS):
            c = "."
            for y in reversed(range(yS)):
                if m[x][y][z] is not None:
                    c = m[x][y][z]
                    break
            line.append(c)
        print(str(p + 1) + " " + "".join(line))
