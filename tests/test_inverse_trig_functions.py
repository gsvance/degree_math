"""Unit tests for the inverse (arc) trig functions in degree_math."""

import math
from typing import Final
import unittest

from degree_math import asin, acos, atan, atan2


SQRT_2: Final[float] = math.sqrt(2)
SQRT_3: Final[float] = math.sqrt(3)

INF: Final[float] = float('inf')


class TestInverseTrigFunctions(unittest.TestCase):

    # Inverse sine function

    def test_arcsine(self):

        # Negative inputs
        self.assertAlmostEqual(asin(-1), -90)
        self.assertAlmostEqual(asin(-SQRT_3/2), -60)
        self.assertAlmostEqual(asin(-SQRT_2/2), -45)
        self.assertAlmostEqual(asin(-1/2), -30)
        self.assertAlmostEqual(asin(-0.0), 0)

        # Positive inputs
        self.assertAlmostEqual(asin(0), 0)
        self.assertAlmostEqual(asin(1/2), 30)
        self.assertAlmostEqual(asin(SQRT_2/2), 45)
        self.assertAlmostEqual(asin(SQRT_3/2), 60)
        self.assertAlmostEqual(asin(1), 90)

    # Inverse cosine function

    def test_arccosine(self):

        # Negative inputs
        self.assertAlmostEqual(acos(-1), 180)
        self.assertAlmostEqual(acos(-SQRT_3/2), 150)
        self.assertAlmostEqual(acos(-SQRT_2/2), 135)
        self.assertAlmostEqual(acos(-1/2), 120)
        self.assertAlmostEqual(acos(-0.0), 90)

        # Positive inputs
        self.assertAlmostEqual(acos(0), 90)
        self.assertAlmostEqual(acos(1/2), 60)
        self.assertAlmostEqual(acos(SQRT_2/2), 45)
        self.assertAlmostEqual(acos(SQRT_3/2), 30)
        self.assertAlmostEqual(acos(1), 0)

    # Inverse tangent functions

    def test_arctangent(self):

        # Negative inputs
        self.assertAlmostEqual(atan(-INF), -90)
        self.assertAlmostEqual(atan(-SQRT_3), -60)
        self.assertAlmostEqual(atan(-1), -45)
        self.assertAlmostEqual(atan(-SQRT_3/3), -30)
        self.assertAlmostEqual(atan(-0.0), 0)

        # Positive inputs
        self.assertAlmostEqual(atan(0), 0)
        self.assertAlmostEqual(atan(SQRT_3/3), 30)
        self.assertAlmostEqual(atan(1), 45)
        self.assertAlmostEqual(atan(SQRT_3), 60)
        self.assertAlmostEqual(atan(INF), 90)

    def test_arctangent2_on_x_and_y_axes(self):

        # Positive zeros
        self.assertAlmostEqual(atan2(0, 1), 0)
        self.assertAlmostEqual(atan2(1, 0), 90)
        self.assertAlmostEqual(atan2(0, -1), 180)
        self.assertAlmostEqual(atan2(-1, 0), -90)

        # Negative zeros
        self.assertAlmostEqual(atan2(-0.0, 1), 0)
        self.assertAlmostEqual(atan2(1, -0.0), 90)
        self.assertAlmostEqual(atan2(-0.0, -1), -180)
        self.assertAlmostEqual(atan2(-1, -0.0), -90)

    def test_arctangent2_in_1st_quadrant(self):
        self.assertAlmostEqual(atan2(1/2, SQRT_3/2), 30)
        self.assertAlmostEqual(atan2(SQRT_2/2, SQRT_2/2), 45)
        self.assertAlmostEqual(atan2(SQRT_3/2, 1/2), 60)

    def test_arctangent2_in_2nd_quadrant(self):
        self.assertAlmostEqual(atan2(SQRT_3/2, -1/2), 120)
        self.assertAlmostEqual(atan2(SQRT_2/2, -SQRT_2/2), 135)
        self.assertAlmostEqual(atan2(1/2, -SQRT_3/2), 150)

    def test_arctangent2_in_3rd_quadrant(self):
        self.assertAlmostEqual(atan2(-1/2, -SQRT_3/2), -150)
        self.assertAlmostEqual(atan2(-SQRT_2/2, -SQRT_2/2), -135)
        self.assertAlmostEqual(atan2(-SQRT_3/2, -1/2), -120)

    def test_arctangent2_in_4th_quadrant(self):
        self.assertAlmostEqual(atan2(-SQRT_3/2, 1/2), -60)
        self.assertAlmostEqual(atan2(-SQRT_2/2, SQRT_2/2), -45)
        self.assertAlmostEqual(atan2(-1/2, SQRT_3/2), -30)
