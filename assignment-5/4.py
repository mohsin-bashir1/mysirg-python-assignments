#Write a python script to find x power y, where values of x and y are given by user.

from math import pow

print('Enter values for base and exponent: ')
base, exponent = int(input()), int(input())

#calculating exponentiation using exponentiation operator.
print(f"{base} raised to {exponent} is {base ** exponent} ")
#by using pow function of math module.
print(f"{base} raised to {exponent} is {pow(base,exponent)} ")