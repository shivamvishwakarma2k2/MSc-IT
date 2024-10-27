import unittest
from main import to_upper

class TestClass(unittest.TestCase):
    def test_to_upper(self):
        name = 'shivam'
        up = to_upper(name)
        self.assertEqual(up, 'SHIVAM')

if __name__ == "__main__":
    unittest.main()