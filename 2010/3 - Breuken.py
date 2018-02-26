for _ in range(int(input())):
    s = input().split()
    s1 = list(s[0])
    s2 = list(s[1])
    for c1 in list(s1):
        if c1 in s2:
            s1.remove(c1)
            s2.remove(c1)
    print("{} {}".format(
        "".join(sorted(s1)) if s1 else "1",
        "".join(sorted(s2)) if s2 else "1"
    ))

