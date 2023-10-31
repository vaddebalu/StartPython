"""
This program demonstrates the use of raise statement in python programming language
"""
result=0

try:
    #result=10/0
    raise ZeroDivisionError
except ZeroDivisionError:
    print("Zero division error raised and handled")