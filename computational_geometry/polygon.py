from typing import List


def polygon_area(x: List, y: List, signed=False):
    """Return the area of a non-self-intersecting polygon.

    The vertices of the polygon must be given in the order. The lenght of `x` and `y` must be equal.
    The function automatically closes the polygon by connecting the first element (x0, y0) to the last (xn, yn).

    Parameters
    ----------
    x
        The x-coordinates of the polygon vertices.
    y
        The y-coordinate of the polygon vertices.
    signed
        Whether to return the signed area or not. If set to `True`, a polygon with vertices given in counter-clockwise order returns a postitve area, while a clockwise ordering returns a negative area. If set to `False` (default), the area is always positive.

    Returns
    -------
    number
        The area of the polygon.
    """
    # Copy coordinates of first point and append to list to create a closed polygon
    x = x + [x[0]]
    y = y + [y[0]]

    # Perform shoelace multiplication
    a1 = [xi * yi for xi, yi in zip(x, y[1:])]
    a2 = [yi * xi for xi, yi in zip(x[1:], y)]

    # Return area of the polygon
    if signed:
        return 1 / 2 * (sum(a1) - sum(a2))
    else:
        return 1 / 2 * abs(sum(a1) - sum(a2))
