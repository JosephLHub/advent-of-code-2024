import sys

data = sys.stdin.read().split("\n")
total = 0

pos = [0, 0]
dirs = [[-1, 0], [0, 1], [1, 0], [0, -1]]

for x in range(len(data)):
    data[x] = list(data[x])
    for y in range(len(data[0])):
        if data[x][y] == "^":
            pos = [x, y]
            curr_dir = [-1, 0]

in_grid = True
turns = 0
data[pos[0]][pos[1]] = "X"
while in_grid:
    if (0 <= (pos[0] + curr_dir[0]) < len(data) and 0 <= (pos[1] + curr_dir[1]) < len(data[0])):
        if data[pos[0] + curr_dir[0]][pos[1] + curr_dir[1]] == "#":
            turns += 1
            curr_dir = dirs[turns % len(dirs)]
        data[pos[0]][pos[1]] = "X"
        pos[0] += curr_dir[0]
        pos[1] += curr_dir[1]
        print(pos[0], pos[1])
    else:
        data[pos[0]][pos[1]] = "X"
        in_grid = False

for x in data:
    total += x.count("X")
print(total)