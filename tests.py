import unittest
from check_pwd import check_pwd


class TestCase(unittest.TestCase):
    # Test 1 checks to see if password less than 8 characters returns False
    def test1(self):
        self.assertFalse(check_pwd("1234567"))

if __name__ == '__main__':
    unittest.main()