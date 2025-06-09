'''
Write a python script to display the current date and time. First create variables to
store date and time, then display date and time in proper format (like: 13-8-2022 and
9:00 PM)
'''

#importing the datetime module
from datetime import datetime

#getting current date and time of the system
current_date_time = datetime.today()

#printing the date and time using the date time format codes
print(current_date_time.strftime('%d-%m-%Y %I:%M %p'))

#second method using f-string
print(f"{current_date_time:%d-%m-%Y %I:%M %p}")