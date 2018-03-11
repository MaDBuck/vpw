def main(lines):
    inhoud = lines
    a = inhoud[0].split()
    breedte = int(a[0])
    lengte = int(a[1])
    tijd = int(a[2])
    inhoud.pop(0)
    max = checkMax(inhoud, lengte, breedte, tijd)
    for j in range(int(lengte)):
        inhoud.pop(0)
    print(str(i + 1) + " " + str(max))

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
            movablegarfield = i
            volgendevis = vindbestevis(vis, movablegarfield, gegetenvissen)
            if volgendevis is not None:
                afstandbij = afstand(movablegarfield, volgendevis) + 1
        if aantalvissen > max:
            max = aantalvissen
    return max


def vindbestevis(setje, garfield, gegetenvissen):
    min = None
    visje = None
    for vis in setje:
        if vis not in gegetenvissen:
            if min is None or afstand(vis, garfield) < min:
                min = afstand(vis, garfield)
                visje = vis
    return visje


def afstand(tup1, tup2):
    return abs(tup1[0] - tup2[0]) + abs(tup1[1] - tup2[1])