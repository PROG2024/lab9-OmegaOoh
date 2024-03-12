"""Unit tests of the Circle class using unittest or pytest (your choice).

Write unit tests as described in README.md.

1. Unit test for add_area using typical values.
2. Unit test for add_area for an "edge case" where one circle has radius 0.
3. Unit test that circle constructor raises exception of radius is negative.

"""
from circle import Circle
import math
import pytest


# TODO write 3 tests as described above
def test_add_area():
    """ Test for add_area method"""
    c1_rad = 2
    c1 = Circle(c1_rad)
    c2_rad = 1
    c2 = Circle(c2_rad)
    expected_rad = math.hypot(c1_rad,c2_rad)
    assert c1.add_area(c2).radius == expected_rad

def test_add_area_0():
    """ Test for add_area when radius is 0"""
    c1_rad = 2
    c1 = Circle(c1_rad)
    c2_rad = 0
    c2 = Circle(c2_rad)
    expected_rad = math.hypot(c1_rad, c2_rad)
    assert c1.add_area(c2).radius == expected_rad


def test_add_area_negative():
    """ Test for add_area when radius is negative"""
    with pytest.raises(ValueError):
        Circle(-1)
