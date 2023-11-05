"""
A Python program to demonstrate super class and subclass relationship.
"""
from Vehicle import Vehicle
from TwoWheeler import TwoWheeler
#subclass for vehicle class and TwoWheeler class
class BiCycle(TwoWheeler,Vehicle):
    def wheels(self):
        return 2
    def transportType(self):
        return 'Slow Transport'
if(__name__=='__main__'):
    Bi=BiCycle('Atlas')
    whls=Bi.wheels()
    type=Bi.transportType()
    print(Bi.name,'has',whls,' wheels and It is Used for ',type)
