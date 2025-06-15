'''Write a python script to remove the last digit from a given number.
(e.g., if user enters 2534 then your output should be 253)'''

number = temp = int(input("Enter a number: "))

#performing the floor division
temp //= 10
print(f"The {number} without last digit is {temp}")