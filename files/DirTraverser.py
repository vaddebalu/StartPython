"""
Python program to traverse a directory using Python code
"""
import os

for topdir,subdirs,files in os.walk('D:\\astro'):
    print('files ... ')
    for file in files:
        print(file)
    if(len(subdirs)>0):
        print('sub dirs ...',subdirs)