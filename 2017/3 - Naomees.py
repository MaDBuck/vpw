import re

pattern = re.compile(r"^((ba|di|du))*$")

for i in range(int(input())):
    result = []
    for x in range(5):
        w = input()
        r = pattern.match(w)
        if r is None:
            result.append("onzin")
        else:
            replaced = w.replace("ba", "1").replace("di", "2").replace("du", "3")
            if replaced != replaced[::-1]:
                result.append("onzin")
            else:
                result.append("naomees")
    print("{} {}".format(i + 1, " ".join(result)))
