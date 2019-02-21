#Circle area/circumference
#Andrew Riedlinger
#February 21st, 2019
#
#Contains methods for the perimeter and area of a cricle

import math

def area(radius):
    """Returns area of a circle with given radius"""
    #pi*r^2
    return math.pi * radius ** 2

def circumference(radius):
    """Returns circumference of a circle with given radius"""
    #pi * D
    return math.pi * 2 * radius;
