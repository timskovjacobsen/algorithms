from numpy.testing import assert_almost_equal

from computational_geometry.polygon import polygon_area


def test_polygon_with_counterclockwise_rectangle():

    # ----- Setup -----
    # Define the vertices of a rectangle (B x H = 10 x 10)
    x = [0, 10, 10, 0]
    y = [0, 0, 10, 10]

    # ----- Exercise -----
    # Compute the area of the hexagon
    actual = polygon_area(x, y)
    actual_signed = polygon_area(x, y, signed=True)

    # The CORRECT result for the area is 100.00 and 100.00
    expected = 100.00
    expected_signed = 100.00

    # ----- Verify -----
    assert_almost_equal(actual, expected, decimal=2)
    assert_almost_equal(actual_signed, expected_signed, decimal=2)


def test_polygon_with_clockwise_rectangle():

    # ----- Setup -----
    # Define the vertices of a rectangle (B x H = 10 x 10)
    x = [0, 0, 10, 10]
    y = [0, 10, 10, 0]

    # ----- Exercise -----
    # Compute the area of the hexagon
    actual = polygon_area(x, y)
    actual_signed = polygon_area(x, y, signed=True)

    # The CORRECT result for the area is 100.00 and -100.00
    expected = 100.00
    expected_signed = -100.00

    # ----- Verify -----
    assert_almost_equal(actual, expected, decimal=2)
    assert_almost_equal(actual_signed, expected_signed, decimal=2)


def test_polygon_with_counterclockwise_hexagon():

    # ----- Setup -----
    # Define the vertices of a hexagon
    x = [3, 4, 7, 8, 8.5, 3]
    y = [5, 3, 0, 1, 3, 5]

    # ----- Exercise -----
    # Compute the area of the hexagon
    actual = polygon_area(x, y)
    actual_signed = polygon_area(x, y, signed=True)

    # The CORRECT result for the area is 12.0 and 12.0
    expected = 12.0
    expected_signed = 12.0

    # ----- Verify -----
    assert_almost_equal(actual, expected, decimal=2)
    assert_almost_equal(actual_signed, expected_signed, decimal=2)
