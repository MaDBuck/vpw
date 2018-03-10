import itertools


def count():
    budgets = input().split()[1:]
    trucks = (((int(x) for x in input().split()[1:]) for _ in range(int(input()))))
    ans = []
    m = set(map(sum, itertools.product(*trucks)))
    for b in budgets:
        if int(b) in m:
            ans.append(b)
    return " ".join(ans) if len(ans) > 0 else "GEEN"


for i in range(int(input())):
    print("{} {}".format(i + 1, count()))
