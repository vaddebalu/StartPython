#This program demonstrates the use of exception handling in Python
"""
As we have used try and except blocks , execution flow continues
"""
result=0
try:
    result=10/0
except Exception:
    print(result)
print(" This line also gets displayed")
