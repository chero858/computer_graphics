import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import random
from lab_5.lab5_jarvis import jarvis
from lab_5.lab5_diameter import diameter_search
from lab_1.task_1 import Point


def animate_points(i):
    carcass = jarvis(points)
    distance, d1, d2 = diameter_search(carcass)
    change_speed_flag = True if distance > 190 else False
    for point in points:
        if change_speed_flag:
            point.set_speed((-point.speed[0], -point.speed[1]))
        point.move()
    mat.set_data([point.x for point in points], [point.y for point in points])
    lines.set_data([i.x for i in carcass] + [carcass[0].x]
                   , [i.y for i in carcass] + [carcass[0].y])
    lines2.set_data([d1.x, d2.x], [d1.y, d2.y])
    return mat, lines, lines2,


if __name__ == "__main__":
    fig = plt.figure()
    ax = plt.axes(xlim=(-100, 100), ylim=(-100, 100))
    random.seed(205)
    points = [Point(random.randint(-50, 50), random.randint(-50, 50)) for i in range(0, 100)]
    for point in points:
        point.set_random_speed(0.1)
    mat, = ax.plot([point.x for point in points], [point.y for point in points], 'o', markersize=4)
    lines, = ax.plot([], [])
    lines2, = ax.plot([], [])
    anim = FuncAnimation(fig, animate_points, frames=100, interval=1,
                         blit=True)
    plt.show()
