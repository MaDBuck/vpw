def shift(seq):
    return seq[1:] + [seq[0]]


def updateNieuws(haltes, nieuws):
    for i1, a1 in enumerate(haltes):
        for i2, a2 in enumerate(haltes):
            if a1[0] == a2[0]:
                for i, b in enumerate(nieuws[i2]):
                    if b:
                        nieuws[i1][i] = True


def output(b):
    haltes = []
    nieuws = []
    for i in range(b):
        ritten = [int(x) for x in input().split()]
        ritten.pop(0)
        haltes.append(ritten)
        nieuws.append([False] * i + [True] + [False] * (b - i - 1))
    updateNieuws(haltes, nieuws)
    if done(nieuws):
        return 0
    for i in range(1440):
        for z, a in enumerate(haltes):
            haltes[z] = shift(a)
        updateNieuws(haltes, nieuws)
        if done(nieuws):
            return i + 1
    return "NOOIT"


def done(nieuws):
    for a in nieuws:
        if False in a:
            return False
    return True


for _ in range(int(input())):
    print(output(int(input())))
