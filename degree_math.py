"""degree_math

An alternative version of the Python math module with trig functions that
operate in degrees. This module is identical to the built-in math module, but
the trig functions are in degree mode instead of defaulting to radians.
"""

import math as _math
import typing as _typing

from math import *


__all__ = [_name for _name in dir(_math) if not _name.startswith('__')]


type _SupportsFloatOrIndex = _typing.SupportsFloat | _typing.SupportsIndex


# This decorator writes docstrings for the trig functions in this module by
# looking up the corresponding function in the built-in math module and
# replacing a few select substrings in its docstring
def _rewrite_docstring[**P, R](
    new_function: _typing.Callable[P, R],
) -> _typing.Callable[P, R]:

    old_function = getattr(_math, new_function.__name__)
    assert isinstance(old_function.__doc__, str)

    new_function.__doc__ = (
        old_function.__doc__
        .replace('radians', 'degrees')
        .replace('pi/2', '90')
        .replace('pi', '180')
    )

    return new_function


@_rewrite_docstring
def sin(x: _SupportsFloatOrIndex, /) -> float:
    return _math.sin(_math.degrees(x))


@_rewrite_docstring
def cos(x: _SupportsFloatOrIndex, /) -> float:
    return _math.cos(_math.degrees(x))


@_rewrite_docstring
def tan(x: _SupportsFloatOrIndex, /) -> float:
    return _math.tan(_math.degrees(x))


@_rewrite_docstring
def asin(x: _SupportsFloatOrIndex, /) -> float:
    return _math.degrees(_math.asin(x))


@_rewrite_docstring
def acos(x: _SupportsFloatOrIndex, /) -> float:
    return _math.degrees(_math.acos(x))


@_rewrite_docstring
def atan(x: _SupportsFloatOrIndex) -> float:
    return _math.degrees(_math.atan(x))


@_rewrite_docstring
def atan2(y: _SupportsFloatOrIndex, x: _SupportsFloatOrIndex, /) -> float:
    return _math.degrees(_math.atan2(y, x))
