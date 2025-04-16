import unittest
from mainclass import SalesAnalysis
from test.TestUtils import TestUtils
import numpy as np

class ExceptionalTests(unittest.TestCase):
    def test_empty_data_max(self):
        """Test if ValueError is raised when the sales data is empty for max calculation."""
        test_obj = TestUtils()
        try:
            empty_data = SalesAnalysis([], [])
            empty_data.find_max()
            test_obj.yakshaAssert("TestEmptyDataMax", False, "exceptional")
            print("TestEmptyDataMax = Failed")
        except ValueError:
            test_obj.yakshaAssert("TestEmptyDataMax", True, "exceptional")
            print("TestEmptyDataMax = Passed")

    def test_empty_data_min(self):
        """Test if ValueError is raised when the sales data is empty for min calculation."""
        test_obj = TestUtils()
        try:
            empty_data = SalesAnalysis([], [])
            empty_data.find_min()
            test_obj.yakshaAssert("TestEmptyDataMin", False, "exceptional")
            print("TestEmptyDataMin = Failed")
        except ValueError:
            test_obj.yakshaAssert("TestEmptyDataMin", True, "exceptional")
            print("TestEmptyDataMin = Passed")

    def test_empty_data_sum(self):
        """Test if ValueError is raised when the sales data is empty for sum calculation."""
        test_obj = TestUtils()
        try:
            empty_data = SalesAnalysis([], [])
            empty_data.find_sum()
            test_obj.yakshaAssert("TestEmptyDataSum", False, "exceptional")
            print("TestEmptyDataSum = Failed")
        except ValueError:
            test_obj.yakshaAssert("TestEmptyDataSum", True, "exceptional")
            print("TestEmptyDataSum = Passed")
