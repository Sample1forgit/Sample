import unittest
from app import add, subtract

class TestAppFunctions(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(3, 5), 8)  # Test if add(3, 5) returns 8
        self.assertEqual(add(-1, 1), 0) # Test if add(-1, 1) returns 0

    def test_subtract(self):
        self.assertEqual(subtract(10, 5), 5) # Test if subtract(10, 5) returns 5
        self.assertEqual(subtract(0, 0), 0)  # Test if subtract(0, 0) returns 0

if __name__ == "__main__":
    unittest.main()
