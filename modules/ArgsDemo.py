""""
Python program to demonstrate how to use modules
"""
#use from and import statement to import only argv from sys
from sys import argv
print('run with command line arguements . . .')
num=argv[1]
for i in range(int(num)):
    print(i)
