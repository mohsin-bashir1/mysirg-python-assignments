#Write a python script which takes the radius from the user and display area of a circle

from math import pi

radius = float(input("Enter the radius of the circle: "))

area = pi * radius ** 2

print(f"Area of a circle having {radius} radius is {area:.2f} square units.")