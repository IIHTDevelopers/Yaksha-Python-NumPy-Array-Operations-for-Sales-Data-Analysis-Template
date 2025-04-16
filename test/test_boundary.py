import unittest
import numpy as np
from mainclass import SalesAnalysis
from test.TestUtils import TestUtils

class BoundaryTests(unittest.TestCase):
    def test_single_product_sales(self):
        """Test with only one data point for each product."""
        single_data = SalesAnalysis([50], [30])
        obj_max = single_data.find_max()
        obj_min = single_data.find_min()
        obj_sum = single_data.find_sum()
        expected_max = 50
        expected_min = 30
        expected_sum = 80
        test_obj = TestUtils()
        if obj_max == expected_max and obj_min == expected_min and obj_sum == expected_sum:
            test_obj.yakshaAssert("TestSingleProductSales", True, "boundary")
            print("TestSingleProductSales = Passed")
        else:
            test_obj.yakshaAssert("TestSingleProductSales", False, "boundary")
            print("TestSingleProductSales = Failed")

    def test_large_data_set(self):
        """Test with a very large data set."""
        large_data = SalesAnalysis([i for i in range(1, 100001)], [i for i in range(100001, 200001)])
        try:
            obj_max = large_data.find_max()
            obj_min = large_data.find_min()
            obj_sum = large_data.find_sum()
            if not obj_max:
                test_obj.yakshaAssert("TestLargeDataSet", False, "boundary")
                print("TestLargeDataSet = Failed")
                return
            test_obj = TestUtils()
            test_obj.yakshaAssert("TestLargeDataSet", True, "boundary")
            print("TestLargeDataSet = Passed")
        except:
            test_obj = TestUtils()
            test_obj.yakshaAssert("TestLargeDataSet", False, "boundary")
            print("TestLargeDataSet = Failed")
