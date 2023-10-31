"""
This program demonstrates the use of else statement in Exception handling in Python
else statements gets executed only if no error is occured
"""

result=0
try:
    result=10/0
except TypeError:
    print("Arithmetic error occured")
except NameError:
    print("Name Error occured")
else:
    print("No error occured")