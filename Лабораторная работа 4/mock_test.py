import unittest
import sys, os
from unittest.mock import patch, Mock

import composite

sys.path.append(os.getcwd())
from composite import *


class TestComposite(unittest.TestCase):
    @patch.object(composite.Car, 'cost')
    def test_car_cost(self, mock_cost):
        mock_cost.return_value = "100"
        SUV = Car("SUV")
        self.assertEqual(SUV.cost(), "100")
