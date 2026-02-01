"""Unit tests for the inverse (arc) trig functions in degree_math."""

import math
import unittest

from degree_math import asin, acos, atan, atan2


class TestInverseTrigFunctions(unittest.TestCase):

    def test_arcsine(self):

        # Negative inputs
        self.assertAlmostEqual(asin(-1), -90)
        self.assertAlmostEqual(asin(-math.sqrt(3)/2), -60)
        self.assertAlmostEqual(asin(-math.sqrt(2)/2), -45)
        self.assertAlmostEqual(asin(-1/2), -30)
        self.assertAlmostEqual(asin(-0.0), 0)

        # Positive inputs
        self.assertAlmostEqual(asin(0), 0)
        self.assertAlmostEqual(asin(1/2), 30)
        self.assertAlmostEqual(asin(math.sqrt(2)/2), 45)
        self.assertAlmostEqual(asin(math.sqrt(3)/2), 60)
        self.assertAlmostEqual(asin(1), 90)

    def test_arccosine(self):

        # Negative inputs
        self.assertAlmostEqual(acos(-1), 180)
        self.assertAlmostEqual(acos(-math.sqrt(3)/2), 150)
        self.assertAlmostEqual(acos(-math.sqrt(2)/2), 135)
        self.assertAlmostEqual(acos(-1/2), 120)
        self.assertAlmostEqual(acos(-0.0), 90)

        # Positive inputs
        self.assertAlmostEqual(acos(0), 90)
        self.assertAlmostEqual(acos(1/2), 60)
        self.assertAlmostEqual(acos(math.sqrt(2)/2), 45)
        self.assertAlmostEqual(acos(math.sqrt(3)/2), 30)
        self.assertAlmostEqual(acos(1), 0)

    def test_arctangent(self):

        # Negative inputs
        self.assertAlmostEqual(atan(float('-inf')), -90)
        self.assertAlmostEqual(atan(-math.sqrt(3)), -60)
        self.assertAlmostEqual(atan(-1), -45)
        self.assertAlmostEqual(atan(-math.sqrt(3)/3), -30)
        self.assertAlmostEqual(atan(-0.0), 0)

        # Positive inputs
        self.assertAlmostEqual(atan(0), 0)
        self.assertAlmostEqual(atan(math.sqrt(3)/3), 30)
        self.assertAlmostEqual(atan(1), 45)
        self.assertAlmostEqual(atan(math.sqrt(3)), 60)
        self.assertAlmostEqual(atan(float('inf')), 90)

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
        self.assertAlmostEqual(atan2(1/2, math.sqrt(3)/2), 30)
        self.assertAlmostEqual(atan2(math.sqrt(2)/2, math.sqrt(2)/2), 45)
        self.assertAlmostEqual(atan2(math.sqrt(3)/2, 1/2), 60)

    def test_arctangent2_in_2nd_quadrant(self):
        self.assertAlmostEqual(atan2(math.sqrt(3)/2, -1/2), 120)
        self.assertAlmostEqual(atan2(math.sqrt(2)/2, -math.sqrt(2)/2), 135)
        self.assertAlmostEqual(atan2(1/2, -math.sqrt(3)/2), 150)

    def test_arctangent2_in_3rd_quadrant(self):
        self.assertAlmostEqual(atan2(-1/2, -math.sqrt(3)/2), -150)
        self.assertAlmostEqual(atan2(-math.sqrt(2)/2, -math.sqrt(2)/2), -135)
        self.assertAlmostEqual(atan2(-math.sqrt(3)/2, -1/2), -120)

    def test_arctangent2_in_4th_quadrant(self):
        self.assertAlmostEqual(atan2(-math.sqrt(3)/2, 1/2), -60)
        self.assertAlmostEqual(atan2(-math.sqrt(2)/2, math.sqrt(2)/2), -45)
        self.assertAlmostEqual(atan2(-1/2, math.sqrt(3)/2), -30)
