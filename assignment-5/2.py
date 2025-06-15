'''Write a python script to get the last digit from a given number.
(e.g., if user enters 2089 then your output should be 9)'''

temp = number = int(input("Enter a number: "))

#performing the modulus operaton
temp %= 10
print(f"The last digit of {number} is {temp}")