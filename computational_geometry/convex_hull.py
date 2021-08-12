from typing import List, Tuple
from math import atan2

from computational_geometry.core import Point


def pop_anchor_point(points: List[Point]) -> Point:
    """Return the anchor point from a list of 2D points and remove it from
    the list.

    Parameters
    ----------
    points
        The list of points from which to extract the anchor point

    Returns
    -------
    The anchor point, i.e. the point with the smallest y-coordinate.
    If multiple points have the smallest y-coordinate, the point with
    the smallest x-coordinate among those is returned.

    Note
    ----
    This function mutates the input list.
    """
    anchor = points[0]
    anchor_index = 0

    # Loop over the array of points, excluding the first point
    for i, p in enumerate(points[1:], start=1):

        is_y_smaller = p.y < anchor.y
        is_y_equal_and_x_smaller = p.y == anchor.y and p.x < anchor.x

        if is_y_smaller or is_y_equal_and_x_smaller:
            # New anchor point found
            anchor = p
            anchor_index = i

    # Return the anchor point and remove it from the array
    return points.pop(anchor_index)


def convex_hull_graham_scan(points: List[Point]) -> List[Point]:
    """Return the convex hull using the Graham Scan algorithm."""

    # Create a copy of the input list to avoid mutating it
    xy_points = points[:]

    # Extract the anchor as the point with min y-coordinate, lowest x in case of a tie
    anchor = pop_anchor_point(xy_points)

    # Sort points acc. to their angle measured from the x-axis to the anchor point in
    # counter-clockwise direction. In case of ties, sort by distance from anchor point.
    xy_points.sort(key=lambda p: (p.angle(anchor), (p.distance_to(anchor))))

    # Initialize the list of hull points with the anchor and the first point in the
    # sorted points list. These are both guaranteed to be in the convex hull
    # This hull list works as a stack, where we add and pop points as needed. Thus,
    # a point that are added to the hull in an intermediate step might be removed if
    # as we gain more information during the algorithm's execution.
    hull = [anchor, xy_points[0]]

    for point in xy_points[1:]:

        # Backtrack to see if any points in the current hull need to be removed
        # while determinant(hull[-2], hull[-1], point) <= 0:
        # print("\nHULL =", hull, "\n")
        # print("\nHULL[-1] =", hull[-1], "\n")
        # print("\nHULL[-2] =", hull[-2], "\n")
        while point.determinant(hull[-2], hull[-1]) <= 0:
            # CASE 1:
            # THe determinant was negative, i.e. the point is on the right side of
            # the line segment formed by the last two point in the hull. Thus, the
            # current last point in the hull list cannot possibly be in the hull.

            # CASE 2:
            # The determinant was 0, i.e. the three points are colinear.
            # We  discard the middle point, i.e. the last point in the current hull
            hull.pop()

        # When we get here, the point must be on the left side of the line segment,
        # Thus, we add it to the convex hull.
        # Note that the point is not necessarily part of the final convex hull as it
        # might be removed in future backtracking steps.
        hull.append(point)

    return hull


if __name__ == "__main__":
    # import matplotlib.pyplot as plt

    points = [
        Point(2.5, 5.0),  # 1
        Point(1.4, 6.0),  # 2
        Point(4.0, 6.5),  # 3
        Point(3.5, 5.3),  # 4
        Point(4.2, 7.0),  # 5
        Point(6.0, 5.0),  # 6
        Point(6.2, 6.0),  # 7
        Point(6.5, 3.5),  # 8
        Point(2.5, 2.5),  # 9
        Point(0.5, 1.0),  # 10
        Point(1.5, 2.0),  # 11
        Point(2.0, 0.2),  # 12
        Point(5.0, 0.5),  # 13
        Point(5.0, 3.5),  # 14
        Point(4.0, 2.5),  # 15
    ]
    hull = convex_hull_graham_scan(points)
    print(hull)
