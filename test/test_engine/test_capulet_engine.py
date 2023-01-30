import unittest

from engine.capulet_engine import CapuletEngine

class TestCapuletEngine(unittest.TestCase):
    def test_needs_service_true(self):
        current_mileage = 30001
        last_service_mileage = 0
        Engine = CapuletEngine(current_mileage= current_mileage,last_service_mileage= last_service_mileage)
        self.assertTrue(Engine.needs_service())
    
    def test_needs_service_false(self):
        current_mileage = 30000
        last_service_mileage = 0
        Engine = CapuletEngine(current_mileage=current_mileage,last_service_mileage=last_service_mileage)
        self.assertFalse(Engine.needs_service())