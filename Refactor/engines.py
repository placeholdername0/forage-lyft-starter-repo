from serv_interface import Serviceable
from abc import ABC, abstractmethod

class Engine(Serviceable, ABC):
    @abstractmethod
    def needs_service(self):
        pass

class Capulet_E(Engine):
    def __init__(self, last_serv_m, current_mileage):
        last_service_mileage = last_serv_m
        curr_m = current_mileage
    def needs_service(self):
        return self.curr_m - self.last_service_mileage > 30000
    
class Willoughby_E(Engine):
    def __init__(self, last_serv_m, current_mileage):
        last_service_mileage = last_serv_m
        curr_m = current_mileage
    def needs_service(self):
        return self.curr_m - self.last_service_mileage > 60000

class Sternman_E(Engine):
    def __init__(self, curr_warn_light):
        warning_light_on = curr_warn_light
    def needs_service(self):
        if self.warning_light_on:
            return True
        else:
            return False
        


