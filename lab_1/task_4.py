from task_1 import determine_the_location_of_the_point
from task_3 import draw_polygon, is_polygon_simple


def is_polygon_convex(*points):
    if not is_polygon_simple(points):
        return False
    points += (points[0], points[1])
    location = determine_the_location_of_the_point(points[0], points[1], points[2])
    for i, point in enumerate(points[:len(points) - 2]):
        if location != determine_the_location_of_the_point(points[i], points[i + 1], points[i + 2]):
            return False
    return True


if __name__ == '__main__':
    points = [[-1, -1], [1, -1], [1, 1], [-1, 1], [0, 0]]
    print(is_polygon_convex(*points))
    draw_polygon(*points)
