import io
import sys

if len(sys.argv) > 1:
    filename = sys.argv[1]
    inp = ''.join(open(filename, "r").readlines())
    sys.stdin = io.StringIO(inp)

def main(lines):
    aantalKeer = int(lines[0])
    lines.pop(0)
    inhoud = lines
    teller =  1
    for i in range(aantalKeer):
        a = inhoud[0].split()
        breedte = int(a[0])
        lengte = int(a[1])
        tijd = int(a[2])
        inhoud.pop(0)
        max = checkMax(inhoud, lengte, breedte, tijd)
        for j in range(int(lengte)):
            inhoud.pop(0)
        print(teller, end=' ')
        print(max)
        teller += 1

def checkMax(arr, lengte, breedte, tijd):
    garfield = ""
    vis = set()
    for i, line in enumerate(arr):
        if i < lengte:
            for j, ch in enumerate(line.replace("\n","")):
                if ch == "E":
                    vis.add((i,j))
                elif ch == "G":
                   garfield = i,j
    # print vis
    # print garfield
    max = 0
    for i in vis:
        if i == (6,8):
            manu = 0
        tick = 0
        aantalvissen = 0
        movablegarfield = garfield
        volgendevis = i
        gegetenvissen = set()
        afstandbij = afstand(movablegarfield, i) + 1
        while volgendevis is not None and tick + afstandbij + afstand(garfield, volgendevis) <= tijd:
            tick += afstandbij
            gegetenvissen.add(volgendevis)
            aantalvissen += 1
            movablegarfield = volgendevis
            volgendevis = vindbestevis(vis, movablegarfield, gegetenvissen, lengte, breedte)
            if volgendevis is not None:
                afstandbij = afstand(movablegarfield, volgendevis) + 1
        if aantalvissen > max:
            max = aantalvissen
    return max


def vindbestevis(setje, garfield, gegetenvissen, lengte, breedte):
    min = None
    visje = None
    for vis in setje:
        if vis not in gegetenvissen:
            if min is None or afstand(vis, garfield) < min:
                min = afstand(vis, garfield)
                visje = vis
            if min is not None and afstand(vis, garfield) == min:
                minafs = 0
                visvroeger = vindomstreken(visje, setje, gegetenvissen, minafs)
                visnu = vindomstreken(vis, setje, gegetenvissen, minafs)
                while(minafs < lengte + breedte and visvroeger is None and visnu is None):
                    minafs += 1
                    visvroeger = vindomstreken(visje, setje, gegetenvissen, minafs)
                    visnu = vindomstreken(vis, setje, gegetenvissen, minafs)
                if visnu is not None:
                    visje = vis
    return visje

def vindomstreken(plaats, set, gegetenvissen, min):
    for vis in set:
        if vis not in gegetenvissen and not vis == plaats:
            if afstand(plaats, vis) <= min:
                return vis
    return None

def afstand(tup1, tup2):
    return abs(tup1[0] - tup2[0]) + abs(tup1[1] - tup2[1])

str = input()
arr = []
while str:
    arr.append(str)
    try:
        str = input()
    except:
        str = False
main(arr)
