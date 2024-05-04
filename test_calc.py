import unittest
import calc 

class TestCalc(unittest.TestCase):
    def test_calc(self):
        result = calc.add(10,5)
        self.assertEqual(result,15)

if __name__ == '__main__':
    unittest.main() # to enable us run python test_calc.py directly
    