import unittest
import sys, os
from composite import *

sys.path.append(os.getcwd())


class TestPartCost(unittest.TestCase):
    def test_part_cost_is_working(self):
        engine = ComplexPart('Engine')
        engine.add_product(Part('Cylinders', 100))
        engine.add_product(Part('Pistons', 120))
        self.assertEqual(engine.cost(), 220)

    def test_part_cost_receives_string_is_working(self):
        engine = ComplexPart('Engine')
        engine.add_product(Part('Cylinders', '100'))
        engine.add_product(Part('Pistons', '120'))
        self.assertIsInstance(engine.cost(), float)


if __name__ == '__main__':
    unittest.main()
