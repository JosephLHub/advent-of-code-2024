import sys, math

data = sys.stdin.read().split("\n")

orders = data[:data.index("")]
updates = data[data.index("") + 1:]

total = 0

for x in updates:
    safe = True
    x = x.split(",")
    for y in orders:
        y = y.split("|")
        if (y[0] in x and y[1] in x):
            if (x.index(y[0]) > x.index(y[1])):
                safe = False
                break
    if (safe):
        total += int(x[math.floor(len(x) / 2)])
print (total)