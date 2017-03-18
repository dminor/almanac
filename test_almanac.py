# Copyright (c) 2017 Daniel Minor
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
import unittest
import math

import almanac


class TestAlmanac(unittest.TestCase):

    def assertFuzzyEquals(self, a, b, eps=0.01):
        self.assertTrue(math.fabs(a - b) < eps,
                        "Difference between expected value %f and actual value"
                        " %f is too large (%f, eps=%f)" %
                        (a, b, math.fabs(a - b), eps))


    def test_apparent_sidereal_time_greenwich(self):
        self.assertFuzzyEquals(almanac.hms_to_deg(13, 10, 46.1351),
                               almanac.apparent_sidereal_time_greenwich(1987, 4, 10), 0.00001)

    def test_deg_to_hms(self):
        h, m, s = almanac.deg_to_hms(232.64)
        self.assertEquals(15, h)
        self.assertEquals(30, m)
        self.assertFuzzyEquals(33.59, s)

        h, m, s = almanac.deg_to_hms(12)
        self.assertEquals(0, h)
        self.assertEquals(48, m)
        self.assertFuzzyEquals(0, s)

        h, m, s = almanac.deg_to_hms(345)
        self.assertEquals(23, h)
        self.assertEquals(0, m)
        self.assertFuzzyEquals(0, s)

        h, m, s = almanac.deg_to_hms(119.7)
        self.assertEquals(7, h)
        self.assertEquals(58, m)
        self.assertFuzzyEquals(48.00, s)


    def test_hms_to_deg(self):
        self.assertFuzzyEquals(119.7, almanac.hms_to_deg(7, 58, 48))
        self.assertFuzzyEquals(227.03, almanac.hms_to_deg(15, 8, 7))

    def test_illuminated_fraction_of_moon(self):
        f = almanac.illuminated_fraction_of_moon(1992, 4, 12)
        self.assertFuzzyEquals(0.678, f, 0.001)
        f = almanac.illuminated_fraction_of_moon(2017, 3, 16.83)
        self.assertFuzzyEquals(0.833, f, 0.001)

    def test_julian_day(self):
        self.assertEquals(2436116.31, almanac.julian_day(1957, 10, 4.81))
        self.assertEquals(2451545.0, almanac.julian_day(2000, 1, 1.5))
        self.assertEquals(2451179.5, almanac.julian_day(1999, 1, 1.0))
        self.assertEquals(2446822.5, almanac.julian_day(1987, 1, 27.0))
        self.assertEquals(2446966.0, almanac.julian_day(1987, 6, 19.5))
        self.assertEquals(2447187.5, almanac.julian_day(1988, 1, 27.0))
        self.assertEquals(2447332.0, almanac.julian_day(1988, 6, 19.5))
        self.assertEquals(2415020.5, almanac.julian_day(1900, 1, 1.0))
        self.assertEquals(2305447.5, almanac.julian_day(1600, 1, 1.0))
        self.assertEquals(2305812.5, almanac.julian_day(1600, 12, 31.0))
        self.assertEquals(2026871.8, almanac.julian_day(837, 4, 10.3, False))
        self.assertEquals(1676496.5, almanac.julian_day(-123, 12, 31.0, False))
        self.assertEquals(1676497.5, almanac.julian_day(-122, 1, 1.0, False))
        self.assertEquals(1356001.0, almanac.julian_day(-1000, 7, 12.5, False))
        self.assertEquals(1355866.5, almanac.julian_day(-1000, 2, 29, False))
        self.assertEquals(1355671.4, almanac.julian_day(-1001, 8, 17.9, False))
        self.assertEquals(0.0, almanac.julian_day(-4712, 1, 1.5, False))

    def test_lunar_position(self):
        right_ascension, declination, radius = almanac.lunar_position(1992, 4, 12)
        self.assertFuzzyEquals(right_ascension, 134.688470, 0.001)
        self.assertFuzzyEquals(declination, 13.768368, 0.001)
        self.assertFuzzyEquals(radius, 368409.7, 0.1)

    def test_mean_sidereal_time_greenwich(self):
        self.assertFuzzyEquals(almanac.hms_to_deg(13, 10, 46.3668),
                               almanac.mean_sidereal_time_greenwich(1987, 4, 10))

        self.assertFuzzyEquals(128.73787,
                               almanac.mean_sidereal_time_greenwich(1987, 4, 10.80625), 0.00001)


    def test_moonrise_moonset(self):
        # Source data for expected values is accurate to +/- 2 minutes
        eps = 2.0/60.0

        moonrise, moonset = almanac.moonrise_moonset(45.4215, -75.6972, 2017, 3, 16)
        self.assertFuzzyEquals(2.40, moonrise, eps)
        self.assertFuzzyEquals(13.37, moonset, eps)


    def test_nutation(self):
        delta_phi, delta_eps, eps = almanac.nutation(1987, 4, 10)
        self.assertFuzzyEquals(-0.001052, delta_phi, 0.000001)
        self.assertFuzzyEquals(0.002623, delta_eps, 0.000001)
        self.assertFuzzyEquals(23 + 26/60.0 + 36.850/3600.0,
                               eps + delta_eps, 0.001)

    def test_rise_transit_set(self):
        r, t, s = almanac.rise_transit_set(42.3333, -71.0833,
                                           1988, 3, 20, -0.5667,
                                           [[40.68021, 18.04761],
                                            [41.73129, 18.44092],
                                            [42.78204, 18.82742]], 56)

        self.assertFuzzyEquals(0.51766, r, 0.000005)
        self.assertFuzzyEquals(0.81980, t, 0.000005)
        self.assertFuzzyEquals(0.12130, s, 0.000005)

    def test_solar_position(self):
        right_ascension, declination, distance = almanac.solar_position(1992, 10, 13)
        self.assertFuzzyEquals(-161.61917, right_ascension, 0.00001)
        self.assertFuzzyEquals(-7.78507, declination, 0.00001)
        self.assertFuzzyEquals(0.99766, distance, 0.00001)

    def test_sunrise_sunset(self):
        # Source data for expected values is accurate to +/- 2 minutes
        eps = 2.0/60.0

        sunrise, sunset = almanac.sunrise_sunset(45.4215, -75.6972, 2017, 3, 13)
        self.assertFuzzyEquals(11.32, sunrise, eps)
        self.assertFuzzyEquals(23.12, sunset, eps)

        sunrise, sunset = almanac.sunrise_sunset(45.4215, -75.6972, 2017, 6, 20)
        self.assertFuzzyEquals(9.25, sunrise, eps)
        self.assertFuzzyEquals(0.9, sunset, eps)

        # Civil twilight
        sunrise, sunset = almanac.sunrise_sunset(45.4215, -75.6972, 2017, 3, 13, -6.0)
        self.assertFuzzyEquals(10.82, sunrise, eps)
        self.assertFuzzyEquals(23.6, sunset, eps)

        # Inuvik, NT
        sunrise, sunset = almanac.sunrise_sunset(68.72, -133.36, 2017, 6, 20)
        self.assertTrue(math.isnan(sunrise))
        self.assertTrue(math.isnan(sunset))
