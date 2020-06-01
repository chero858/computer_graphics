from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation
from lab_3.task_1 import draw_points

bezier_points = []
bezier_line = []


def get_point(p1, p2, t):
    return p1[0] + (p2[0] - p1[0]) * t, p1[1] + (p2[1] - p1[1]) * t


def bezier(points, t):
    medium_points = []
    for i in range(len(points) - 1):
        medium_points.append(get_point(points[i], points[i + 1], t))
    if len(medium_points) > 1:
        bezier_points.append(medium_points)
        bezier(medium_points, t)
    else:
        bezier_line.append(medium_points[0])
        return


def animate_points(i):
    t = i / 100
    if t == 1.01:
        ani.event_source.stop()
        return lines
    global bezier_points
    bezier_points = []
    bezier(points, t)
    for line, bezier_point in zip(lines[:-1], bezier_points):
        line.set_data([point[0] for point in bezier_point], [point[1] for point in bezier_point])
    lines[-1].set_data([point[0] for point in bezier_line], [point[1] for point in bezier_line])
    return lines


if __name__ == "__main__":
    points = [(20, 0), (0, 50), (60, 50), (100, 0), (140, 38), (120, 50)]
    fig = plt.figure()
    ax = plt.axes(xlim=(-10, 150), ylim=(-10, 60))
    lines = []
    for index in range(len(points) - 1):
        lines.append(ax.plot([], [], lw=2)[0])
    ani = FuncAnimation(fig, animate_points, frames=150, interval=50, blit=True)
    draw_points(points, '#858080', 'o')
    plt.show()
