from task_2 import intersection_of_lines
import matplotlib.pyplot as plt


def draw_polygon(*points):
    x = []
    y = []
    for point in points:
        x.append(point[0])
        y.append(point[1])
    x.append(points[0][0])
    y.append(points[0][1])
    plt.plot(x, y, marker='o')
    plt.show()


def is_polygon_simple(*points):
    points += (points[0],)
    for i, point in enumerate(points[:len(points) - 3]):
        for j in range(i + 2, len(points) - 1):
            if intersection_of_lines(points[i], points[i + 1], points[j], points[j + 1]) and points[i] != points[j + 1]:
                return False
    return True


if __name__ == '__main__':
    # points = [[-1, -1], [1, -1], [1, 1], [-1, 1]]
    # points = [[-1, -1], [1, -1], [-1, 1], [1, 1]]
    points = [[-2, -4], [2, -3], [3, 2], [0, 4], [-5, 2], [-3, 6], [1, 0]]
    # points = [[-2, -4], [2, -3], [3, 1], [1, 4], [-5, 2]    ]
    print(is_polygon_simple(*points))
    draw_polygon(*points)
