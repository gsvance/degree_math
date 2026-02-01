"""degree_math

An alternative version of the Python math module with trig functions that
operate in degrees. This module is identical to the built-in math module, but
the trig functions are in degree mode instead of defaulting to radians.
"""

import math as _math
import typing as _typing

from math import *


type _SupportsFloatOrIndex = _typing.SupportsFloat | _typing.SupportsIndex


def sin(x: _SupportsFloatOrIndex, /) -> float:
    return _math.sin(_math.degrees(x))


def cos(x: _SupportsFloatOrIndex, /) -> float:
    return _math.cos(_math.degrees(x))


def tan(x: _SupportsFloatOrIndex, /) -> float:
    return _math.tan(_math.degrees(x))


def asin(x: _SupportsFloatOrIndex, /) -> float:
    return _math.degrees(_math.asin(x))


def acos(x: _SupportsFloatOrIndex, /) -> float:
    return _math.degrees(_math.acos(x))


def atan(x: _SupportsFloatOrIndex) -> float:
    return _math.degrees(_math.atan(x))


def atan2(y: _SupportsFloatOrIndex, x: _SupportsFloatOrIndex, /) -> float:
    return _math.degrees(_math.atan2(y, x))
