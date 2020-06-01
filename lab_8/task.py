import matplotlib.pyplot as plt
import sys
import os

sys.path.append(os.path.join(sys.path[0], '../lab_1/'))
from lab_3.task_1 import draw_polygons, draw_polygon, slanting_product, scalar_product, intersection_of_lines, \
    location_of_the_point


def get_point_of_intersection(a, b, c, d):
    xdiff = (a[0] - b[0], c[0] - d[0])
    ydiff = (a[1] - b[1], c[1] - d[1])

    def det(i, j):
        return i[0] * j[1] - i[1] * j[0]

    div = det(xdiff, ydiff)
    d = (det(a, b), det(c, d))
    x = det(d, xdiff) / div
    y = det(d, ydiff) / div
    return x, y


def is_aimed(a_start, a_end, b_start, b_end):
    if slanting_product(b_start, b_end, b_start, a_end) > 0 and slanting_product(b_start, b_end, a_start, a_end) < 0:
        return True
    if slanting_product(b_start, b_end, b_start, a_end) < 0 and slanting_product(b_start, b_end, a_start, a_end) > 0:
        return True
    return scalar_product(a_end, a_start, a_end, b_end) < 0


def is_point_outer(a_start, a_end, b_end):
    return location_of_the_point(a_start, a_end, b_end) == 'right'


def get_lines(points_p, points_q):
    for i, point_q in enumerate(points_q):
            if is_point_outer(points_p[0], points_p[1], point_q) or \
                    is_point_outer(point_q, points_q[(i + 1) % len(points_q)], points_p[1]):
                return 0, i


def polygon_intersection(points_p, points_q):
    p_index, q_index = get_lines(points_p, points_q)
    res = []
    while True:
        pq = is_aimed(points_p[p_index], points_p[(p_index + 1) % len(points_p)], points_q[q_index],
                      points_q[(q_index + 1) % len(points_q)])
        qp = is_aimed(points_q[q_index], points_q[(q_index + 1) % len(points_q)], points_p[p_index],
                      points_p[(p_index + 1) % len(points_p)])
        # p на q & q на p
        if pq and qp:
            if is_point_outer(points_p[p_index], points_p[(p_index + 1) % len(points_p)],
                              points_q[(q_index + 1) % len(points_q)]):
                q_index += 1 if q_index + 1 < len(points_q) else -len(points_q) + 1
            else:
                p_index += 1 if p_index + 1 < len(points_p) else -len(points_p) + 1
        # p на q & q не на p
        elif pq and not qp:
            if not is_point_outer(points_q[q_index], points_q[(q_index + 1) % len(points_q)],
                                  points_p[(p_index + 1) % len(points_p)]):
                res.append(points_p[(p_index + 1) % len(points_p)])
            p_index += 1 if p_index + 1 < len(points_p) else -len(points_p) + 1
        # p не на q & q на p
        elif not pq and qp:
            if not is_point_outer(points_p[p_index], points_p[(p_index + 1) % len(points_p)],
                                  points_q[(q_index + 1) % len(points_q)]):
                res.append(points_q[(q_index + 1) % len(points_q)])
            q_index += 1 if q_index + 1 < len(points_q) else -len(points_q) + 1
        # p не на q & q не на p
        else:
            if intersection_of_lines(points_p[p_index], points_p[(p_index + 1) % len(points_p)],
                                     points_q[q_index], points_q[(q_index + 1) % len(points_q)]):
                res.append(get_point_of_intersection(points_p[p_index], points_p[(p_index + 1) % len(points_p)],
                                                     points_q[q_index], points_q[(q_index + 1) % len(points_q)]))
            if location_of_the_point(points_p[p_index], points_p[(p_index + 1) % len(points_p)],
                                     points_q[(q_index + 1) % len(points_q)]) == 'right':
                q_index += 1 if q_index + 1 < len(points_q) else -len(points_q) + 1
            else:
                p_index += 1 if p_index + 1 < len(points_p) else -len(points_p) + 1
        if len(res) > 1:
            if res[0] == res[-1]:
                res.pop()
                break
    return res


if __name__ == "__main__":
    points_p = [(9, 7), (-6, 5), (-10, 2), (-9, -5), (3, -10), (6, -10), (8, -5), (10, 6)]
    points_q = [(1, 10), (-7, 9), (-8, 4), (-7, -2), (-6, -5), (1, -2), (3, 6)]
    draw_polygons(points_p, points_q)
    draw_polygon(polygon_intersection(points_p, points_q))
    plt.show()
