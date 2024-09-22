import unittest
from main import _calculate_deposit, Deposit

from datetime import datetime


test_deposit = Deposit(date='31.01.2021', periods=3, amount=10000, rate=6)
start_date = datetime.strptime(test_deposit.date, "%d.%m.%Y")
expected_result = {
    "31.01.2021": 10050,
    "28.02.2021": 10100.25,
    "31.03.2021": 10150.75
}


class TestCalculate(unittest.TestCase):
    def test_calculate_amount(self):

        res = _calculate_deposit(test_deposit, start_date)
        self.assertEqual(type(res), dict)
        self.assertEqual(res, expected_result)
