from typing import List, Tuple
from math import atan2


def angle(point0: Tuple[float, float], point1: Tuple[float, float]) -> float:
    """Return the angle between a line in 2D and the horizontal axis."""
    dx = point1[0] - point0[0]
    dy = point1[1] - point0[1]
    return atan2(dy, dx)


def distance(point0, point1):
    """Return the Euclidian distance between two points."""
    dx = point1[0] - point0[0]
    dy = point1[1] - point0[1]
    return (dx ** 2 + dy ** 2) ** 0.5


def determinant(
    point0: Tuple[float, float],
    point1: Tuple[float, float],
    point2: Tuple[float, float],
) -> float:
    """Return the determinant of the triangle defined by three points.

    If the determinant is:

        positive:
            Getting to point 2 means a counter-clockwise turn from the line segment
            point 0 -> point 1, i.e. point 2 is on the left side of the segment.
        negative:
            Getting to point 2 means a clockwise turn from the line segment
            point 0 -> point 1, i.e. point 2 is on the right side of the segment.
        zero:
            All three points are colinear, i.e. on a straight line.
    """
    x0, y0 = point0[0], point0[1]
    x1, y1 = point1[0], point1[1]
    x2, y2 = point2[0], point2[1]

    # Compute determinant
    return (x1 - x0) * (y2 - y0) - (y1 - y0) * (x2 - x0)


def pop_anchor_point(points: List[Tuple[float, float]]) -> Tuple[float, float]:
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
    for i, (x, y) in enumerate(points[1:], start=1):

        is_y_smaller = y < anchor[1]
        is_y_equal_and_x_smaller = y == anchor[1] and x < anchor[0]

        if is_y_smaller or is_y_equal_and_x_smaller:
            # New anchor point found
            anchor = (x, y)
            anchor_index = i

    # Return the anchor point and remove it from the array
    return points.pop(anchor_index)


def convex_hull_graham_scan(
    points: List[Tuple[float, float]]
) -> List[Tuple[float, float]]:
    """Return the convex hull using the Graham Scan algorithm."""

    # Create a copy of the input list to avoid mutating it
    xy_points = points[:]

    # Extract the anchor as the point with min y-coordinate, lowest x in case of a tie
    anchor = pop_anchor_point(xy_points)

    # Sort points acc. to their angle measured from the x-axis to the anchor point in
    # counter-clockwise direction. In case of ties, sort by distance from anchor point.
    xy_points.sort(key=lambda p: (angle(anchor, p), distance(anchor, p)))

    # Initialize the list of hull points with the anchor and the first point in the
    # sorted points list. These are both guaranteed to be in the convex hull
    # This hull list works as a stack, where we add and pop points as needed. Thus,
    # a point that are added to the hull in an intermediate step might be removed if
    # as we gain more information during the algorithm's execution.
    hull = [anchor, xy_points[0]]

    for point in xy_points[1:]:

        # Backtrack to see if any points in the current hull need to be removed
        while determinant(hull[-2], hull[-1], point) <= 0:
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
