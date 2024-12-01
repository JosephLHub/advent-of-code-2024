import sys

data = sys.stdin.read().split("\n")
similarity = 0
left_side = []
right_side = []

for x in data:
    values = x.split("   ")
    left_side.append(int(values[0]))
    right_side.append(int(values[1]))

for y in range(len(left_side)):
    similarity = similarity + (left_side[y] * right_side.count(left_side[y]))

print(similarity)