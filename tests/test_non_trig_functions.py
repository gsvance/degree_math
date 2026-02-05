"""Unit tests for the other functions that degree_math borrows from math."""

import math
from typing import Final
import unittest

import degree_math


TRIG_FUNCTION_NAMES: Final[list[str]] = [
    'sin', 'cos', 'tan',
    'asin', 'acos', 'atan', 'atan2',
]


class TestNonTrigFunctions(unittest.TestCase):

    def test_non_trig_function_ids(self):
        for name in dir(math):
            if name.startswith('__') or name in TRIG_FUNCTION_NAMES:
                continue
            self.assertIs(getattr(degree_math, name), getattr(math, name))

    def test_trig_function_ids(self):
        for name in TRIG_FUNCTION_NAMES:
            self.assertIsNot(getattr(degree_math, name), getattr(math, name))

    def test_simple_non_trig_calculations(self):
        self.assertEqual(degree_math.lcm(8, 10), 40)
        self.assertEqual(degree_math.floor(4.7), 4)
        self.assertTrue(degree_math.isnan(float('nan')))
        self.assertAlmostEqual(degree_math.sqrt(9), 3)
        self.assertAlmostEqual(degree_math.hypot(5, 12), 13)
        self.assertAlmostEqual(degree_math.degrees(math.pi), 180)
        self.assertAlmostEqual(degree_math.cosh(0), 1)
        self.assertAlmostEqual(degree_math.gamma(5), 24)
        self.assertAlmostEqual(degree_math.e, math.exp(1))
