import matplotlib.pyplot as plt


def slanting_product(a, b, c, d):
    return (b[0] - a[0]) * (d[1] - c[1]) - (b[1] - a[1]) * (d[0] - c[0])


def draw_line_and_point(a, b, c):
    plt.plot([a[0], b[0]], [a[1], b[1]], color='blue')
    plt.plot(c[0], c[1], 'ro')
    plt.plot(b[0], b[1], 'x', color='blue')
    plt.show()


def determine_the_location_of_the_point(a, b, c):
    # c - the point for which we want to know the position
    det = slanting_product(a, b, a, c)
    if det < 0:
        return 'right'
    elif det > 0:
        return 'left'
    else:
        return 'on line'

import random

class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed = (0, 0)

    def set_speed(self, speed):
        self.speed = speed

    def set_random_speed(self, value, seed=0):
        if seed != 0:
            random.seed(seed)
        r = random.uniform(-1, 1)
        self.speed = (value * r, value * (r - 1) if r > 0 else value * (r + 1))

    def move(self):
        self.x += self.speed[0]
        self.y += self.speed[1]

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __str__(self):
        return str(self.x) + "," + str(self.y)

if __name__ == '__main__':
    points = [[1, 2], [2, 3], [3, 4]]
    print(determine_the_location_of_the_point(*points))  # 3rd point for which we want to know the position
    draw_line_and_point(*points)
