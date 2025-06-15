'''Write a python script which takes a three digit number
from the user and displays only its first digit.'''

temp = number = int(input("Enter three digit number: "))

temp //= 100
print('The first digit of {} is {}'.format(number, temp))