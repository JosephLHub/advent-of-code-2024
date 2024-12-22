import sys, copy

original_grid = sys.stdin.read().split("\n")

total = 0

start_pos = [0, 0]
dirs = [[-1, 0], [0, 1], [1, 0], [0, -1]]
letters = ["U", "R", "D", "L"]

for x in range(len(original_grid)):
    original_grid[x] = list(original_grid[x])
    for y in range(len(original_grid[0])):
        if original_grid[x][y] == "^":
            start_pos = [x, y]
            curr_dir = [-1, 0]

rows = len(original_grid)
cols = len(original_grid[0])

for z in range(rows * cols):
    data = copy.deepcopy(original_grid)
    if data[z // rows][z % (cols-1)] == "^":
        continue
    else:
        in_grid = True
        turns = 0
        pos = [start_pos[0], start_pos[1]]
        curr_dir = [-1, 0]
        data[z // len(data)][z % len(data[0])] = "#"
    print(z)

    while in_grid:
        if (0 <= (pos[0] + curr_dir[0]) < len(data) and 0 <= (pos[1] + curr_dir[1]) < len(data[0])):
            to_set = letters[dirs.index(curr_dir)]
            if data[pos[0] + curr_dir[0]][pos[1] + curr_dir[1]] == "#":
                turns += 1
                to_set = "T"
                curr_dir = dirs[turns % len(dirs)]
            if to_set == data[pos[0]][pos[1]]:
                total += 1
                in_grid = False
                break
            data[pos[0]][pos[1]] = to_set
            
            pos[0] += curr_dir[0]
            pos[1] += curr_dir[1]
        else:
            in_grid = False
            break


print("total: ", str(total))