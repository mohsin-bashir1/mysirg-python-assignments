'''Write a python script to add two numbers 25 (in octal) and 39 (in hexadecimal)
and display the result in binary format'''

a = 0o25
b = 0x39
c = a + b

print(c, bin(c), sep=" --> ")
