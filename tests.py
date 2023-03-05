import unittest
from check_pwd import check_pwd


class TestCase(unittest.TestCase):
    # Test 1 checks to see if password less than 8 characters returns False
    def test1(self):
        self.assertFalse(check_pwd("1234567"))

    # Test 2 checks to see if password more than 20 characters returns False
    def test2(self):
        self.assertFalse(check_pwd("123456789123456789123"))

    # Test 3 checks to see if password at correct length but with all digits 
    # returns False
    def test3(self):
        self.assertFalse(check_pwd("123456789"))

    # Test 4 checks to see if password at correct length but with all lowercase
    def test4(self):
        self.assertFalse(check_pwd("abcdefghi"))
if __name__ == '__main__':
    unittest.main()