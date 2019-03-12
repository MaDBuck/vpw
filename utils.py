# Sorteren

l = [1, 3, 5, 7, 2]
l.sort(key=lambda x: x, reverse=True)
sorted(l)

# 2D Array printen

array = [[1, 2], [3, 4]]
print(str(array).replace("],", "],\n"))

# Is infinite

import math

math.isinf(float('inf'))

# alphabet

import string

string.ascii_lowercase
string.ascii_uppercase

# n aantal keer splitten maximum

s = "123 456 789"
n = 1
s.split(maxsplit=n)

# input van file lezen

import io
import sys

if len(sys.argv) > 1:
    filename = sys.argv[1]
    inp = ''.join(open(filename, "r").readlines())
    sys.stdin = io.StringIO(inp)

# array kopieren

a = [1, 2, 3]
b = a[:]
b = list(a)

# Object kopieren

import copy

old_list = [[1, 2], [3, 4]]
new_list = copy.deepcopy(old_list)
new_list = list(old_list)
new_list = copy.copy(old_list)
new_list = old_list[:]

# case insensitive regex search

import re

ignorecase = re.compile("test", re.IGNORECASE)
re.match("test", "TesT", re.IGNORECASE)

# Print multidimensional array

import numpy

array = [[0, 1], [1, 0]]
print(numpy.matrix(array))

# transpose array

import numpy

array = [[0, 1], [1, 0]]
print(numpy.transpose(array))

# cache method

from functools import lru_cache as cache


@cache(maxsize=None)
def test():
    pass


# alle permutaties van lijst

import itertools

list(itertools.permutations([1, 2, 3]))

# alle combinaties van meerdere lijsten

import itertools

a = [[1, 2, 3], [4, 5, 6], [7, 8, 9, 10]]
list(itertools.product(*a))


# Manhattan-metriek, met tup1 en tup2 respectievelijk 2 tuples met x, y coördinaat

def afstand(tup1, tup2):
    return abs(tup1[0] - tup2[0]) + abs(tup1[1] - tup2[1])


# Steek alles van stdin in een array en geef deze array door aan de methode main. cf. open(bestand).readlines()

str = input()
arr = []
while str:
    arr.append(str)
    try:
        str = input()
    except:
        str = False
# main(arr)

# Sort dictionary on first or second element

import operator
x = {1: 2, 2: 3, 6: 10, 3: 2}
sorted_x = sorted(x.items(), key=operator.itemgetter(0))
