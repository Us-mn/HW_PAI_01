import unittest
from csv_processor import get_average_score

class TestCSVLab(unittest.TestCase):

    def test_average(self):
        # Numeric scores are 85, 42, 95, 60. Average = 70.5
        result = get_average_score('data.csv')
        self.assertAlmostEqual(result, 70.5, places=1, msg="The average score is incorrect. Did you skip the 'invalid' row?")

    def test_return_type(self):
        result = get_average_score('data.csv')
        self.assertIsInstance(result, float, "The function should return a float.")

if __name__ == '__main__':
    unittest.main()
