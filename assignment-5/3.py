#Write a python script to swap data of two variables.

print("Enter two number: ")
n1, n2 = int(input()), int(input())

print(f"Before swap n1 = {n1} and n2 = {n2}")
n1, n2 = n2, n1
print(f"After swap n1 = {n1} and n2 = {n2}")