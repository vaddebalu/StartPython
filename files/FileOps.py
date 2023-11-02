"""
How to perform common file operations using Python programming language
"""
import os
pwd=os.getcwd()
print('current os directory is ...',pwd)
print('List current directory ... ')
for files in os.listdir():
    print(files)
print('create a new directory in the current folder ...')
os.mkdir('test')