import pytest
from numpy.testing import assert_array_almost_equal

from computational_geometry.points import move_point_towards_point


@pytest.mark.parametrize(
    "point1, point2, relative_dist, expected",
    [
        ((0, 0), (1, 0), 0.49, (0.49, 0.00)),
        ((0, 0), (0, 1), 0.49, (0.00, 0.49)),
        ((4, 9), (5, 10), 2.00, (2.00, 2.00)),
        ((1, 1), (-5, -5), 1.00, (-6.00, -6.00)),
    ],
)
def test_move_point_towards_point_along_x_axis(point1, point2, relative_dist, expected):
    # ----- Setup -----
    # Done by parametrization

    # ----- Execute -----
    actual = move_point_towards_point(point1, point2, relative_dist)

    # ----- Verify -----
    assert_array_almost_equal(actual, expected)
