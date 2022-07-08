from abc import ABC

from car import Car 

class CarFactory: 
    def createModel(self):
        newCar = Car()
