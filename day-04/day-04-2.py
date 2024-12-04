import sys

data = sys.stdin.read().split("\n")
xmas_count = 0
directions = [[-1, -1], [1, -1], [-1, 1], [1, 1]]

def loc_valid(x, y, x_limit, y_limit):
    return (0 <= x < x_limit) and (0 <= y < y_limit)

for x in range(len(data)):
    for y in range(len(data[0])):
        diagonals = 0
        if data[x][y] == "A":
            for dir_x, dir_y in directions:
                if (loc_valid(x + dir_x, y + dir_y, len(data), len(data[0])) and data[x + dir_x][y + dir_y] == "M"):
                    if (loc_valid(x - dir_x, y - dir_y, len(data), len(data[0])) and data[x - dir_x][y - dir_y] == "S"):
                        diagonals += 1
        if diagonals == 2:
            xmas_count += 1

print(xmas_count)