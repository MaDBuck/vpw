import io
import sys

if len(sys.argv) > 1:
    filename = sys.argv[1]
    inp = ''.join(open(filename, "r").readlines())
    sys.stdin = io.StringIO(inp)

def main(array):
    aantalKeer = array[0]
    array.pop(0)
    lengte = array[0][0]
    breedte = array[0][1]
    array.pop(0)
    opl = losOp(array, lengte, breedte)
    for _ in range(lengte):
        array.pop(0)
    print(opl)


def losOp(array, lengte, breedte):
    # Zet input om in 2 arrays die resp de groepen en de waarden bevatten.
    groepen = []
    waarden = []
    for rij in range(lengte):
        groepenrij =[]
        waardenrij = []
        for kolom in range(breedte):
            groepenrij.append(array[rij][kolom])
            waardenrij.append(array[rij][kolom + 1])
        groepen.append(groepenrij)
        waarden.append(waardenrij)
    



str = input()
arr = []
while str:
    arr.append(str)
    try:
        str = input()
    except:
        str = False
main(arr)