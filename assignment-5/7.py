'''Write a python script which takes a three digit number from the user
and displays only its last digit.'''

temp = number = int(input('Enter three digit number: '))

number %= 10
print("The last digit of %d is %d" %(temp, number))