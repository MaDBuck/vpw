import functools
import string


@functools.lru_cache()
def verdeling(nummer):
    a = []
    n = 8
    while 1 <= n:
        if nummer >= n:
            a.append(int(n))
            nummer -= n
        else:
            a.append(0)
        n /= 2
    return a[::-1]


def isValid(raster, x, y, first):
    v = verdeling(first)
    # Rechts
    if x < len(raster) - 1 and raster[x + 1][y] is not None:
        if (v[1] + verdeling(raster[x + 1][y])[3]) % 5 != 0:
            return False
    if x == len(raster) - 1 and v[1] != 0:
        return False
    # Links
    if 0 < x and raster[x - 1][y] is not None:
        if (v[3] + verdeling(raster[x - 1][y])[1]) % 5 != 0:
            return False
    if x == 0 and v[3] != 0:
        return False
    # Boven
    if y < len(raster[x]) - 1 and raster[x][y + 1] is not None:
        if (v[2] + verdeling(raster[x][y + 1])[0]) % 5 != 0:
            return False
    if y == len(raster[x]) - 1 and v[2] != 0:
        return False
    # Onder
    if 0 < y and raster[x][y - 1] is not None:
        if (v[0] + verdeling(raster[x][y - 1])[2]) % 5 != 0:
            return False
    if y == 0 and v[0] != 0:
        return False
    return True


def zoekmap(letters, raster):
    if len(letters) > 0:
        for l in set(letters):
            first = l
            x, y = findEmpty(raster)
            raster[x][y] = first
            if isValid(raster, x, y, first):
                lc = letters[:]
                lc.remove(l)
                z = zoekmap(lc, raster)
                if z is not None:
                    return z
                else:
                    raster[x][y] = None
            else:
                raster[x][y] = None
    else:
        return raster


def findEmpty(raster):
    for x in range(len(raster)):
        for y in range(len(raster[x])):
            if raster[x][y] is None:
                return x, y


def loodgieter():
    size = int(input())
    letters = [string.ascii_uppercase.find(c) + 1 for c in input()]
    raster = [None] * size
    for x in range(size):
        raster[x] = [None] * size
    for y in range(size):
        line = input()
        for x in range(size):
            c = line[x]
            if c == "?":
                raster[x][y] = None
            else:
                raster[x][y] = string.ascii_uppercase.find(c) + 1
    return zoekmap(letters, raster)


for _ in range(int(input())):
    l = loodgieter()
    for y in range(len(l[0])):
        print("".join(string.ascii_uppercase[l[x][y] - 1] for x in range(len(l))))
