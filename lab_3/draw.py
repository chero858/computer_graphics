import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import random
from math import cos, sin
from lab_3.task_1 import is_point_belong_simple_polygon, is_point_belong_convex_polygon, draw_polygons


def animate_points(i):
    for point in points:
        x_bool = bool(random.getrandbits(1))
        y_bool = bool(random.getrandbits(1))
        # point[0] += cos(angle) * cos(angle) if x_bool else -cos(angle) * cos(angle)
        # point[1] += sin(angle) * sin(angle) if y_bool else -sin(angle) * sin(angle)
        point[0] += 0.7 if x_bool else -0.7
        point[1] += 0.7 if y_bool else -0.7
        if is_point_belong_simple_polygon(point, simple_points):
            points.remove(point)
        if not is_point_belong_convex_polygon(point, convex_points):
            point[0] -= 1.4 if x_bool else -1.4
            point[1] -= 1.4 if y_bool else -1.4
    mat.set_data([point[0] for point in points], [point[1] for point in points])
    return mat,


if __name__ == "__main__":
    convex_points = [[-11, 0], [-8, 8], [-2, 10], [4, 9], [9, 6], [9, -1], [6, -3], [-1, -4]]
    simple_points = [[-2, 0], [0, 2], [-2, 2], [0, 4], [-1, 6], [4, 6], [2, 3], [4, 3]]
    fig = plt.figure()
    ax = plt.axes(xlim=(-14, 12), ylim=(-7, 14))
    points = []
    while len(points) != 10:
        point = [random.randint(-10, 8), random.randint(-3, 9)]
        if not is_point_belong_simple_polygon(point, simple_points) and is_point_belong_convex_polygon(point, convex_points):
            points.append(point)
    mat, = ax.plot([point[0] for point in points], [point[1] for point in points], 'o', markersize=4)
    angle = -2.5
    ani = FuncAnimation(fig, animate_points, frames=150, interval=20, blit=True)
    draw_polygons(convex_points, simple_points)
    plt.show()
