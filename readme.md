Almanac
-------
Almanac is a Python module for calculating rise and set times of the Sun and
Moon for a given location and time. The following calculations are currently
supported:
* illuminated fraction of Moon's disc
* lunar position
* moonrise and moonset
* solar position
* sunrise and sunset
* rise, transit and set of a body for a given location and time

The calculations are based on *Astronomical Algorithms, 2nd Edition* by Jean
Meeus, published by Willmann-Bell, 1998. There are no guarantees as to
accuracy. I've tested using the sample calculations in the books and from a
few external sources. At best, the rise and set times are only accurate to
within a minute or two. At worst, I made mistakes and the accuracy is even less.

Some other calculations I might add:
* atmospheric refraction
* dates of phases of the moon
* dates of equinoxes and solstices
