import itertools


def count():
    budgets = input().split()
    budgets.pop(0)

    n = int(input())

    trucks = [' '] * n

    for t in range(n):
            trucks[t] = input().split()
            trucks[t].pop(0)

    for t in range(len(trucks)):
        for x in range(len(trucks[t])):
            trucks[t][x] = int(trucks[t][x])

    combs = list(itertools.product(*trucks))

    ans = []

    som = 0

    for b in budgets:
        for l in map(sum, combs):
            if l == int(b):
                ans.append(l)

    st = ""

    for i in set(ans):
        st += str(i) + " "

    return st if len(ans) > 0 else "GEEN"


for i in range(1, int(input()) + 1):
    print("{} {}".format(i, count().strip()))
