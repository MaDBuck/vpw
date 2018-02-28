import re


def output(regel):
    regel = re.sub("10( |$)", "10 0\\1", regel)
    kegels = list(int(s) for s in regel.split())
    worpen = [0] * 10
    bonussen = [0] * 10
    for i in range(0, 19, 2):
        k1 = kegels[i]
        k2 = kegels[i + 1]
        if not 0 <= k1 <= 10 or not 0 <= k2 <= 10 or not 0 <= k1 + k2 <= 10:
            return "ONGELDIG"
        for index, w in ((index, w) for index, w in enumerate(bonussen) if w != 0):
            bonussen[index] -= 1
            worpen[index] += k1
            if index < 9:
                worpen[index + 1] += k1
        if k1 != 10:
            for index, w in ((index, w) for index, w in enumerate(bonussen) if w != 0):
                bonussen[index] -= 1
                worpen[index] += k2
                if index < 9:
                    worpen[index + 1] += k2
        if k1 == 10:
            bonussen[i // 2] += 2
        elif k1 + k2 == 10:
            bonussen[i // 2] += 1
        score = (worpen[i // 2 - 1] if i > 0 else 0) + k1 + k2
        worpen[i // 2] = score
    if bonussen[9] == 2:
        k1 = kegels[20]
        k2index = 21
        if k1 == 10:
            k2index = 22
            if kegels[21] != 0:
                return "ONGELDIG"
        k2 = kegels[k2index]
        if k2 == 10:
            if kegels[k2index + 1] != 0 or len(kegels) != k2index + 2:
                return "ONGELDIG"
        elif len(kegels) != (k2index + 1):
            return "ONGELDIG"
        worpen[9] += k1 + k2
        if bonussen[8] == 1:
            worpen[8] += k1
            worpen[9] += k1
    elif bonussen[9] == 1:
        k1 = kegels[20]
        if k1 == 10:
            if kegels[21] != 0 or len(kegels) != 22:
                return "ONGELDIG"
        elif len(kegels) != 21:
            return "ONGELDIG"
        worpen[9] += k1
        if bonussen[8] == 1:
            worpen[8] += k1
    else:
        if not len(kegels) == 20:
            return "ONGELDIG"
    return " ".join(str(x) for x in worpen)


for _ in range(int(input())):
    print(output(input()))
