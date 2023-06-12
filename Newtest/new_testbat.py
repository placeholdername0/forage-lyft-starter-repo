import unittest
from refactor.batteries import Spindler_B, Nubbin_B
from refactor.engines import Willoughby_E, Sternman_E, Capulet_E
from datetime import datetime

class TestSpindler_B(unittest.TestCase):
    def test_battery_needs_service(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 4)
        bat = Spindler_B(last_service_date, today)
        self.assertTrue(bat.needs_service())

    def test_battery_not_need_service(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)
        bat = Spindler_B(last_service_date, today)
        self.assertFalse(bat.needs_service())

class TestNubbin_B(unittest.TestCase):
    def test_battery_needs_service(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 5)
        bat = Spindler_B(last_service_date, today)
        self.assertTrue(bat.needs_service())
    def test_battery_not_need_service(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        bat = Spindler_B(last_service_date, today)
        self.assertFalse(bat.needs_service())



