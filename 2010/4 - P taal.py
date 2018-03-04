import re

p = re.compile("([aieuo]+|ij)p\\1", re.IGNORECASE)
for _ in range(int(input())):
    print(p.sub("\\1", input()))
