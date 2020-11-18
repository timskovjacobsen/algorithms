
from typing import Tuple


def move_point_towards_point(
    startpoint: Tuple[float],
    directionpoint: Tuple[float],
    relativedist: float = 1.0,
) -> Tuple[float]:
    '''Return the vector that offsets a point a distance towards another point.

    Parameters
    ----------
    startpoint
        Start point to offset, in the format (x, y).
    directionpoint
        Point that the offset will travel towards, in the format (x, y).
    relativedist, optional
        The relative distance for the offset as a fraction of the full distance
        between the points. Defaults to 1.0, meaning the offset is equal to
        the full distance.

    Returns
    -------
    The vector (x- and y-deltas) to offset the starting point. 
    '''
    x1, y1 = startpoint
    x2, y2 = directionpoint

    # Compute destinateion coordinates after desired move
    x_destination = (1 - relativedist) * x1 + relativedist * x2
    y_destination = (1 - relativedist) * y1 + relativedist * y2

    # Compute offsets in each direction required to move to destination point
    x_offset = x_destination - x1
    y_offset = y_destination - y1

    return x_offset, y_offset
