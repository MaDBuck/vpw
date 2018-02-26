def getv(min, max):
    for n in range(min, max + 1):
        som = n
        for i in range(1, n // 2 + 1):
            if n % i == 0:
                som += i
        if som != 0 and som % n == 0:
            return "{} {}".format(n, som // n)
    return "GEEN"


for _ in range(int(input())):
    i = input().split()
    min = int(i[0])
    max = int(i[1])
    print(getv(min, max))
