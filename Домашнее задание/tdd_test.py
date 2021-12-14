import unittest
import sys, os

sys.path.append(os.getcwd())
from app.handlers.cars import *


class TestBot(unittest.TestCase):
    def test_1(self):
        pass
        self.assertEqual(car_check("внедорожник"), 0)
        self.assertEqual(car_check("Машина"), 1)

    def test_2(self):
        pass
        self.assertEqual(equipment_check("минимальная"), 0)
        self.assertEqual(equipment_check("самая полная"), 1)
