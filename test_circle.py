"""Unit tests of the Circle class using unittest or pytest (your choice).

Write unit tests as described in README.md.

1. Unit test for add_area using typical values.
2. Unit test for add_area for an "edge case" where one circle has radius 0.
3. Unit test that circle constructor raises exception of radius is negative.

"""
from circle import Circle
import math
import pytest


def test_add_area():
    """ Test for add_area method"""
    c1 = Circle(3)
    c2 = Circle(4)
    c_result = c1.add_area(c2)
    assert c_result.radius == 5
    assert c_result.get_area() == math.pi * 25


def test_add_area_0():
    """ Test for add_area when radius is 0"""
    c1 = Circle(3)
    c2 = Circle(0)
    c_result = c1.add_area(c2)
    assert c_result.radius == 3
    assert c_result.get_area() == math.pi * 9


def test_negative_rad():
    """ Test for add_area when radius is negative"""
    with pytest.raises(ValueError):
        Circle(-1)
