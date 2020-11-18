from typing import List, Tuple
import operator

from math import atan2


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
