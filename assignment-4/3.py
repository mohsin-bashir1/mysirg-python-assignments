'''Write a python script which takes two numbers from the user, then calculate their sum and display the result'''

print("Enter two numbers: ")
n1, n2 = int(input()), int(input())

sum = n1 + n2
print(f"sum of {n1} and {n2} is {sum}")

print("sum of %d and %d is %d" % (n1, n2, sum))

print("sum of {} and {} is {}".format(n1, n2, sum))