from abc import ABC, abstractmethod
from serviceable import serviceable 
from battery import Battery 


class Car(ABC, serviceable):
    def __init__(self, last_service_date):
        self.last_service_date = last_service_date

    @abstractmethod
    def needs_service(self):
        pass
