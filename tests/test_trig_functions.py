"""Unit tests for the normal forward trig functions in degree_math."""

import math
from typing import Final
import unittest

from degree_math import sin, cos, tan


SQRT_2: Final[float] = math.sqrt(2)
SQRT_3: Final[float] = math.sqrt(3)


class TestTrigFunctions(unittest.TestCase):

    def test_sine_on_x_and_y_axes(self):

        # Positive angles
        self.assertAlmostEqual(sin(0), 0)
        self.assertAlmostEqual(sin(90), 1)
        self.assertAlmostEqual(sin(180), 0)
        self.assertAlmostEqual(sin(270), -1)
        self.assertAlmostEqual(sin(360), 0)

        # Negative angles
        self.assertAlmostEqual(sin(-360), 0)
        self.assertAlmostEqual(sin(-270), 1)
        self.assertAlmostEqual(sin(-180), 0)
        self.assertAlmostEqual(sin(-90), -1)
        self.assertAlmostEqual(sin(-0.0), 0)

    def test_sine_in_1st_quadrant(self):

        # Positive angles
        self.assertAlmostEqual(sin(30), 1/2)
        self.assertAlmostEqual(sin(45), SQRT_2/2)
        self.assertAlmostEqual(sin(60), SQRT_3/2)

        # Negative angles
        self.assertAlmostEqual(sin(-330), 1/2)
        self.assertAlmostEqual(sin(-315), SQRT_2/2)
        self.assertAlmostEqual(sin(-300), SQRT_3/2)

    def test_sine_in_2nd_quadrant(self):

        # Positive angles
        self.assertAlmostEqual(sin(120), SQRT_3/2)
        self.assertAlmostEqual(sin(135), SQRT_2/2)
        self.assertAlmostEqual(sin(150), 1/2)

        # Negative angles
        self.assertAlmostEqual(sin(-240), SQRT_3/2)
        self.assertAlmostEqual(sin(-225), SQRT_2/2)
        self.assertAlmostEqual(sin(-210), 1/2)

    def test_sine_in_3rd_quadrant(self):

        # Positive angles
        self.assertAlmostEqual(sin(210), -1/2)
        self.assertAlmostEqual(sin(225), -SQRT_2/2)
        self.assertAlmostEqual(sin(240), -SQRT_3/2)

        # Negative angles
        self.assertAlmostEqual(sin(-150), -1/2)
        self.assertAlmostEqual(sin(-135), -SQRT_2/2)
        self.assertAlmostEqual(sin(-120), -SQRT_3/2)

    def test_sine_in_4th_quadrant(self):

        # Positive angles
        self.assertAlmostEqual(sin(300), -SQRT_3/2)
        self.assertAlmostEqual(sin(315), -SQRT_2/2)
        self.assertAlmostEqual(sin(330), -1/2)

        # Negative angles
        self.assertAlmostEqual(sin(-60), -SQRT_3/2)
        self.assertAlmostEqual(sin(-45), -SQRT_2/2)
        self.assertAlmostEqual(sin(-30), -1/2)

    def test_cosine_on_x_and_y_axes(self):

        # Positive angles
        self.assertAlmostEqual(cos(0), 1)
        self.assertAlmostEqual(cos(90), 0)
        self.assertAlmostEqual(cos(180), -1)
        self.assertAlmostEqual(cos(270), 0)
        self.assertAlmostEqual(cos(360), 1)

        # Negative angles
        self.assertAlmostEqual(cos(-360), 1)
        self.assertAlmostEqual(cos(-270), 0)
        self.assertAlmostEqual(cos(-180), -1)
        self.assertAlmostEqual(cos(-90), 0)
        self.assertAlmostEqual(cos(-0.0), 1)

    def test_cosine_in_1st_quadrant(self):

        # Positive angles
        self.assertAlmostEqual(cos(30), SQRT_3/2)
        self.assertAlmostEqual(cos(45), SQRT_2/2)
        self.assertAlmostEqual(cos(60), 1/2)

        # Negative angles
        self.assertAlmostEqual(cos(-330), SQRT_3/2)
        self.assertAlmostEqual(cos(-315), SQRT_2/2)
        self.assertAlmostEqual(cos(-300), 1/2)

    def test_cosine_in_2nd_quadrant(self):

        # Positive angles
        self.assertAlmostEqual(cos(120), -1/2)
        self.assertAlmostEqual(cos(135), -SQRT_2/2)
        self.assertAlmostEqual(cos(150), -SQRT_3/2)

        # Negative angles
        self.assertAlmostEqual(cos(-240), -1/2)
        self.assertAlmostEqual(cos(-225), -SQRT_2/2)
        self.assertAlmostEqual(cos(-210), -SQRT_3/2)

    def test_cosine_in_3rd_quadrant(self):

        # Positive angles
        self.assertAlmostEqual(cos(210), -SQRT_3/2)
        self.assertAlmostEqual(cos(225), -SQRT_2/2)
        self.assertAlmostEqual(cos(240), -1/2)

        # Negative angles
        self.assertAlmostEqual(cos(-150), -SQRT_3/2)
        self.assertAlmostEqual(cos(-135), -SQRT_2/2)
        self.assertAlmostEqual(cos(-120), -1/2)

    def test_cosine_in_4th_quadrant(self):

        # Positive angles
        self.assertAlmostEqual(cos(300), 1/2)
        self.assertAlmostEqual(cos(315), SQRT_2/2)
        self.assertAlmostEqual(cos(330), SQRT_3/2)

        # Negative angles
        self.assertAlmostEqual(cos(-60), 1/2)
        self.assertAlmostEqual(cos(-45), SQRT_2/2)
        self.assertAlmostEqual(cos(-30), SQRT_3/2)

    def test_tangent_on_x_and_y_axes(self):

        # Positive angles
        self.assertAlmostEqual(tan(0), 0)
        self.assertAlmostEqual(1/tan(90), 0)  # infinite
        self.assertAlmostEqual(tan(180), 0)
        self.assertAlmostEqual(1/tan(270), 0)  # infinite
        self.assertAlmostEqual(tan(360), 0)

        # Negative angles
        self.assertAlmostEqual(tan(-360), 0)
        self.assertAlmostEqual(1/tan(-270), 0)  # infinite
        self.assertAlmostEqual(tan(-180), 0)
        self.assertAlmostEqual(1/tan(-90), 0)  # infinite
        self.assertAlmostEqual(tan(-0.0), 0)

    def test_tangent_in_1st_quadrant(self):

        # Positive angles
        self.assertAlmostEqual(tan(30), SQRT_3/3)
        self.assertAlmostEqual(tan(45), 1)
        self.assertAlmostEqual(tan(60), SQRT_3)

        # Negative angles
        self.assertAlmostEqual(tan(-330), SQRT_3/3)
        self.assertAlmostEqual(tan(-315), 1)
        self.assertAlmostEqual(tan(-300), SQRT_3)

    def test_tangent_in_2nd_quadrant(self):

        # Positive angles
        self.assertAlmostEqual(tan(120), -SQRT_3)
        self.assertAlmostEqual(tan(135), -1)
        self.assertAlmostEqual(tan(150), -SQRT_3/3)

        # Negative angles
        self.assertAlmostEqual(tan(-240), -SQRT_3)
        self.assertAlmostEqual(tan(-225), -1)
        self.assertAlmostEqual(tan(-210), -SQRT_3/3)

    def test_tangent_in_3rd_quadrant(self):

        # Positive angles
        self.assertAlmostEqual(tan(210), SQRT_3/3)
        self.assertAlmostEqual(tan(225), 1)
        self.assertAlmostEqual(tan(240), SQRT_3)

        # Negative angles
        self.assertAlmostEqual(tan(-150), SQRT_3/3)
        self.assertAlmostEqual(tan(-135), 1)
        self.assertAlmostEqual(tan(-120), SQRT_3)

    def test_tangent_in_4th_quadrant(self):

        # Positive angles
        self.assertAlmostEqual(tan(300), -SQRT_3)
        self.assertAlmostEqual(tan(315), -1)
        self.assertAlmostEqual(tan(330), -SQRT_3/3)

        # Negative angles
        self.assertAlmostEqual(tan(-60), -SQRT_3)
        self.assertAlmostEqual(tan(-45), -1)
        self.assertAlmostEqual(tan(-30), -SQRT_3/3)
