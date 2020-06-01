from math import factorial
import matplotlib.pyplot as plt
from lab_3.task_1 import draw_points


def bezier(points):
    ts = [t / 100.0 for t in range(101)]
    n = len(points)
    combinations = pascal_row(n - 1)
    result = []
    for t in ts:
        t_powers = (t ** i for i in range(n))
        u_powers = reversed([(1 - t) ** i for i in range(n)])
        coefs = [c * a * b for c, a, b in zip(combinations, t_powers, u_powers)]
        result.append(
            tuple(sum([coef * p for coef, p in zip(coefs, ps)]) for ps in zip(*points)))
    return result


def combination(n, r):
    return int((factorial(n)) / ((factorial(r)) * factorial(n - r)))


def pascal_row(count):
    result = []
    for element in range(count + 1):
        result.append(combination(count, element))
    return result


if __name__ == '__main__':
    points = [(20, 0), (0, 50), (60, 50), (100, 0), (140, 38)]
    draw_points(points, 'blue', 'o')
    bezier_points = bezier(points)

    draw_points(bezier_points, 'green', None)
    plt.show()
