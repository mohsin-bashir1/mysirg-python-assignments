#Write a command to get the Python version you are using.

#python -V
#or python --version
#or python3 --version
#or python3 -V

import platform
from sys import version
print('Current python version ', platform.python_version()) 
print('Current python version ', version)