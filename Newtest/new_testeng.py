import unittest
from refactor.batteries import Spindler_B, Nubbin_B
from refactor.engines import Willoughby_E, Sternman_E, Capulet_E
from datetime import datetime


class TestCapulet_E(unittest.TestCase):
    def test_engine_needs_service(self):
        current_mileage = 30001
        last_service_mileage = 0
        eng = Capulet_E(last_service_mileage, current_mileage)
        self.assertTrue(eng.needs_service())

    def test_engine_not_need_service(self):
       current_mileage = 30000
       last_service_mileage = 0
       eng = Capulet_E(last_service_mileage, current_mileage)
       self.assertFalse(eng.needs_service())

class TestWilloughby_E(unittest.TestCase):
    def test_engine_needs_service(self):
        current_mileage = 60001
        last_service_mileage = 0
        eng = Willoughby_E(last_service_mileage, current_mileage)
        self.assertTrue(eng.needs_service())

    def test_engine_not_need_service(self):
        current_mileage = 60000
        last_service_mileage = 0
        eng = Willoughby_E(last_service_mileage, current_mileage)
        self.assertFalse(eng.needs_service())

class TestSternman_E(unittest.TestCase):
    def test_engine_needs_service(self):
        last_service_date = datetime.today().date()
        warning_light_is_on = True
        eng = Sternman_E(warning_light_is_on)
        self.assertTrue(eng.needs_service())

    def test_engine_not_need_service(self):
        warning_light_is_on = False
        eng = Sternman_E(warning_light_is_on)
        self.assertFalse(eng.needs_service())


