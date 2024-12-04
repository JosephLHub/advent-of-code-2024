import sys

data = sys.stdin.read().split("\n")
xmas_count = 0

def loc_valid(x, y, x_limit, y_limit):
    return (0 <= x < x_limit) and (0 <= y < y_limit)

def word_found(data, word, x, y, progress, dir_x, dir_y):
    if progress == len(word):
        return True
    
    if loc_valid(x, y, len(data), len(data[0])) and word[progress] == data[x][y]:
        return word_found(data, word, x + dir_x, y + dir_y, progress + 1, dir_x, dir_y)
    
    return False

def search(data, word):
    word_count = 0
    directions = [[-1, -1], [-1, 0], [0, -1], [1, 0], [0, 1], [1, -1], [-1, 1], [1, 1]]
    for x in range(len(data)):
        for y in range(len(data[0])):
            if data[x][y] == word[0]:
                for dir_x, dir_y in directions:
                    if word_found(data, word, x, y, 0, dir_x, dir_y):
                        word_count += 1
    return word_count

xmas_count += search(data, "XMAS")
print(xmas_count)