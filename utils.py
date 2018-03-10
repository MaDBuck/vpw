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




