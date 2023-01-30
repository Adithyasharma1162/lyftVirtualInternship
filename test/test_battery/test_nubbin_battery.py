import unittest
from datetime import date
from battery.nubbin_battery import NubbinBattery

class TestNubbinBattery(unittest.TestCase):
    def test_service_needed_true(self):
        current_date = date.fromisoformat("2023-01-29")
        last_service_date = date.fromisoformat("2019-01-20")
        battery = NubbinBattery(current_date,last_service_date)
        self.assertTrue(battery.needs_service)
    
    def test_service_needed_false(self):
        current_date = date.fromisoformat("2023-01-29")
        last_service_date = date.fromisoformat("2019-06-29")
        battery = NubbinBattery(current_date,last_service_date)
        self.assertFalse(battery.needs_service)