import sys

data = sys.stdin.read().split("\n")
sum_total = 0
left_side = []
right_side = []

for x in data:
    values = x.split("   ")
    left_side.append(int(values[0]))
    right_side.append(int(values[1]))

left_side.sort()
right_side.sort()

for y in range(len(left_side)):
    sum_total = sum_total + abs(left_side[y] - right_side[y])

print(sum_total)