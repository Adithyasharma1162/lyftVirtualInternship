import unittest
from tire.octoprime_tire import OctoprimeTire

class TestOctoprimeTire(unittest.TestCase):
    def test_octoprime_tire_true(self):
        array_produced = [1,0.4,0.9,0.7]
        tire = OctoprimeTire(array_produced)
        self.assertTrue(tire.needs_service())
    
    def test_octoprime_tire_false(self):
        array_produced = [1,0.4,0.9,0]
        tire = OctoprimeTire(array_produced)
        self.assertFalse(tire.needs_service())
        