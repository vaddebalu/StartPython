"""
A Python program to demonstrate super class and subclass relationship.
"""
from Vehicle import Vehicle
#subclass for vehicle class
class TwoWheeler(Vehicle):
    def wheels(self):
        return 2
    def transportType(self):
        return 'Speed'