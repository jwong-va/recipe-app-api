from django.test import SimpleTestCase

from app import calc

class CalcTests(SimpleTestCase):
    def test_add_numbers(self):
        print("running test_add_numbers")
        actualOutput = calc.add(5, 6)

        self.assertEqual(actualOutput, 11)


    def test_subtract_numbers(self):
        print("running test_subtract_numbers")
        actualOutput = calc.subtract(6, 5)

        self.assertEqual(actualOutput, 1);