from datetime import datetime

from abc import ABC, abstractmethod

from serv_interface import Serviceable
from engines import Willoughby_E, Sternman_E, Capulet_E
from batteries import Spindler_B, Nubbin_B
"""
from engine.model.calliope import Calliope

from engine.model.glissade import Glissade
from engine.model.palindrome import Palindrome
from engine.model.rorschach import Rorschach
from engine.model.thovex import Thovex
"""

""""
class Car(ABC):
    def __init__(self, last_service_date):
        self.last_service_date = last_service_date

    @abstractmethod
    def needs_service(self):
        pass
"""



"""x = CarFactory.create_something(something, something, something)"""


"""make a service check method for each engine and put in the ints. Then make a battery service check thing and put in all the data there."""


class CarFactory():
    def create_calliope(current_date, last_service_date, current_mileage, last_service_mileage, tire_array):
        car_engine = Capulet_E(last_service_mileage, current_mileage)
        car_battery = Spindler_B(last_service_date, current_date)
        newCar = Car(car_battery, car_engine)
        return newCar

    def create_glissade(current_date, last_service_date, current_mileage, last_service_mileage):
        car_engine = Willoughby_E(last_service_mileage, current_mileage)
        car_battery = Spindler_B(last_service_date, current_date)
        newCar = Car(car_battery, car_engine)
        return newCar

    def create_palindrome(current_date, last_service_date, warning_light_on):
        newCar = Car(current_date, last_service_date, warning_light_on)
        car_engine = Sternman_E(warning_light_on)
        car_battery = Spindler_B(last_service_date, current_date)
        newCar = Car(car_battery, car_engine)
        return newCar

    def create_rorschach(current_date, last_service_date, current_mileage, last_service_mileage):
        car_engine = Willoughby_E(last_service_mileage, current_mileage)
        car_battery = Nubbin_B(last_service_date, current_date)
        newCar = Car(car_battery, car_engine)
        return newCar
      
    def create_thovex(current_date, last_service_date, current_mileage, last_service_mileage):
        car_engine = Capulet_E(last_service_mileage, current_mileage)
        car_battery = Nubbin_B(last_service_date, current_date)
        newCar = Car(car_battery, car_engine)
        return newCar


class Car(Serviceable):
    def __init__(self, engine, batter, last_serv_date):
        Car_Engine = engine 
        Car_Batt = batter
        last_service_date = last_serv_date
    def needs_service(self):
        if Car.Car_Batt.needs_service() == True or Car.Car_Engine.needs_service() == True:
            return True
        else:
            return False
