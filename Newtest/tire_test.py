import unittest
import numpy as nump
from refactor.tires import Carrigan, Octoprime


class TestCarrigan(unittest.TestCase):
    def test_tire_should_be_serviced(self):
        sensor_nums = nump.array([0.1, 0.3, 0.9, 0.5])
        tiretest = Carrigan(sensor_nums)
        self.assertTrue(tiretest.needs_service())

    def test_tire_should_not_be_serviced(self):
        sensor_nums = nump.array([0.1, 0.3, 0.4, 0.5])
        tiretest = Carrigan(sensor_nums)
        self.assertFalse(tiretest.needs_service())

class TestOctoprime(unittest.TestCase):
    def test_tire_should_be_serviced(self):
        sensor_nums = nump.array([1.0, 0.5, 0.8 1.0])
        tiretest = Octoprime(sensor_nums)
        self.assertTrue(tiretest.needs_service())

    def test_tire_should_not_be_serviced(self):
        sensor_nums = nump.array([0.1, 0.3, 0.4, 0.5])
        tiretest = Octoprime(sensor_nums)
        self.assertFalse(tiretest.needs_service()) 

        