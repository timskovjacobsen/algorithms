from typing import List, Tuple
import operator

from math import atan2


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def angle(self, other):
        dx = self.x - other.x
        dy = self.x - other.y
        return atan2(dy, dx)

    def distance(self, other):
        """Return the Euclidian distance between two points."""
        dx = self.x - other.x
        dy = self.x - other.y
        return (dx ** 2 + dy ** 2) ** 0.5

    def determinant(self, other1, other2):
        """Return the determinant of the triangle defined by three points.

        If the determinant is:

            Positive: Counter-clockwise turn
            Negative: Clock-wise turn
            zero: All three points are on a straight line
        """
        x0, y0 = self.x, self.y
        x1, y1 = other1.x, other1.y
        x2, y2 = other2.x, other2.y

        # Compute determinant
        return (x1 - x0) * (y2 - y0) - (y1 - y0) * (x2 - x0)


def angle(point0, point1):
    """Return the angle between two points."""

    dx = point1[0] - point0[0]
    dy = point1[1] - point0[1]
    return atan2(dy, dx)


def distance(point0, point1):
    """Return the Euclidian distance between two points."""
    dx = point1[0] - point0[0]
    dy = point1[1] - point0[1]
    return (dx ** 2 + dy ** 2) ** 0.5


def determinant(point0, point1, point2):
    """Return the determinant of the triangle defined by three points.

    If the determinant is:

        Positive: Counter-clockwise turn
        Negative: Clock-wise turn
        zero: All three points are on a straight line
    """
    x0, y0 = point0[0], point0[1]
    x1, y1 = point1[0], point1[1]
    x2, y2 = point2[0], point2[1]

    # Compute determinant
    return (x1 - x0) * (y2 - y0) - (y1 - y0) * (x2 - x0)


def convex_hull_graham_scan(
    points: List[Tuple[float, float]]
) -> List[Tuple[float, float]]:
    """Return the convex hull using the Graham Scan algorithm."""

    # Set anchor to point with lowest y-coordinate and lowest x in case of a tie
    points.sort(key=operator.itemgetter(1))
    anchor = points.pop(0)

    # Sort points by acc. to their angle with the anchor point
    # Secondary sort by distance from anchor point in case of ties
    points.sort(key=lambda p: (angle(anchor, p), distance(anchor, p)))

    hull = [anchor, points[0]]
    for point in points[1:]:
        while determinant(hull[-2], hull[-1], point) <= 0:
            del hull[-1]
        hull.append(point)

    return hull


def is_convex(*points):
    """Return 'True' if polygon is convex, otherwise 'False'"""
    pass


if __name__ == "__main__":

    import numpy as np

    points = list(np.random.random((100, 2)))

    for x, y in points:
        print(f"({x:.4F}, {y:.4F})")

    # for point in points:
    #     print(point)

    # points = [
    #     (3, 3.0),
    #     (6, 3.5),
    #     (5, 7.7),
    #     (8, 5),  #
    #     (4.9, 7.7),
    #     (6, 3.9),
    #     (4.8, 7.9),
    #     (-2, 2),  #
    #     (3, 7),
    #     (5, -10),  # Anchor
    #     (4, 15),  #
    # ]

    hull = convex_hull(points)
    print("\n\n")
    for x, y in hull:
        print(f"({x:.4F}, {y:.4F})")

    # Class definition
    # points = [Point(x, y) for x, y in points]
    # p = Point(12, 42)
    # print(p[0])

    import matplotlib.pyplot as plt

    xp, yp = zip(*points)
    xh, yh = zip(*hull)
    plt.plot(xp, yp, "r.")
    plt.plot(xh, yh, "g-")
    plt.show()

    # hull = convex_hull(points)
