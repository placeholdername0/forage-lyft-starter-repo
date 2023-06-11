from serv_interface import Serviceable
from abc import ABC, abstractmethod
from datetime import datetime

class Battery(Serviceable, ABC):
    @abstractmethod
    def needs_service(self):
        pass

class Spindler_B(Battery):
    def __init__(self, last_serv_d, curr_date):
        last_service_date = last_serv_d 
        current_date = curr_date
    def needs_service(self):
        service_threshold_date = self.last_service_date.replace(year=self.last_service_date.year + 2)
        if service_threshold_date < datetime.today().date():
            return True
        else:
            return False
        
class Nubbin_B(Battery):
    def __init__(self, last_serv_d, curr_date):
        last_service_date = last_serv_d 
        current_date = curr_date
    def needs_service(self):
        service_threshold_date = self.last_service_date.replace(year=self.last_service_date.year + 4)
        if service_threshold_date < datetime.today().date():
            return True
        else:
            return False
        
