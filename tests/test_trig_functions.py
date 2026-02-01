"""Unit tests for the normal forward trig functions in degree_math."""

import math
import unittest

from degree_math import sin, cos, tan


class TestTrigFunctions(unittest.TestCase):

    def test_sine_on_x_and_y_axes(self):
        self.assertAlmostEqual(sin(0), 0)
        self.assertAlmostEqual(sin(90), 1)
        self.assertAlmostEqual(sin(180), 0)
        self.assertAlmostEqual(sin(270), -1)
        self.assertAlmostEqual(sin(360), 0)

    def test_sine_in_1st_quadrant(self):
        self.assertAlmostEqual(sin(30), 1/2)
        self.assertAlmostEqual(sin(45), math.sqrt(2)/2)
        self.assertAlmostEqual(sin(60), math.sqrt(3)/2)

    def test_sine_in_2nd_quadrant(self):
        self.assertAlmostEqual(sin(120), math.sqrt(3)/2)
        self.assertAlmostEqual(sin(135), math.sqrt(2)/2)
        self.assertAlmostEqual(sin(150), 1/2)

    def test_sine_in_3rd_quadrant(self):
        self.assertAlmostEqual(sin(210), -1/2)
        self.assertAlmostEqual(sin(225), -math.sqrt(2)/2)
        self.assertAlmostEqual(sin(240), -math.sqrt(3)/2)

    def test_sine_in_4th_quadrant(self):
        self.assertAlmostEqual(sin(300), -math.sqrt(3)/2)
        self.assertAlmostEqual(sin(315), -math.sqrt(2)/2)
        self.assertAlmostEqual(sin(330), -1/2)

    def test_cosine_on_x_and_y_axes(self):
        self.assertAlmostEqual(cos(0), 1)
        self.assertAlmostEqual(cos(90), 0)
        self.assertAlmostEqual(cos(180), -1)
        self.assertAlmostEqual(cos(270), 0)
        self.assertAlmostEqual(cos(360), 1)

    def test_cosine_in_1st_quadrant(self):
        self.assertAlmostEqual(cos(30), math.sqrt(3)/2)
        self.assertAlmostEqual(cos(45), math.sqrt(2)/2)
        self.assertAlmostEqual(cos(60), 1/2)

    def test_cosine_in_2nd_quadrant(self):
        self.assertAlmostEqual(cos(120), -1/2)
        self.assertAlmostEqual(cos(135), -math.sqrt(2)/2)
        self.assertAlmostEqual(cos(150), -math.sqrt(3)/2)

    def test_cosine_in_3rd_quadrant(self):
        self.assertAlmostEqual(cos(210), -math.sqrt(3)/2)
        self.assertAlmostEqual(cos(225), -math.sqrt(2)/2)
        self.assertAlmostEqual(cos(240), -1/2)

    def test_cosine_in_4th_quadrant(self):
        self.assertAlmostEqual(cos(300), 1/2)
        self.assertAlmostEqual(cos(315), math.sqrt(2)/2)
        self.assertAlmostEqual(cos(330), math.sqrt(3)/2)

    def test_tangent_on_x_and_y_axes(self):
        self.assertAlmostEqual(tan(0), 0)
        self.assertAlmostEqual(1/tan(90), 0)  # infinite
        self.assertAlmostEqual(tan(180), 0)
        self.assertAlmostEqual(1/tan(270), 0)  # infinite
        self.assertAlmostEqual(tan(360), 0)

    def test_tangent_in_1st_quadrant(self):
        self.assertAlmostEqual(tan(30), math.sqrt(3)/3)
        self.assertAlmostEqual(tan(45), 1)
        self.assertAlmostEqual(tan(60), math.sqrt(3))

    def test_tangent_in_2nd_quadrant(self):
        self.assertAlmostEqual(tan(120), -math.sqrt(3))
        self.assertAlmostEqual(tan(135), -1)
        self.assertAlmostEqual(tan(150), -math.sqrt(3)/3)

    def test_tangent_in_3rd_quadrant(self):
        self.assertAlmostEqual(tan(210), math.sqrt(3)/3)
        self.assertAlmostEqual(tan(225), 1)
        self.assertAlmostEqual(tan(240), math.sqrt(3))

    def test_tangent_in_4th_quadrant(self):
        self.assertAlmostEqual(tan(300), -math.sqrt(3))
        self.assertAlmostEqual(tan(315), -1)
        self.assertAlmostEqual(tan(330), -math.sqrt(3)/3)
