import operator

def main(input):
    aantal = int(input.pop(0))
    for i in range(aantal):
        h = int(input.pop(0))
        b = int(input.pop(0))
        area = input[:h]
        d = verwerk(h, b, area)
        s = []
        for (r, k) in d:
            s.append("{0} {1}".format(r, k))
        try:
            print(str(i + 1) + " " + " ".join(s)).strip()
        except:
            print(str(i + 1) + " " + " ".join(s))
        input = input[h:]

def verwerk(hoogte, breedte, gebied):
    bezocht = []
    dict = {}
    for i in range(hoogte):
        for j in range(breedte):
            if gebied[i][j] == "+" and (i, j) not in bezocht:
                bezocht.append((i, j))
                (bezocht, grootte) = recursief(i, j, hoogte, breedte, gebied, bezocht, 1)
                dict[grootte] = dict.get(grootte, 0) + 1
    return sorted(dict.items(), key=operator.itemgetter(0))

def recursief(r, k, h, b, gebied, bezocht, grootte):
    rx = [1, -1, 0, 0]
    kx = [0, 0, 1, -1]
    for i in range(4):
        if 0 <= r + rx[i] < h and 0 <= k + kx[i] < b:
            if (r + rx[i], k + kx[i]) not in bezocht:
                if gebied[r + rx[i]][k + kx[i]] == "+":
                    bezocht.append((r + rx[i], k + kx[i]))
                    (bezocht, grootte) = recursief(r + rx[i], k + kx[i], h, b, gebied, bezocht, grootte + 1)
    return (bezocht, grootte)


s = input()
arr = []
while s:
    arr.append(s)
    try:
        s = input()
    except:
        s = False
main(arr)