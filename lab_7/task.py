from math import sqrt
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import sys
import os
import time

sys.path.append(os.path.join(sys.path[0], '../lab_1/'))
from lab_3.task_1 import location_of_the_point


def vector_len(a, b):
    return sqrt(((b[0] - a[0]) ** 2) + ((b[1] - a[1]) ** 2))


def draw_polygon(points, point_s):
    x = []
    y = []
    for point in points:
        x.append(point[0])
        y.append(point[1])
    x.append(points[0][0])
    y.append(points[0][1])
    plt.plot(x, y, marker='o')
    plt.plot(point_s[0], point_s[1], 'o', markersize=5, color='blue')


def add_point(convex_points, point_s):
    if len(convex_points) == 0 or len(convex_points) == 1:
        convex_points.append(point_s)
        return convex_points
    elif len(convex_points) == 2:
        if location_of_the_point(convex_points[0], convex_points[1], point_s) == 'on line':
            if vector_len(convex_points[0], convex_points[1]) > vector_len(convex_points[0], point_s) and \
                    vector_len(convex_points[0], convex_points[1]) > vector_len(convex_points[1], point_s):
                return convex_points
            elif vector_len(convex_points[0], point_s) > vector_len(convex_points[0], convex_points[1]) and \
                    vector_len(convex_points[0], point_s) > vector_len(convex_points[1], point_s):
                return [convex_points[0], point_s]
            elif vector_len(convex_points[1], point_s) > vector_len(convex_points[0], convex_points[1]) and \
                    vector_len(convex_points[1], point_s) > vector_len(convex_points[0], point_s):
                return [convex_points[1], point_s]
        elif location_of_the_point(convex_points[0], convex_points[1], point_s) == 'left':
            return [convex_points[0], convex_points[1], point_s]
        else:
            return [convex_points[0], point_s, convex_points[1]]
    left = []
    point_s_index = None
    for j in range(len(convex_points)):
        if location_of_the_point(convex_points[j], convex_points[(j + 1) % len(convex_points)], point_s) == "left":
            if convex_points[j] not in left:
                left.append(convex_points[j])
            if convex_points[(j + 1) % len(convex_points)] not in left:
                left.append(convex_points[(j + 1) % len(convex_points)])
        elif point_s_index is None:
            point_s_index = len(left)
    if len(left) == 0:
        return convex_points
    convex_points = []
    for j, point in enumerate(left):
        if j == point_s_index:
            convex_points.append(point_s)
        convex_points.append(point)
    return convex_points


def animate_points(i):
    # time.sleep(4)
    if i == 1:
        ani.event_source.stop()
        return mat,
    points = add_point(convex_points, point_s)
    points.append(points[0])
    x_vals = [point[0] for point in points]
    y_vals = [point[1] for point in points]
    mat.set_data(x_vals, y_vals)
    i += 1
    return mat,


if __name__ == "__main__":
    convex_points = [(9, 7), (-5, 9), (-6, 9), (-10, 6), (-9, -5), (0, -9), (3, -10), (6, -10), (8, -5), (10, 6)]
    point_s = (12, 12)
    fig = plt.figure()
    ax = plt.axes(xlim=(-13, 13), ylim=(-13, 13))
    mat, = ax.plot([], [])
    ani = FuncAnimation(fig, animate_points, frames=150, interval=250, blit=True)
    draw_polygon(convex_points, point_s)
    plt.show()
    print(convex_points)
