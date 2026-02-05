# Degree Math

Are you searching for an alternative version of [Python's `math` module](https://docs.python.org/3/library/math.html) where the trig functions operate in degrees instead of radians?
Look no further!

The `degree_math` module is a wrapper around Python's standard library `math` module that exposes all the same mathematical functions, but changes the trigonometric functions so that they operate in degrees rather than radians.
Much like how a handheld scientific calculator can be switched from "radian mode" into "degree mode," `degree_math` is Python's `math` module operating in "degree mode."

## Example Usage

```python
>>> import degree_math as dmath
>>> # Trig functions take arguments in degrees
>>> dmath.sin(90)
1.0
>>> dmath.sin(30)
0.49999999999999994
>>> dmath.cos(180)
-1.0
>>> dmath.cos(135)
-0.7071067811865475
>>> dmath.tan(45)
0.9999999999999999
>>> dmath.tan(-45)
-0.9999999999999999
>>> # Inverse trig functions return values in degrees
>>> dmath.asin(dmath.sqrt(3) / 2)
59.99999999999999
>>> dmath.acos(0)
90.0
>>> dmath.atan(1)
45.0
>>> dmath.atan2(-dmath.sqrt(2) / 2, -dmath.sqrt(2) / 2)
-135.0
>>> # All other math functions work exactly the same
>>> dmath.sqrt(2)
1.4142135623730951
```

## Installation

_Coming soon_

## How It Works

Arguments passed to `sin()`, `cos()`, and `tan()` are automatically sent through the `math.radians()` function before being routed to their respective trig functions in the `math` module.
For inverse trig functions, the return values from `asin()`, `acos()`, `atan()`, and `atan2()` are automatically sent through the `math.degrees()` function before they are returned.

## License

_Coming soon_
