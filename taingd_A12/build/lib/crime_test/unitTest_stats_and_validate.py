import unittest
import pandas as pd
from stats_function import mean_age, median_age
from validate_functions import validate_sex_and_age

class TestStatsFunction(unittest.TestCase):
    def setUp(self):
        valid_data = {
            'Vict Sex': ['M', 'F', 'M', 'F', 'M', 'F'], 
            'Vict Age': [20, 30, 40, 50, 60, 70]
        }
        self.valid_df = pd.DataFrame(valid_data)

        invalid_data = {
            'Vict Sex': ['M', 'F', 'M', 'F', 'M', 10], 
            'Vict Age': [20, 30, 40, 50, 60, 70]
        }
        self.invalid_df = pd.DataFrame(invalid_data)

        edge_case_data = {
            'Vict Sex': ['M', 'F', 'M', 'F', 'M'], 
            'Vict Age': [2, 100, 100, 99, -1]
        }
        self.edge_case_df = pd.DataFrame(edge_case_data)

    def test_mean_age(self):
        self.assertEqual(mean_age(self.valid_df), 45) # test for valid return
        self.assertEqual(mean_age(self.edge_case_df), 60) # test edge case (negative age)

    def test_median_age(self):
        self.assertEqual(median_age(self.valid_df), 45) # test for valid return (plus test even number of elements)
        self.assertEqual(median_age(self.edge_case_df), 99) # test edge case (negative age)

    def test_validation(self):
        self.assertEqual(validate_sex_and_age(self.valid_df), 'Data is valid') # valid data
        self.assertEqual(validate_sex_and_age(self.invalid_df), 'Data is invalid') # invalid data (wrong data type)
        self.assertEqual(validate_sex_and_age(self.edge_case_df), 'Data is invalid') # invalid data (negative age)

if __name__ == '__main__':
    unittest.main()