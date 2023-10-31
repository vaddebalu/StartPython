"""
This program demonstrates the use of finally statement in Exception handling in Python
Finally statements gets executed by default irrespective of an error has occured or not
"""
import traceback
result=0
try:
    result=10/0
except TypeError:
    print("Type error occured")
except NameError:
    print("Name Error occured")
#except ZeroDivisionError:
 # print("Zero division error occured")
finally:
    print("This runs everytime",traceback.print_exc())
print("Exception handled")