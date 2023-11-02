"""
How to write to a file in Python programming language
"""
import os
sample=open('sample.txt','w')
emp=['Balu','100','Hyderabad']
for e in emp:
    sample.write(e)
    sample.write('\n')
sample.close()

sample=open('sample.txt','a')
for e in emp:
    sample.write(e)
    sample.write('\n')
sample.close()
