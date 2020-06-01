from operator import attrgetter
from copy import deepcopy


def det(a, b, c, d):
    return a * d - b * c


def define_orientation(p1, p2, p0):
    D = det((p2.x - p1.x), (p2.y - p1.y), (p0.x - p1.x), (p0.y - p1.y))
    if D > 0:
        return "left"
    elif D < 0:
        return "right"
    else:
        return "on"


def find_max_right(core_point, points):
    max = points[0]
    if max == core_point:
        max = points[-1]
        for point in points[:-1]:
            if define_orientation(core_point, max, point) == "right" and point != core_point:
                max = point
    else:
        for point in points[1:]:
            if define_orientation(core_point, max, point) == "right" and point != core_point:
                max = point
    return max


def jarvis(original_points):
    points = deepcopy(original_points)
    points = [i for n, i in enumerate(points) if i not in points[:n]]
    core_point = min(points, key=attrgetter('y'))
    carcass = [core_point]
    while True:
        p1 = find_max_right(core_point, points)
        core_point = p1
        points.remove(core_point)
        if p1 == carcass[0]:
            break
        carcass.append(p1)
    return carcass
