"""
Write a program to demonstrate mutable data types (List and Dictionary) in python programming language
"""
empinfo=['Bala',101,200100.5]
def setEmpInfo(empList):
    empList[0]='Balu'
    empList[1]=100
    empList[2]=222333.5


setEmpInfo(empinfo)
print('Employee information is ...',empinfo)

empDict={'empname':'Bala','empno':101,'salary':200100.5}
def setEmpInfo(emp):
    emp['empname']='Balu'
    emp['empno']=100
    emp['salary']=222333.5


setEmpInfo(empDict)
print('Employee information is ...',empDict)
