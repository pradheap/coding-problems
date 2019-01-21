import unittest

from array_best_time_to_buy_sell_stock.source import buy_and_sell


class TestBuyAndSellStock(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(buy_and_sell([]), 0)
    
    def test_with_6_elements(self):
        self.assertEqual(buy_and_sell([7, 1, 5, 3, 6, 4]), 5)
    
    def test_with_first_and_last_elements(self):
        self.assertEqual(buy_and_sell([1, 7, 4, 11]), 10)

    def test_with_no_profit(self):
        self.assertEqual(buy_and_sell([11, 7, 4, 1]), 0)
    
    def test_with_no_profit(self):
        self.assertEqual(buy_and_sell([121]), 0)
