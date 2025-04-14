import unittest
from calculator import *
# https://github.com/JosiahCaballero/-lab10--J.C---M.L-
# Partner 1: Maria Luiza C Nogueira
# Partner 2: Josiah Caballero

def multiply(param, param1):
    pass


class TestCalculator(unittest.TestCase):
    # Partner 2
    def test_add(self): # 3 assertions
          self.assertEqual(add(13, 7), 20)
          self.assertEqual(add(-5, 12), 7)
          self.assertEqual(add(0, 99), 99)

    def test_subtract(self): # 3 assertions
        self.assertEqual(sub(100, 45), 55)
        self.assertEqual(sub(-10, -3), -7)
        self.assertEqual(sub(9, 27), -18)
    ##########################

    # Partner 1
    def test_multiply(self): # 3 assertions
        self.assertEqual(multiply(5,5),25)
        self.assertEqual(multiply(5,10), 50)
        self.assertEqual(multiply(1,5),5)

    def test_divide(self): # 3 assertions
        self.assertEqual(div(5, 1), 5)
        self.assertEqual(div(50, 10), 5)
        self.assertEqual(div(10, 5), 2)

    # Partner 2
    def test_divide_by_zero(self): # 1 assertion
        # call division function inside, example:
        # with self.assertRaises(<INSERT_ERROR_TYPE>):
        #     div(0, 5)
        with self.assertRaises(ZeroDivisionError):
            div(42, 0)
        

    def test_logarithm(self): # 3 assertions
        self.assertAlmostEqual(log(4, 16), 2)
        self.assertAlmostEqual(log(3, 81), 4)
        self.assertAlmostEqual(log(2, 32), 5)

    def test_log_invalid_base(self): # 1 assertion
        # use same technique from test_divide_by_zero
        with self.assertRaises(ValueError):
            log(1, 50)
    ##########################
    
    # Partner 1
    def test_log_invalid_argument(self): # 1 assertion
        # call log function inside, example:
        # with self.assertRaises(<INSERT_ERROR_TYPE>):
        #     logarithm(0, 5)
        with self.assertRaises(ValueError):
            logarithm(10, 0)
        with self.assertRaises(ValueError):
            log(0,5)
        pass

    def test_hypotenuse(self):
        # 3 assertions
        self.assertEqual(hypotenuse(3,4),5)
        self.assertEqual(hypotenuse(5,12),13)
        self.assertAlmostEqual(hypotenuse(1.5,2.0),math.hypot(1.5,2.0),places=5)
        pass

    def test_sqrt(self): # 3 assertions
        # Test for invalid argument, example:
        # with self.assertRaises(<INSERT_ERROR_TYPE>):
        with self.assertRaises(ValueError):
            square_root(-9)
        #    square_root(NUM)
        self.assertEqual(square_root(16),4)
        # Test basic function
        self.assertAlmostEqual(square_root(2),math.sqrt(2),places=5)

    ##########################

# Do not touch this
if __name__ == "__main__":
    unittest.main()