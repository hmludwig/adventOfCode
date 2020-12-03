import sys

f = open(sys.argv[1])
data = f.read().split()


def slope(data, x, y):
    cnt = 0
    j = y
    for i in range(x, len(data), x):
        if data[i][j] == '#':
            cnt += 1
        j += y
        j = j % len(data[0])
    return cnt


print(
    slope(data, 1, 1) * slope(data, 1, 3) * slope(data, 1, 5) *
    slope(data, 1, 7) * slope(data, 2, 1))
