"""
This program helps you understand how to use iterator in Python
"""
#normal iteration of a list
names=['Balu',' Bala','Sai','Nirupam','Swamy']

#iteration using iter() class
nameslist=iter(names)
print(next(nameslist))
print(next(nameslist))
print(next(nameslist))
