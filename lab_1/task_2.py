from task_1 import slanting_product
import matplotlib.pyplot as plt


def scalar_product(a, b, c, d):
    return (b[0] - a[0]) * (d[0] - c[0]) + (b[1] - a[1]) * (d[1] - c[1])


def intersection_of_lines(a, b, c, d):
    det1 = slanting_product(c, d, c, a)
    det2 = slanting_product(c, d, c, b)
    det3 = slanting_product(a, b, a, c)
    det4 = slanting_product(a, b, a, d)
    if det1 == det2 == det3 == det4 == 0:
        return (scalar_product(a, c, a, d) < 0) or (scalar_product(b, c, b, d) < 0) or \
                (scalar_product(c, a, c, b) < 0) or (scalar_product(d, a, d, b) < 0)
    return (det1 * det2 <= 0) and (det3 * det4 <= 0)


if __name__ == '__main__':
    a, b, c, d = [-1, -1], [1, -1], [1, -1], [1, 1]
    # a, b, c, d = [1, 0], [5, 0], [7, 0], [11, 0]
    print(intersection_of_lines(a, b, c, d))
    plt.plot([a[0], b[0]], [a[1], b[1]], [c[0], d[0]], [c[1], d[1]], marker='o')
    plt.show()
