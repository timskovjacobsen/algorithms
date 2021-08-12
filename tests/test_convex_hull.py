from numpy.testing import assert_array_almost_equal

from computational_geometry.convex_hull import convex_hull_graham_scan
from tests.testdata.data_convex_hull1 import points_1, hull_1


def test_convex_hull_graham_scan():
    # ----- Setup -----
    # Done by parametrization

    # ----- Execute -----
    hull = convex_hull_graham_scan(points_1)

    actual_x = [p.x for p in hull]
    actual_y = [p.y for p in hull]

    expected_x = [p.x for p in hull_1]
    expected_y = [p.y for p in hull_1]

    # ----- Verify -----
    assert_array_almost_equal(actual_x, expected_x)
    assert_array_almost_equal(actual_y, expected_y)
