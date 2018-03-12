import io
import sys

if len(sys.argv) > 1:
    filename = sys.argv[1]
    inp = ''.join(open(filename, "r").readlines())
    sys.stdin = io.StringIO(inp)

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
    m = {}
    x = y = z = 0
    dir = 1
    for s in input().split()[1]:
        if s == "D":
            z += movement[s]
        if x not in m:
            m[x] = {}
        if y not in m[x]:
            m[x][y] = {}
        if z not in m[x][y]:
            m[x][y][z] = {}
        m[x][y][z] = chars[s][dir]
        if s == "U":
            z += movement[s]
        if s in ["L", "R"]:
            dir = dirD[s][dir]
        x += movement["x"][dir]
        y += movement["y"][dir]
    del x, y, z
    minX = min(m.keys())
    maxX = max(m.keys())
    minY = maxY = minZ = maxZ = None
    for x in m:
        for y in m[x]:
            for z in m[x][y].keys():
                if minZ is None or z < minZ:
                    minZ = z
                if maxZ is None or z > maxZ:
                    maxZ = z
        if minY is None or y < minY:
            minY = y
        if maxY is None or y > maxY:
            maxY = y
    del x, y, z
    for z in range(maxZ, minZ - 1, -1):
        line = []
        for x in range(minX, maxX + 1):
            c = "."
            for y in sorted(m[x], reverse=True):
                try:
                    if m[x][y][z] is not None:
                        c = m[x][y][z]
                        break
                except KeyError:
                    pass
            line.append(c)
        print(str(p + 1) + " " + "".join(line))
