import itertools


def count():
    budgets = list(int(x) for x in input().split()[1:])
    trucks = list(list(int(x) for x in input().split()[1:]) for _ in range(int(input())))
    minV = sum(min(t) for t in trucks)
    maxV = max(budgets)
    budgets = list(filter(lambda x: minV <= x, budgets))
    if len(budgets) == 0:
        return "GEEN"
    for t in trucks:
        t = set(filter(lambda x: minV - min(t) + x <= maxV, t))
    ans = []
    m = set(map(sum, itertools.product(*trucks)))
    for b in budgets:
        if b in m:
            ans.append(str(b))
    return " ".join(ans) if len(ans) > 0 else "GEEN"


for i in range(int(input())):
    print("{} {}".format(i + 1, count()))
