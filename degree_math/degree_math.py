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


type _Converter = _typing.Callable[[_SupportsFloatOrIndex], float]

_forward_converter: _Converter = _math.radians
_inverse_converter: _Converter = _math.degrees


def set_mode(
    mode: _typing.Literal['degrees', 'radians'] | None = None,
) -> _typing.Literal['degrees', 'radians']:
    """Set the trig function mode to 'degrees' or 'radians'.

    Returns the current mode as a string, even if called without arguments.
    """
    global _forward_converter, _inverse_converter
    match mode:
        case 'degrees':
            _forward_converter = _math.radians
            _inverse_converter = _math.degrees
            return mode
        case 'radians':
            _forward_converter = float
            _inverse_converter = float
            return mode
        case None:
            if _forward_converter is _math.radians:
                return 'degrees'
            return 'radians'
        case _:
            raise TypeError(f'value for mode cannot be {mode!r}')


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
    return _math.sin(_forward_converter(x))


@_rewrite_docstring
def cos(x: _SupportsFloatOrIndex, /) -> float:
    return _math.cos(_forward_converter(x))


@_rewrite_docstring
def tan(x: _SupportsFloatOrIndex, /) -> float:
    return _math.tan(_forward_converter(x))


# Overwrite the asin(), acos(), atan(), and atan2() functions to return values
# in degrees. First call the standard functions, then convert the output to
# degrees before returning it.

@_rewrite_docstring
def asin(x: _SupportsFloatOrIndex, /) -> float:
    return _inverse_converter(_math.asin(x))


@_rewrite_docstring
def acos(x: _SupportsFloatOrIndex, /) -> float:
    return _inverse_converter(_math.acos(x))


@_rewrite_docstring
def atan(x: _SupportsFloatOrIndex) -> float:
    return _inverse_converter(_math.atan(x))


@_rewrite_docstring
def atan2(y: _SupportsFloatOrIndex, x: _SupportsFloatOrIndex, /) -> float:
    return _inverse_converter(_math.atan2(y, x))
