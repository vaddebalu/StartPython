"""
This program demonstrates features of The Tuple in Python programming language

Tuples are immutable,ordered collection and heterogeneous and read only
"""

fruits=('apple','orange','mango','grape',100,False)

#Indexing
#print first element using forward indexing
print(fruits[0])

#print first element using backward indexing
print(fruits[-1])

#concatenation of lists



#Slicing

#print first 3 fruit names
print(fruits[:3])

#print last 3 fruit names
print(fruits[-3:])

#sort
fruits=list(fruits)
fruits.sort()
print(fruits)
#reverse
fruits.reverse()
print(fruits)
#Index
print(fruits.index('apple'))