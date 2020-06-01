from lab_5.lab5_jarvis import jarvis
from lab_5.lab5_jarvis import det
from math import sqrt


def S(p1, p2, p3):
    return abs(
        det(p1.x - p3.x, p1.y - p3.y, p2.x - p3.x, p2.y - p3.y) / 2)


def distance(p1, p2):
    return sqrt((p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2)


class Next():
    def __init__(self, list):
        self.list = list

    def next(self, p):
        return self.list[(self.list.index(p) + 1) % len(self.list)]


def diameter_search(points):
    carcass = jarvis(points)
    P = Next(carcass)
    n = len(carcass)
    p = carcass[-1]
    q = P.next(p)
    while S(p, P.next(p), P.next(q)) > S(p, P.next(p), q):
        q = P.next(q)
    q0 = q
    d_max = 0, p, q
    counter = 0
    while q != carcass[0] and counter < n:
        p = P.next(p)
        d_max = (distance(p, q), p, q) if distance(p, q) >= d_max[0] else d_max
        while S(p, P.next(p), P.next(q)) > S(p, P.next(p), q):
            counter += 1
            q = P.next(q)
            if distance(p, q) != distance(q0, carcass[0]):
                d_max = (distance(p, q), p, q) if distance(p, q) >= d_max[0] else d_max
        # if S(p, P.next(p), P.next(q)) == S(p, P.next(p), q):
        #     if distance(p, q) != (q0, carcass[-1]):
        #         d_max = (distance(p, P.next(q)), p, P.next(q)) if distance(p, P.next(q)) >= d_max[0] else d_max
    return d_max


