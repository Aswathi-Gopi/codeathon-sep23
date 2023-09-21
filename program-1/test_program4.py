import unittest
from test import sort_array

class TestSortArray(unittest.TestCase):
    
    def test_empty_array(self):
        input_array = []
        expected_output = []
        self.assertEqual(sort_array(input_array), expected_output)
        
    def test_single_element_array(self):
        input_array = [10]
        expected_output = [10]
        self.assertEqual(sort_array(input_array), expected_output)
        
    def test_sorted_array(self):
        input_array = [10, 20, 30, 40, 50]
        expected_output = [10, 20, 30, 40, 50]
        self.assertEqual(sort_array(input_array), expected_output)
        
    def test_unsorted_array(self):
        input_array = [50, 40, 30, 20, 10]
        expected_output = [10, 20, 30, 40, 50]
        self.assertEqual(sort_array(input_array), expected_output)
        
    def test_duplicate_elements(self):
        input_array = [10, 20, 30, 20, 10]
        expected_output = [10, 10, 20, 20, 30]
        self.assertEqual(sort_array(input_array), expected_output)
        
if __name__ == '__main__':
    unittest.main()
