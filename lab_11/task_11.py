import random
from math import atan, pi
import matplotlib.pyplot as plt
from lab_2.task_1 import is_point_belong_polygon
from lab_3.task_1 import draw_polygon, intersection_of_lines, location_of_the_point

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


def triangulation(points):
    triangles = [(points.pop(0), points.pop(0), points.pop(0)), ]
    first_vertex = 0
    second_vertex = 0
    for point in points:
        i = -1  # index of current triangle
        passed_i = [-1, ]
        while True:
            centre = triangle_centre(triangles[i])
            is_next_triangle_exist = False
            for j, vertex in enumerate(triangles[i]):
                if intersection_of_lines(centre, point, vertex, triangles[i][(j + 1) % 3]):
                    if next_triangle(vertex, triangles[i][(j + 1) % 3], triangles[i], triangles) is not None:
                        i = next_triangle(vertex, triangles[i][(j + 1) % 3], triangles[i], triangles)
                        is_next_triangle_exist = True if i not in passed_i else False
                        passed_i.append(i)
                    else:
                        first_vertex = vertex
                        second_vertex = triangles[i][(j + 1) % 3]
                    break
            if not is_next_triangle_exist:
                break
        if is_point_belong_polygon(point, triangles[i]):
            new_triangles = get_new_triangles(point, triangles.pop(i))
            for new_triangle in new_triangles:
                triangles.append(new_triangle)
                for j, vertex in enumerate(new_triangle):
                    i = next_triangle(vertex, new_triangle[(j + 1) % 3], new_triangle, triangles)
                    if i is not None and not check(new_triangle, triangles[i]):
                        triangles[-1], triangles[i] = rebuild(new_triangle, triangles[i])
        else:
            triangles.append((first_vertex, second_vertex, point))
            for j, vertex in enumerate(triangles[-1]):
                i = next_triangle(vertex, triangles[-1][(j + 1) % 3], triangles[-1], triangles)
                if i is not None and not check(triangles[-1], triangles[i]):
                    triangles[-1], triangles[i] = rebuild(triangles[-1], triangles[i])
    triangles = global_check(triangles)
    return triangles


def global_check(triangles):
    flag = True
    while flag:
        flag = False
        for j, triangle1 in enumerate(triangles):
            for k, triangle2 in enumerate(triangles):
                if not check(triangle1, triangle2):
                    triangles[j], triangles[k] = rebuild(triangle1, triangle2)
                    flag = True
    return triangles


def check(triangle1, triangle2):  # delaunay's check
    if len(list(set(triangle1) & set(triangle2))) != 2:  # adjacent triangles have two points in common
        return True
    for vertex in triangle2:
        if vertex not in triangle1:
            point = vertex
    return abs(((point[0] - triangle1[0][0]) * (point[1] - triangle1[2][1]) - (point[0] - triangle1[2][0]) * (
            point[1] - triangle1[0][1]))) * \
           ((triangle1[1][0] - triangle1[0][0]) * (triangle1[1][0] - triangle1[2][0]) + (
                   triangle1[1][1] - triangle1[0][1]) * (triangle1[1][1] - triangle1[2][1])) + \
           ((point[0] - triangle1[0][0]) * (point[0] - triangle1[2][0]) + (point[1] - triangle1[0][1]) * (
                   point[1] - triangle1[2][1])) * \
           abs(((triangle1[1][0] - triangle1[0][0]) * (triangle1[1][1] - triangle1[2][1]) - (
                   triangle1[1][0] - triangle1[2][0]) * (triangle1[1][1] - triangle1[0][1]))) >= 0


def get_new_triangles(point, triangle):
    triangles = []
    for i, vertex in enumerate(triangle):
        if location_of_the_point(vertex, triangle[(i + 1) % 3], point) == 'on line':
            continue
        triangles.append((vertex, triangle[(i + 1) % 3], point))
    return triangles


def next_triangle(start, end, curr_triangle, triangles):
    for triangle in triangles:
        if start in triangle and end in triangle and triangle != curr_triangle:
            return triangles.index(triangle)


def triangle_centre(triangle):
    return sum([point[0] for point in triangle]) / 3, sum([point[1] for point in triangle]) / 3


def rebuild(triangle1, triangle2):
    base = list(set(triangle1) ^ set(triangle2))
    for point in triangle1:
        if point not in base:
            base.append(point)
            triangle1 = tuple(base)
            base.pop()
    for point in triangle2:
        if point not in base and point not in triangle1:
            base.append(point)
            triangle2 = tuple(base)
            base.pop()
    return triangle1, triangle2


def convex_hull(points):
    points.sort(key=polar_angle)
    stack = [min_point, points[0]]
    while len(points) != 0:
        point = (points.pop(0))
        while location_of_the_point(stack[-2], stack[-1], point) == 'right':
            stack.pop()
        stack.append(point)
    return stack


if __name__ == '__main__':
    points = list(set([(random.randint(-50, 50), random.randint(-50, 50)) for i in range(30)]))
    points_copy = points.copy()
    min_point = find_min_point(points_copy)
    convex = convex_hull(points_copy)
    draw_polygon(convex)
    triangles = triangulation(points)
    for triangle in triangles:
        draw_polygon(triangle)
    plt.show()
