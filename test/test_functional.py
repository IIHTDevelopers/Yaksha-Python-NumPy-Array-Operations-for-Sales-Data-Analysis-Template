import unittest
import numpy as np
from mainclass import SalesAnalysis
from test.TestUtils import TestUtils



class FunctionalTests(unittest.TestCase):
    def setUp(self):
        """Set up test data"""
        self.product1_sales = [50, 30, 20, 40, 10]
        self.product2_sales = [30, 50, 40, 10, 60]
        self.sales_analysis = SalesAnalysis(self.product1_sales, self.product2_sales)

    def test_find_max(self):
        """Test if the maximum sales value is calculated correctly."""
        obj = self.sales_analysis.find_max()
        expected_max = 60
        test_obj = TestUtils()
        if obj == expected_max:
            test_obj.yakshaAssert("TestFindMax", True, "functional")
            print("TestFindMax = Passed")
        else:
            test_obj.yakshaAssert("TestFindMax", False, "functional")
            print("TestFindMax = Failed")

    def test_find_min(self):
        """Test if the minimum sales value is calculated correctly."""
        obj = self.sales_analysis.find_min()
        expected_min = 10
        test_obj = TestUtils()
        if obj == expected_min:
            test_obj.yakshaAssert("TestFindMin", True, "functional")
            print("TestFindMin = Passed")
        else:
            test_obj.yakshaAssert("TestFindMin", False, "functional")
            print("TestFindMin = Failed")

    def test_find_sum(self):
        """Test if the sum of all sales is calculated correctly."""
        obj = self.sales_analysis.find_sum()
        expected_sum = 340
        test_obj = TestUtils()
        if obj == expected_sum:
            test_obj.yakshaAssert("TestFindSum", True, "functional")
            print("TestFindSum = Passed")
        else:
            test_obj.yakshaAssert("TestFindSum", False, "functional")
            print("TestFindSum = Failed")