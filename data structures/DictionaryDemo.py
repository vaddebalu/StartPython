"""
This program demonstrates features of  Dictionary in Python programming language
Lists are mutable,ordered collection and heterogeneous.
"""

fruits={'apple':1,'orange':2,'mango':3,'grape':4}

#copy a dictionary
myfruits=fruits.copy()

#indexing
print(myfruits['apple'])
#adding
fruits['Ice Apple']=5
print(fruits)

#deleting
del fruits['apple']
print(fruits)

#print keys
print(fruits.keys())

#print values
print(fruits.values())

#merging
newfruits={'watermelon':6,'musk melon':7}
fruits.update(newfruits)

print(fruits)

#has key

print('watermelon' in fruits)