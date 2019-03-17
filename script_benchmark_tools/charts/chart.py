from math import floor
from random import randint


def chart(points, max_x=10000, max_y=10000):
    grid = [[' ' for _ in range(26)] for _ in range(26)]
    for index, point in enumerate(points):
        for x in range(0, floor(point / max_y * 25)):
            grid[x][index] = '█'

    for row in grid[::-1]:
        for col in row:
            print(col, end='')
        print('')


if __name__ == '__main__':
    chart([randint(1000, 10000) for _ in range(25)])
