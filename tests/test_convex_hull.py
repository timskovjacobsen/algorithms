from numpy.testing import assert_array_almost_equal

from computational_geometry.convex_hull import convex_hull_graham_scan
from tests.testdata.data_convex_hull1 import points_1, hull_1


def test_convex_hull_graham_scan():
    # ----- Setup -----
    # Done by parametrization

    # ----- Execute -----
    actual = convex_hull_graham_scan(points_1)

    expected = hull_1

    # ----- Verify -----
    assert_array_almost_equal(actual, expected)
