from abc import ABC
from car import Car 

class Serviceable(Car, ABC):
    def __init__(self, last_service_date, current_mileage, last_service_mileage, mileage_limit):
        super().__init__(last_service_date)
        self.current_mileage = current_mileage
        self.last_service_mileage = last_service_mileage
        self.mileage_limit = mileage_limit

    def needs_service(self):
        return self.current_mileage - self.last_service_mileage > self.mileage_limit