import unittest
from Func.Calc import Calc


class TestCalc(unittest.TestCase):
    def setUp(self):
        print("setUp")

    def tearDown(self):
        print("teardown")

    def test_calc_add(self):
        res = Calc().add(3, 5)
        print("add:", res)

    def test_calc_sub(self):
        res = Calc().sub(3, 6)
        print("sub:", res)


if __name__ == '__main__':
    unittest.main()
