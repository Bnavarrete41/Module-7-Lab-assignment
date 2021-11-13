# Brandon Navarrete
# 11/12/2021
# Problem number 1 this will be showing the area of a circle and return it to the person inputting the code

import math

def areaOfCircle(r):
    area = math.pi * r * r
    return area

radius = 5
print("Area", round(areaOfCircle(radius), 2))
