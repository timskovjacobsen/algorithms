from __future__ import annotations
from math import atan2
from dataclasses import dataclass


@dataclass
class Point:
    # def __init__(self, x: float, y: float):
    #     self.x = x
    #     self.y = y
    x: float
    y: float

    def angle(self, other: Point):
        """Return the angle between a line a horizontal.

        The line is defined by the instance and another point."""
        dx = self.x - other.x
        dy = self.y - other.y
        return atan2(dy, dx)

    def distance_to(self, other: Point):
        """Return the Euclidian distance to from the point to another point."""
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
        # x0, y0 = self.x, self.y
        x1, y1 = other1.x, other1.y
        x2, y2 = other2.x, other2.y

        # Compute determinant
        # return (x1 - x0) * (y2 - y0) - (y1 - y0) * (x2 - x0)
        return (x2 - x1) * (self.y - y1) - (y2 - y1) * (self.x - x1)
