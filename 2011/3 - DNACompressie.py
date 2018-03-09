import io
import string
import sys

if len(sys.argv) > 1:
    filename = sys.argv[1]
    inp = ''.join(open(filename, "r").readlines())
    sys.stdin = io.StringIO(inp)


def format(c, count):
    if count >= 4:
        return "-{}{}".format(string.ascii_uppercase[count - 1],
                              c)
    else:
        return c * count


def compress(dna):
    previous = ""
    count = 0
    result = ""
    for c in dna:
        if c != previous:
            result += format(previous, count)
            previous = c
            count = 1
        else:
            count += 1
            if count == 26:
                result += format(previous, count)
                count = 0
    result += format(previous, count)
    return result


def decompress(dna):
    skip = 0
    result = ""
    for i, c in enumerate(dna):
        if skip > 0:
            skip -= 1
        else:
            if c == "-":
                count = string.ascii_uppercase.find(dna[i + 1]) + 1
                c = dna[i + 2]
                result += count * c
                skip = 2
            else:
                result += c
    return result


def dna(s):
    s = s.split(" ")
    if s[0] == "???":
        return decompress(s[1]) + " " + s[1]
    else:
        return s[0] + " " + compress(s[0])


for _ in range(int(input())):
    print(dna(input()))
