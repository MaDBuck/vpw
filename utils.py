# Alfabet
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

# case insensitive regex search
import re
ignorecase = re.compile("test", re.IGNORECASE)
re.match("test", "TesT", re.IGNORECASE)

# Create alphabet list of lowercase letters
alphabet = []
for letter in range(97,123):
    alphabet.append(chr(letter))
 
>>> alphabet
['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
 
# Create alphabet list of uppercase letters
alphabet = []
for letter in range(65, 91):
    alphabet.append(chr(letter))
 
>>> alphabet
['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
