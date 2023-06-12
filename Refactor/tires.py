from Refactor.serv_interface import Serviceable
from abc import ABC, abstractmethod


class Tire(ABC):
    @abstractmethod
    def needs_service(self):
        pass

class Carrigan(Tire):
    def __init__(self, num_array):
        tires_quality = num_array
    def needs_service(self):
        for num in self.tires_quality:
            if num >= 0.9:
                return True
            else:
                return False

class Octoprime(Tire):
    def __init__(self, num_array):
        tires_quality = num_array
    def needs_service(self):
        for num in self.tires_quality:
            sum += num
        if sum >= 3:
            return True
        else:
            return False