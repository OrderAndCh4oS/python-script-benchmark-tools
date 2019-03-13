import math
from math import floor


def plot(points, max_x=10000, max_y=10000):
    grid = [[' ' for _ in range(51)] for _ in range(51)]
    for index, point in enumerate(points):
        x = floor(point[0] / max_x * 50)
        y = floor(point[1] / max_y * 50)
        print(x, y)
        grid[y][x] = 'X'

    for row in grid[::-1]:
        for col in row:
            print(col,end='')
        print('')


if __name__ == '__main__':
    plot([[x, int(math.sin(math.radians(x*6)) * 1000)] for x in range(50)], 50, 2250)
