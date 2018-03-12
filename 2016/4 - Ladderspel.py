#Algoritme werkt enkel op gebruikt van ladders
#Beter algoritme zoeken

def count():
    dimensie = int(input())

    tot = int(input())

    ladders = {}
    slangen = {}
    for _ in range(tot):
        x, y = input().split()
        if int(x) < int(y):
            ladders[int(x)] = int(y)
        else:
            slangen[int(x)] = int(y)

    return lds(dimensie, ladders, slangen)


def lds(d, l, s):
    pos = 0

    c = 0

    einde = d * d

    while pos < einde:
        tmp = pos
        for i in range(1, 7):
            if pos + i in l and pos + i not in s:
                tmp = l[pos + i] if l[pos + i] > tmp else tmp
            if pos + i not in s and pos + i > tmp:
                tmp = pos + i

        if pos == tmp:
            for i in range(1, 7):
                if pos + i not in s:
                    tmp = pos + i
        c += 1

        pos = tmp

    return c


for i in range(1, int(input()) + 1):
    print("{} {}".format(i, count()))

    
