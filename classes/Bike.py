"""
A Python program to demonstrate super class and subclass relationship.
"""
from Vehicle import Vehicle
#sub class Bike extends vehicle class

class Bike(Vehicle):
    def wheels(self):
        return 2
if(__name__=='__main__'):
    bike=Bike(' Hero Pleasure')
    whls=bike.wheels()
    print(bike.name,' has ',whls,' wheeels')
