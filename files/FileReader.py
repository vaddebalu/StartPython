"""
This program showas how to write a python program to read a file
"""
#reading line by line froma file in Python
sample=open('sample.txt','r')
for line in sample:
    print(line)
sample.close()
#reading char by char froma file in Python
sample1=open('sample.txt','r')
for char in sample1.read():
    print(char)