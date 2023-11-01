"""
Write a program to demonstrate immutable data types (string,Int and float) in python programming language
"""
empname='Bala'
empno=101
salary=200100.5
def setEmpInfo(empname,empno,salary):
    print('Setting employee Information')
    empname='Balu'
    empno=100
    salary=234510.5

setEmpInfo(empname,empno,salary)
print('Employee information is ...',empname,empno,salary)
