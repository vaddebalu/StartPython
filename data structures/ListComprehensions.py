"""
Wriate a Python program to print squares from 1 to 100 using List comprehensions
"""
#without list comprehension
for num in range(100):
    print(num*num)

#with list comprehension
print("Using list comprehensions ....")
[print(num*num) for num in range(100)]