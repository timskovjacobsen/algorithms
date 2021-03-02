

def polygon_area(xv, yv):
    '''Return the area of a non-self-intersecting polygon
    
    Parameters
    ----------
    xv : list
        The x-coordinates of the polygon vertices.
    yx : list
        The y-coordinate of the polygon vertices.
    signed

    Returns
    -------
    number
        The area of the polygon.
    '''

    # Perform shoelace multiplication
    a1 = [x * y for x, y in zip(xv, yv[1:])]
    a2 = [y * x for x, y in zip(xv[1:], yv)]

    # Return area of the polygon
    return 1/2 * abs(sum(a1) - sum(a2))
