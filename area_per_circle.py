#!/usr/bin/env python3
# Created by: Viviana Hurtado
# Date: march 7 2025
# This program calculates and displays the area
# and perimeter for a given user input
import math

radius = float(input("Enter the radius of the circle: "))
area = math.pi * radius**2
circumference = 2 * math.pi * radius

print(f"The area of the circle is: {round(area, 2)}cm^2")
print(f"The circumference of the circle is: {round(circumference, 2)}cm")
