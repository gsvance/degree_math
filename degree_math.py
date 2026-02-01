"""degree_math

An alternative version of the Python math module with trig functions that
operate in degrees. This module is identical to the built-in math module, but
the trig functions are in degree mode instead of defaulting to radians.
"""

import math as _math

from math import *


def sin(x):
    return _math.sin(_math.degrees(x))


def cos(x):
    return _math.cos(_math.degrees(x))


def tan(x):
    return _math.tan(_math.degrees(x))


def asin(x):
    return _math.degrees(_math.asin(x))


def acos(x):
    return _math.degrees(_math.acos(x))


def atan(x):
    return _math.degrees(_math.atan(x))


def atan2(y, x):
    return _math.degrees(_math.atan2(y, x))

