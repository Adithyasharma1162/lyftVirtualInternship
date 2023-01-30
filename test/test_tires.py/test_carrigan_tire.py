import unittest
from tire.carrigan_tire import CarriganTires

class TestCarriganTire(unittest.TestCase):
    def test_carrigan_tire_true(self):
        array_produced = [0.3,0.9,0,0.8]
        tires = CarriganTires(array_produced)
        self.assertTrue(tires.needs_service())
    
    def test_carrigan_tire_false(self):
        array_produced = [0.7,0.8,0.1,0.89]
        tires = CarriganTires(array_produced)
        self.assertFalse(tires.needs_service())
        