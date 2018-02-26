import string

a = string.ascii_uppercase
for _ in range(int(input())):
    s = input().split(maxsplit=1)
    i = int(s[0])
    zin = s[1]
    result = ""
    for c in zin:
        c = c.upper()
        if c in a or c == " ":
            index = (a.find(c) + 1 - i)
            if index == 0:
                result += " "
            else:
                if index < 0:
                    index += 27
                result += a[index - 1]
        else:
            result += c
    print(result)
