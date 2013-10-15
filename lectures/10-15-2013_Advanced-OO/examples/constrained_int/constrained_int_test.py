import unittest

from constrained_int import ConstrainedInt

class TestConstrainedInt(unittest.TestCase):

    def test_constrainedint(self):
        x = ConstrainedInt(10)
        self.assertEqual(x, 10)

    def test_constrainedint_mods_correctly(self):
        x = ConstrainedInt(256)
        self.assertEqual(x, 1)

    def test_constrainedint_handles_addtion(self):
        x = ConstrainedInt(10)
        x += 246
        self.assertEqual(x,1)
 
    def test_constrainedint_handles_subtraction(self):
        x = ConstrainedInt(10)
        x -= 11
        self.assertEqual(x,254)
