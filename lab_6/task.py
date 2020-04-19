import matplotlib.pyplot as plt
import random
import sys
import os

sys.path.append(os.path.join(sys.path[0], '../lab_1/'))
from lab_3.task_1 import location_of_the_point, slanting_product

convex_hull = []


def draw_points(points):
    for point in points:
        plt.plot(point[0], point[1], 'o', markersize=4, color='blue')


def draw_polygon(points):
    x = []
    y = []
    for point in points:
        x.append(point[0])
        y.append(point[1])
    x.append(points[0][0])
    y.append(points[0][1])
    plt.plot(x, y, marker='o')


def triangle_area(a, b, c):
    return 0.5 * abs(slanting_product(a, b, a, c))


def find_min_max_points(points):
    min_point = points[0]
    max_point = points[0]
    for point in points:
        if point[0] < min_point[0]:
            min_point = point
        elif point[0] > max_point[0]:
            max_point = point
    return min_point, max_point


def separate_points(points, min_point, max_point):
    left_points = []
    right_points = []
    for point in points:
        if location_of_the_point(min_point, max_point, point) == 'left':
            left_points.append(point)
        elif location_of_the_point(min_point, max_point, point) == 'right':
            right_points.append(point)
    return left_points, right_points


def find_hull(points, min_point, max_point):
    if len(points) == 0:
        return
    farthest_point = points[0]
    for point in points:
        if triangle_area(max_point, min_point, point) > triangle_area(max_point, min_point, farthest_point):
            farthest_point = point
    index = convex_hull.index(max_point)  # need to insert farthest_point between max and min points(they locate near
    # each other)
    convex_hull.insert(index, farthest_point)
    left_points = []
    right_points = []
    for point in points:
        if location_of_the_point(farthest_point, min_point, point) == 'left':
            left_points.append(point)
        elif location_of_the_point(farthest_point, max_point, point) == 'right':
            right_points.append(point)
    find_hull(left_points, min_point, farthest_point)
    find_hull(right_points, farthest_point, max_point)


def quick_hull(points):
    min_point, max_point = find_min_max_points(points)
    convex_hull.append(min_point)
    convex_hull.append(max_point)
    left_points, right_points = separate_points(points, min_point, max_point)
    find_hull(right_points, min_point, max_point)
    find_hull(left_points, max_point, min_point)


if __name__ == '__main__':
    random.seed(14)
    points = list(set([(random.randint(-10, 10), random.randint(-10, 10)) for i in range(13)]))
    draw_points(points)
    quick_hull(points)
    draw_polygon(convex_hull)
    plt.show()
    print(convex_hull)
