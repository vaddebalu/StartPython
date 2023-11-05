"""
A Python program to demonstrate super class and subclass relationship.
"""
#sub class Car extends vehicle class
from Vehicle import Vehicle
class Car(Vehicle):
    def wheels(self):
        return 4
if(__name__=='__main__'):
    alto=Car('Alto')
    wheels=alto.wheels()
    print(alto.name,' has ',wheels,' wheels')
