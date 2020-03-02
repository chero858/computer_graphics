import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from math import pi, atan
import random
import sys
import os

sys.path.append(os.path.join(sys.path[0], '../lab_1/'))
from lab_3.task_1 import location_of_the_point

min_point = []


def find_min_point(points):
    min = points[0]
    for point in points:
        if point[1] < min[1]:
            min = point
    return min


def polar_angle(point):
    if point[0] == min_point[0]:
        return pi / 2
    angle = atan((point[1] - min_point[1]) / (point[0] - min_point[0]))
    return angle if point[0] > min_point[0] else angle + pi


def draw(points):
    plt.plot(min_point[0], min_point[1], 'o', markersize=4, color='blue')
    for i, point in enumerate(points):
        plt.plot(point[0], point[1], 'o', markersize=4, color='blue')


def animate_points(i):
    x_vals = [point[0] for point in stack]
    y_vals = [point[1] for point in stack]
    if len(points) == 0:
        x_vals.append(min_point[0])
        y_vals.append(min_point[1])
        ani.event_source.stop()
        mat.set_data(x_vals, y_vals)
        return mat,
    point = (points.pop(0))
    while location_of_the_point(stack[-2], stack[-1], point) == 'right':
        stack.pop()
    stack.append(point)
    mat.set_data(x_vals, y_vals)
    return mat,


if __name__ == "__main__":
    points = list(set([(random.randint(-10, 10), random.randint(-10, 10)) for i in range(20)]))
    min_point = find_min_point(points)
    points.sort(key=polar_angle)
    stack = [min_point, points[0]]
    fig = plt.figure()
    ax = plt.axes(xlim=(-11, 11), ylim=(-11, 11))
    mat, = ax.plot([], [])
    ani = FuncAnimation(fig, animate_points, frames=150, interval=250, blit=True)
    draw(points)
    plt.show()
