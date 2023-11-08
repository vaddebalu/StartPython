"""
This program explains how to use generators in Python
"""
#default iteration of numbers on a list

nums=[1,2,3,4,5]
for num in nums:
    print(num*num)

#using generator
def square(num):
    for i in range(1,num+1):
        yield(i*i)
squares=square(5)
print("next square is : ",next(squares))
print("next square is : ",next(squares))
print("next square is : ",next(squares))

#using iterator
nums=iter(range(1,5))
nextnum1=next(nums)
nextnum2=next(nums)
nextnum3=next(nums)
print(nextnum1*nextnum1)
print(nextnum2*nextnum2)
print(nextnum3*nextnum3)
