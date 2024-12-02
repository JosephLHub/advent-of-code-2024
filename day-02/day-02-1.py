import sys

data = sys.stdin.read().split("\n")
safe = 0

for x in data:
    values = x.split(" ")
    values = list(map(int, values))

    if (sorted(values) != values and sorted(values, reverse=True) != values):
        continue

    previous_level = values[0] - 1 # First level value is always safe
    for y in range(len(values)):
        if (abs(values[y] - previous_level) > 3 or abs(values[y] - previous_level) < 1):
            break
        previous_level = values[y]
        if (y == len(values) - 1):
            safe = safe + 1

print(safe)