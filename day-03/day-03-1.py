import sys, re

data = sys.stdin.read().split("\n")
total = 0

def format(entry):
    entry = entry.rstrip(")").lstrip("mul(")
    entry = entry.split(",")
    return entry

for x in data:
    muls = re.findall("mul\([0-9]+,[0-9]+\)", x)
    muls = list(map(format, muls))
    for y in muls:
        total += (int(y[0]) * int(y[1]))

print(total)