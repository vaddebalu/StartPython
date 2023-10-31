"""
This program demonstrates features of The list in Python programming language
Lists are mutable,ordered collection and heterogeneous.
"""

fruits=['apple','orange','mango','grape',10,True]

#Indexing
#print first element using forward indexing
print(fruits[0])

#print first element using backward indexing
print(fruits[-1])

fruits[1]='Custard apple'
print(fruits)

#concatenation of lists

otherfruits=['Ice apple','Pomegranate','water melon']

allfruits=fruits+otherfruits

print(allfruits)

#Slicing

#print first 3 fruit names
print(allfruits[:3])

#print last 3 fruit names
print(allfruits[-3:])

#Shrinking
#delete last element
del allfruits[-1:]
print(allfruits)

allfruits.pop()
print(allfruits)
#List methods

#append
allfruits.append('pomegranate')
print(allfruits)

#sort
#allfruits.sort()
print(allfruits)
#reverse
allfruits.reverse()
print(allfruits)
#Index
print(allfruits.index('apple'))