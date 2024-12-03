import sys, re

data = sys.stdin.read()
total = 0

def format(entry):
    entry = entry.rstrip(")").lstrip("mul(")
    entry = entry.split(",")
    return entry


muls = re.findall("mul\([0-9]+,[0-9]+\)", data[:(data.index("don't()"))])

sections = data[data.index("don't()"):].split("do()")

for y in sections:
    if (y.find("don't()") == -1):
        muls += re.findall("mul\([0-9]+,[0-9]+\)", y)
    else:
        muls += re.findall("mul\([0-9]+,[0-9]+\)", y[:(y.find("don't()"))])

muls = list(map(format, muls))
print(muls)
for z in muls:
    total += (int(z[0]) * int(z[1]))

print(total)