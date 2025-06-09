'''
Create four variables in a Python script and assign values of different data types to
them. Write a Python script to print value, its type and id of each variable
'''

employeeId = 1261
employeeName = "Mohsin Bashir Najar"
employeeSalary = 19689.45
isMale = True

print(f"Value of Employee Id is {employeeId}, its id is {id(employeeId)}, its type is {type(employeeId)}")

print(f"Value of Employee Name {employeeName}, its id is {id(employeeName)}, its type is {type(employeeName)}")

print(f"Value of Employee Salary {employeeSalary}, its id is {id(employeeSalary)}, its type is {type(employeeSalary)}")

print(f"Value of isMale is {isMale}, its id is {id(isMale)}, its type is {type(isMale)}")