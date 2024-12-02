import sys

data = sys.stdin.read().split("\n")
safe = 0

for x in data:
    values = x.split(" ")
    values = list(map(int, values))

    if (sorted(values) != values and sorted(values, reverse=True) != values):
        fails = True
        for z in range(len(values)):
            if (sorted(values[:z] + values[z+1:]) == values[:z] + values[z+1:] or sorted(values[:z] + values[z+1:], reverse=True) == values[:z] + values[z+1:]):
                fails = False
        if (fails):
            continue

    previous_level = values[0] - 1 # First level value is always safe
    for y in range(len(values)):
        if (abs(values[y] - previous_level) > 3 or abs(values[y] - previous_level) < 1):
            fails = False
            new_values = values[:y] + values[y+1:]
            for w in range(len(new_values)):
                if (abs(new_values[w] - previous_level) > 3 or abs(new_values[w] - previous_level) < 1):
                    fails = True
                previous_level = new_values[w]
            if (fails):
                break

        previous_level = values[y]
        if (y == len(values) - 1):
            safe = safe + 1

print(safe)