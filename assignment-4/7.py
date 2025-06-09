#Write a python script to calculate average of three numbers, entered by the user.

print("Enter three numbers: ")
n1, n2, n3 = int(input()), int(input()), int(input())

average = (n1 + n2 + n3) / 3

print(f"Average of {n1}, {n2}, and {n3} is {average:.2f}")