#Write a python script to calculate the area of Triangle. Number is entered by the user

from math import sqrt

print("Enter the length of three sides of a triangle: ")
s1, s2, s3 = int(input()), int(input()), int(input())

sp = (s1 + s2 + s3) / 2

area = sqrt(sp * (sp - s1) * (sp - s2) * (sp - s3))

print("Area of a triangle with sides %d, %d and %d is %.2f square units." %(s1, s2, s3, area))