import matplotlib.pyplot as plt


def scalar_product(a, b, c, d):
    return (b[0] - a[0]) * (d[0] - c[0]) + (b[1] - a[1]) * (d[1] - c[1])


def slanting_product(a, b, c, d):
    return (b[0] - a[0]) * (d[1] - c[1]) - (b[1] - a[1]) * (d[0] - c[0])


def draw_polygons(convex_points, simple_points):
    x1 = []
    y1 = []
    x2 = []
    y2 = []
    for point in convex_points:
        x1.append(point[0])
        y1.append(point[1])
    x1.append(convex_points[0][0])
    y1.append(convex_points[0][1])
    for point in simple_points:
        x2.append(point[0])
        y2.append(point[1])
    x2.append(simple_points[0][0])
    y2.append(simple_points[0][1])
    plt.plot(x1, y1, x2, y2, marker='o')

def draw_polygon(points):
    x = []
    y = []
    for point in points:
        x.append(point[0])
        y.append(point[1])
    x.append(points[0][0])
    y.append(points[0][1])
    plt.plot(x, y, marker='o')
    # plt.show()


def octane(a, b):
    vector = (b[0] - a[0], b[1] - a[1])
    if 0 <= vector[1] < vector[0]:
        return 1
    elif 0 < vector[0] <= vector[1]:
        return 2
    elif 0 <= -vector[0] < vector[1]:
        return 3
    elif 0 < vector[1] <= -vector[0]:
        return 4
    elif 0 <= -vector[1] < -vector[0]:
        return 5
    elif 0 < -vector[0] <= -vector[1]:
        return 6
    elif 0 <= vector[0] < -vector[1]:
        return 7
    elif 0 < -vector[1] <= vector[0]:
        return 8
    else:
        return 1


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


def location_of_the_point(a, b, c):
    # c - the point for which we want to know the position
    det = slanting_product(a, b, a, c)
    if det < 0:
        return 'right'
    elif det > 0:
        return 'left'
    else:
        return 'on line'


def is_point_belong_convex_polygon(dot, points):
    start = 1
    sep = 0
    end = len(points) + 1
    location = location_of_the_point(points[0], points[1], points[2])
    if location_of_the_point(points[0], points[1], dot) != location or \
            location_of_the_point(points[-1], points[0], dot) != location:
        return False
    while end - start > 1:
        sep = round((start + end) / 2)
        if location_of_the_point(points[0], points[sep], dot) == location:
            start = sep
        else:
            end = sep
    return False if intersection_of_lines(points[0], dot, points[start], points[end]) else True


def is_point_belong_simple_polygon(dot, points):
    s = 0
    points.append(points[0])
    for i in range(len(points) - 1):
        if dot == points[i]:
            return True
        delta = octane(dot, points[i + 1]) - octane(dot, points[i])
        if delta > 4:
            delta -= 8
        elif delta < -4:
            delta += 8
        elif delta == 4 or delta == -4:
            det = slanting_product(dot, points[i], dot, points[i + 1])
            if det > 0:
                delta = 4
            elif det < 0:
                delta = -4
            else:
                return True
        s += delta
    return True if s == 8 or s == -8 else False


# def testing(simple_points):
#     for j in range(-1, 8):
#         for i in range(-3, 6):
#             if is_point_belong_simple_polygon([i, j], simple_points):
#                 plt.plot(i, j, 'ro', color='green')
#             else:
#                 plt.plot(i, j, 'ro', color='red')
#
#
# if __name__ == '__main__':
#     convex_points = [[-11, 0], [-8, 8], [-2, 10], [4, 9], [9, 6], [9, -1], [6, -3], [-1, -4]]
#     simple_points = [[-2, 0], [0, 2], [-2, 2], [0, 4], [-1, 6], [4, 6], [2, 3], [4, 3]]
#     # draw_polygons(convex_points, simple_points)
#     print(is_point_belong_convex_polygon([-9, -2], convex_points))
#     draw_polygon([-9, -2], convex_points)
#     # testing(simple_points)
#     plt.show()

