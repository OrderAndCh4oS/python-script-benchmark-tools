from math import floor


def plot(points, max_x=10000, max_y=10000):
    grid = [[' ' for _ in range(101)] for _ in range(101)]
    for index, point in enumerate(points):
        x = floor(point[0] / max_x * 100)
        y = floor(point[1] / max_y * 100)
        grid[y][x] = 'X'

    for row in grid[::-1]:
        for col in row:
            print(col,end='')
        print('')


if __name__ == '__main__':
    plot([[100, 100], [200, 200], [500, 500], [1000, 1000], [3000, 3000], [10000, 10000]])
