"""Python's math module, but with trig functions that operate in degrees.

The degree_math module is an alternative version of Python's standard library
math module with trigonometric functions that operate in degrees instead of
radians. All other functions from the math module are also available here, but
those do not operate any differently.
"""

import math as _math
import typing as _typing


# Make everything from the standard math module available in this namespace.
from math import *


# Set up a quick type alias for annotating the expected input types of all the
# trig functions.
type _SupportsFloatOrIndex = _typing.SupportsFloat | _typing.SupportsIndex


# The following decorator writes the docstrings for the trig functions in this
# module by looking up the corresponding functions in the standard math module
# and then replacing a few select substrings.
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


# Overwrite the sin(), cos(), and tan() functions to expect their arguments in
# degrees. First convert the argument to radians, and then call the standard
# function from there.

@_rewrite_docstring
def sin(x: _SupportsFloatOrIndex, /) -> float:
    return _math.sin(_math.radians(x))


@_rewrite_docstring
def cos(x: _SupportsFloatOrIndex, /) -> float:
    return _math.cos(_math.radians(x))


@_rewrite_docstring
def tan(x: _SupportsFloatOrIndex, /) -> float:
    return _math.tan(_math.radians(x))


# Overwrite the asin(), acos(), atan(), and atan2() functions to return values
# in degrees. First call the standard functions, then convert the output to
# degrees before returning it.

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
