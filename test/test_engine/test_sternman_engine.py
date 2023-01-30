import unittest

from engine.sternman_engine import SternmanEngine

class TestSternmanEngine(unittest.TestCase):
    def test_needs_service_true(self):
        warning_light_is_on = True
        Engine = SternmanEngine(warning_light_is_on)
        self.assertTrue(Engine.needs_service())
    
    def test_needs_service_false(self):
        warning_light_is_on = True
        Engine = SternmanEngine(warning_light_is_on)
        self.assertFalse(Engine.needs_service())