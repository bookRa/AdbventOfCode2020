import unittest
from day2 import passwords_redux, valid_passwords


class Test(unittest.TestCase):
    testcase = """2-5 l: fllxf
4-5 r: rrrjmrrrrrrh
1-4 k: kkksk
7-8 k: tknsqknzkckrwkjkk
2-3 p: mpbstpxmsxmpnhbwlb
2-7 j: xkjjtjjjj"""

    def test_valid_passwords(self):
        """
        just tests the password function
        """
        input = self.testcase.splitlines()
        expected = [
            "2-5 l: fllxf",
            "1-4 k: kkksk",
            "7-8 k: tknsqknzkckrwkjkk",
            "2-3 p: mpbstpxmsxmpnhbwlb",
            "2-7 j: xkjjtjjjj"
             ]
        self.assertCountEqual(valid_passwords(input), expected)

    def test_passwords_redux(self):
        input = self.testcase.splitlines()
        expected = [
            "2-5 l: fllxf",
            "1-4 k: kkksk",
            "2-3 p: mpbstpxmsxmpnhbwlb",
            "2-7 j: xkjjtjjjj"
        ]
        self.assertCountEqual(passwords_redux(input), expected)

if __name__ == '__main__':
    unittest.main()