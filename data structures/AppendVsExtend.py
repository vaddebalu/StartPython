fruits=['Apple','Orange','Mango']
print("Original List ...")
print(fruits)

print("append new element to the existing list ...")
fruits.append('grapes')
print(fruits)
print("adding new list to the existing list ...")
newfruits=['water melon','musk melon']
fruits.extend(newfruits)
print(fruits)
