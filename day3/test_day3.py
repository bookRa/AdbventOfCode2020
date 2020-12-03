import unittest
from day3 import toboggan_1


class Test(unittest.TestCase):
    testcase = """.#..
.#..
..#.
....
#..."""

    def test_toboggan_1(self):
        input = self.testcase.splitlines()
        self.assertEquals(toboggan_1(1,1,input), 3)


if __name__ == '__main__':
    unittest.main()