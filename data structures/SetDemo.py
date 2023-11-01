"""
This program demonstrates features of The list in Python programming language
Sets are mutable,ordered collection and heterogeneous.
"""

fruits=set(['apple','orange','mango','grape',10,True])
print(type(fruits))
print(fruits)

#add new element
fruits.add('11')
print(fruits)

#membership
print(10 in fruits)

#union
newfruits=set(['11','water melon'])
allfruits=fruits|newfruits
print(allfruits)

#intersection
commonfruits=newfruits&fruits
print(commonfruits)

#difference
onlyfruits=fruits^newfruits
print(onlyfruits)

fruits.remove(10)
print(fruits)


