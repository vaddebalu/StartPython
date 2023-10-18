"""
This python program demonstrates how to use arguments and keyword arguments in functions.
Arguments and keyword arguments are optional arguments for any funtion in Python.
"""
def argsKWargsDemo(name,*args,**kwargs):
    print("Hi ",name)
    if args:
        print("\n",args)
    if kwargs:
        print("\n",kwargs)
# Python function called without arguments and keyword arguments
argsKWargsDemo("Balu")

# Python function called with arguments and keyword arguments
argsKWargsDemo("Balu","Good Morning","1:How are you?")
