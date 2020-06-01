import time

import matplotlib.pyplot as plt
import numpy as np


def annotate_points(*points):
    for index, point in enumerate(points):
        plt.annotate('p' + str(index + 1), (point[0] + 0.015, point[1] + 0.015))


def distance(p1: np.array, p2: np.array) -> float:
    return np.sqrt((p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2)


def identify_closest_pair(x: list, y: list) -> tuple:
    if len(x) <= 3:
        if len(x) == 2:
            return x
        if distance(x[0], x[1]) < distance(x[0], x[2]) and distance(x[0], x[1]) < distance(x[1], x[2]):
            return x[0], x[1]
        if distance(x[0], x[2]) < distance(x[0], x[1]) and distance(x[0], x[2]) < distance(x[1], x[2]):
            return x[0], x[2]
        return x[1], x[2]

    n = len(x)
    sep = n // 2
    x_sep = x[sep]

    x_left = x[:sep + 1]
    x_right = x[sep:]
    y_left = []
    y_right = []

    for point in y:
        if point[0] < x_sep[0]:
            y_left.append(point)
        else:
            y_right.append(point)

    min_in_left = identify_closest_pair(x_left, y_left)
    min_in_right = identify_closest_pair(x_right, y_right)

    if distance(*min_in_left) < distance(*min_in_right):
        total_min = distance(*min_in_left)
        closest_pair = min_in_left
    else:
        total_min = distance(*min_in_right)
        closest_pair = min_in_right

    min_in_y = [point for point in y if distance(point, x_sep) < total_min]
    magic_index = 7 if len(min_in_y) > 7 else len(min_in_y)

    for current_index, _ in enumerate(min_in_y):
        for nex_index in range(magic_index):
            if current_index == nex_index:
                continue
            if distance(min_in_y[current_index], min_in_y[nex_index]) < total_min:
                total_min = distance(min_in_y[current_index], min_in_y[nex_index])
                closest_pair = min_in_y[current_index], min_in_y[nex_index]

    return closest_pair


if __name__ == '__main__':
    size = 15
    radius = 2

    plt.ion()

    points = [30 * np.random.random_sample(2) - 30 for i in range(size)]

    annotate_points(*points)

    vectors = [radius * np.random.random_sample(2) - radius for i in range(size)]
    while True:
        x_set = points.copy()
        x_set.sort(key=lambda point: point[0])
        y_set = points.copy()
        y_set.sort(key=lambda point: point[1])

        plt.clf()
        circles = [plt.Circle(point, radius, fill=False) for point in points]

        ax = plt.gca()
        ax.cla()

        points_x = [p[0] for p in points]
        points_y = [p[1] for p in points]
        ax.scatter(points_x, points_y, color='black')
        points_x = [p[0] for p in identify_closest_pair(x_set, y_set)]
        points_y = [p[1] for p in identify_closest_pair(x_set, y_set)]
        ax.scatter(points_x, points_y, color='red')

        ax.set_xlim((-150, 150))
        ax.set_ylim((-150, 150))

        for circle in circles:
            ax.add_artist(circle)

        plt.draw()
        plt.gcf().canvas.flush_events()
        time.sleep(0.1)

        for index1, _ in enumerate(points):
            for index2, _ in enumerate(points):
                if distance(points[index1], points[index2]) < 2 * radius:
                    vectors[index1] = -vectors[index1]
                    vectors[index2] = -vectors[index2]
                    points[index1] += vectors[index1]
                    points[index2] += vectors[index2]

        for index, _ in enumerate(points):
            points[index] = vectors[index] + points[index]
