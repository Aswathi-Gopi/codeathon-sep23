import unittest
from test import find_max_profit

class TestFindMaxProfit(unittest.TestCase):
    
    def test_empty_list(self):
        input_list = []
        expected_output = -1
        self.assertEqual(find_max_profit(input_list), expected_output)
        
    def test_single_price(self):
        input_list = [10]
        expected_output = -1
        self.assertEqual(find_max_profit(input_list), expected_output)
        
    def test_no_profit(self):
        input_list = [10, 9, 8, 7, 6, 5]
        expected_output = -1
        self.assertEqual(find_max_profit(input_list), expected_output)
        
    def test_max_profit(self):
        input_list = [10, 20, 30, 40, 695, 50, 60]
        expected_output = (4, 40, 6, 60, 20)
        self.assertEqual(find_max_profit(input_list), expected_output)
        
    def test_duplicate_prices(self):
        input_list = [10, 20, 30, 40, 40, 50, 60]
        expected_output = (0, 10, 6, 60, 50)
        self.assertEqual(find_max_profit(input_list), expected_output)
        
if __name__ == '__main__':
    unittest.main()
