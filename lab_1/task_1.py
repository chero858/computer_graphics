import matplotlib.pyplot as plt


def slanting_product(a, b, c, d):
    return (b[0] - a[0]) * (d[1] - c[1]) - (b[1] - a[1]) * (d[0] - c[0])


def draw_line_and_point(a, b, c):
    plt.plot([a[0], b[0]], [a[1], b[1]], color='blue')
    plt.plot(c[0], c[1], 'ro')
    plt.plot(b[0], b[1], 'x', color='blue')
    plt.show()


def determine_the_location_of_the_point(a, b, c):
    # c - the point for which we want to know the position
    det = slanting_product(a, b, a, c)
    if det < 0:
        return 'right'
    elif det > 0:
        return 'left'
    else:
        return 'on line'


if __name__ == '__main__':
    points = [[1, 2], [2, 3], [3, 4]]
    print(determine_the_location_of_the_point(*points))  # 3rd point for which we want to know the position
    draw_line_and_point(*points)
