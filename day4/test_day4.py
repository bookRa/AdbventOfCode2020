import unittest
import os
from day4 import extra_valid, valid_passports


class Test(unittest.TestCase):
    cwd = os.getcwd()
    def test_passport(self):
        path = os.path.join(self.cwd, 'day4/smol.txt')
        assert(valid_passports(path) == 3)

    def test_xtra_invalid(self):
        path = os.path.join(self.cwd, 'day4/invalids.txt')
        assert(extra_valid(path) == 0)

    def test_xtra_valid(self):
        path = os.path.join(self.cwd, 'day4/valids.txt')
        assert(extra_valid(path) == 4)
    
    def test_answer(self):
        path = os.path.join(self.cwd, 'day4/input.txt')
        answer = extra_valid(path)
        print(f"found {answer} valid docs")
        assert(answer > 1)



if __name__ == '__main__':
    unittest.main()