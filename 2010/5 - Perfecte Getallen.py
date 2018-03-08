def getv(min, max):
    for n in range(min, max + 1):
        som = n + sum(i for i in filter(lambda i: n % i == 0, range(1, n // 2 + 1)))
        if som != 0 and som % n == 0:
            return "{} {}".format(n, som // n)
    return "GEEN"


for _ in range(int(input())):
    z = list(int(i) for i in input().split())
    print(getv(z[0], z[1]))
