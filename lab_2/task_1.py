import matplotlib.pyplot as plt
import sys
import os

sys.path.append(os.path.join(sys.path[0], '../lab_1/'))
from lab_1.task_1 import slanting_product


def scalar_product(a, b, c, d):
    return (b[0] - a[0]) * (d[0] - c[0]) + (b[1] - a[1]) * (d[1] - c[1])


# def slanting_product(a, b, c, d):
#     return (b[0] - a[0]) * (d[1] - c[1]) - (b[1] - a[1]) * (d[0] - c[0])


def draw_polygon(dot, *points):
    x = []
    y = []
    for point in points:
        x.append(point[0])
        y.append(point[1])
    x.append(points[0][0])
    y.append(points[0][1])
    plt.plot(x, y, marker='o')
    plt.plot(dot[0], dot[1], 'ro')
    plt.show()


def intersection_of_lines(a, b, c, d):
    det1 = slanting_product(c, d, c, a)
    det2 = slanting_product(c, d, c, b)
    det3 = slanting_product(a, b, a, c)
    det4 = slanting_product(a, b, a, d)
    if det1 == det2 == det3 == det4 == 0:
        if (scalar_product(a, c, a, d) < 0) or (scalar_product(b, c, b, d) < 0) or \
                (scalar_product(c, a, c, b) < 0) or (scalar_product(d, a, d, b) < 0):
            return True
        else:
            return False
    elif (det1 * det2 <= 0) and (det3 * det4 <= 0):
        return True
    else:
        return False


def dimensional_test(*points):
    min = [points[0][0], points[0][1]]
    max = [points[0][0], points[0][1]]
    for point in points:
        if point[0] > max[0]:
            max[0] = point[0]
        if point[1] > max[1]:
            max[1] = point[1]
        if point[0] < min[0]:
            min[0] = point[0]
        if point[1] < min[1]:
            min[1] = point[1]
    return min, max


def is_point_belong_line(a, b, c):
    # c - the point for which we want to know the position
    det = slanting_product(a, b, a, c)
    return True if det == 0 else False


def location_of_the_point(a, b, c):
    # c - the point for which we want to know the position
    det = slanting_product(a, b, a, c)
    if det < 0:
        return 'right'
    elif det > 0:
        return 'left'
    else:
        return 'on line'


def is_point_belong_polygon(dot, points):
    min, max = dimensional_test(*points)
    points += (points[0],)
    if dot[0] > max[0] or dot[0] < min[0] or dot[1] > max[1] or dot[1] < min[1]:
        return False
    q = [min[0] - 1, dot[1]]
    s = 0
    for i, point in enumerate(points[:len(points) - 1]):
        if intersection_of_lines(points[i], points[i + 1], q, dot):
            if not is_point_belong_line(q, dot, points[i]) and not is_point_belong_line(q, dot, points[i + 1]):
                s += 1
            elif is_point_belong_line(q, dot, points[i]):
                k = 0
                while is_point_belong_line(q, dot, points[i + k]):
                    k += 1
                if location_of_the_point(q, dot, points[i - 1]) != location_of_the_point(q, dot, points[i + k]):
                    s += 1
    return True if s % 2 else False


def main():
    dot = [-1, 0]
    points = [[-2, -4], [2, -3], [3, 2], [0, 4], [-5, 2], [-3, 0], [1, 0]]
    print(is_point_belong_polygon(dot, points))
    draw_polygon(dot, *points)


if __name__ == '__main__':
    main()
