import unittest
from datetime import date
from battery.spindler_battery import SpindlerBattery

class TestSpindlerBattery(unittest.TestCase):
    def test_service_needed_true(self):
        current_date = date.fromisoformat("2023-01-29")
        last_service_date = date.fromisoformat("2020-01-20")
        battery = SpindlerBattery(current_date,last_service_date)
        self.assertTrue(battery.needs_service)
    
    def test_service_needed_false(self):
        current_date = date.fromisoformat("2023-01-29")
        last_service_date = date.fromisoformat("2022-07-11")
        battery = SpindlerBattery(current_date,last_service_date)
        self.assertFalse(battery.needs_service)