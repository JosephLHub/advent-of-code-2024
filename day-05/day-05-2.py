import sys, math

data = sys.stdin.read().split("\n")

orders = data[:data.index("")]
updates = data[data.index("") + 1:]

total = 0

for x in updates:
    fixed = False
    x = x.split(",")
    for y in orders:
        y = y.split("|")
        if (y[0] in x and y[1] in x):
            if (x.index(y[0]) > x.index(y[1])):
                while (not fixed):
                    fixed = True
                    for z in orders:
                        z = z.split("|")
                        if (z[0] in x and z[1] in x):
                            if (x.index(z[0]) > x.index(z[1])):
                                x.remove(z[1])
                                x.insert(x.index(z[0])+1, z[1])
                                fixed = False
                break


    if (fixed):
        total += int(x[math.floor(len(x) / 2)])
print (total)