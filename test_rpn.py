import unittest

import rpn

class TestBasics(unittest.TestCase):
    def test_add(self):
        result = rpn.calculate("1 1 +", 0)
        self.assertEqual(2, result)
    def test_subtract(self):
        result = rpn.calculate("5 3 -", 0)
        self.assertEqual(2, result)
    def test_multiply(self):
        result = rpn.calculate("5 3 *", 0)
        self.assertEqual(15, result)
    def test_divide(self):
        result = rpn.calculate("6 3 /", 0)
        self.assertEqual(2, result)
