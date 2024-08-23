# These are some of the unit tests that I wrote to test my part of the group project, which was to
# write a function that converts the number of seconds since the epoch of Jan 1, 1970 given as an
# input into a string of the format MM-DD-YYYY without using any libraries that convert seconds
# to a date. The function I wrote myself is considered confidential and cannot be shown in public, but
# my experience with this project can be seen in the Hwang_Louis_report.pdf file.

# Function 2 tests
import unittest
#from task import my_datetime


class FunctionTests(unittest.TestCase):
    def test1_func2(self):
        """This is the first test listed on Canvas"""
        self.assertEqual(my_datetime(0), "01-01-1970")

    def test2_func2(self):
        """This is the second test listed on Canvas"""
        self.assertEqual(my_datetime(123456789), "11-29-1973")

    def test3_func2(self):
        """This is the third test listed on Canvas"""
        self.assertEqual(my_datetime(9876543210), "12-22-2282")

    def test4_func2(self):
        """This is the fourth test listed on Canvas"""
        self.assertEqual(my_datetime(201653971200), "02-29-8360")

    def test5_func2(self):
        """Tests to see if an edge case of 1 doesn't change the date"""
        self.assertEqual(my_datetime(1), "01-01-1970")

    def test6_func2(self):
        """Tests to see if an edge case of 86400 advances day by 1"""
        self.assertEqual(my_datetime(86400), "01-02-1970")

    def test7_func2(self):
        """Tests to see if an edge case of 86399 doesn't advance day by 1"""
        self.assertEqual(my_datetime(86399), "01-01-1970")

    def test8_func2(self):
        """Tests to see if an edge case advances month by 1"""
        self.assertEqual(my_datetime(2678400), "02-01-1970")

    def test9_func2(self):
        """Tests to see if an edge case does not advance month by 1"""
        self.assertEqual(my_datetime(2678399), "01-31-1970")

    def test10_func2(self):
        """Tests to see if an edge case advances year by 1"""
        self.assertEqual(my_datetime(31536000), "01-01-1971")

    def test11_func2(self):
        """Tests to see if an edge case does not advance year by 1"""
        self.assertEqual(my_datetime(31535999), "12-31-1970")

    def test12_func2(self):
        """Tests to see if February 29 can be printed out"""
        self.assertEqual(my_datetime(68169600), "02-29-1972")

    def test13_func2(self):
        """Tests to see if day after February 29 can be printed out"""
        self.assertEqual(my_datetime(68256000), "03-01-1972")


#if __name__ == '__main__':
#    unittest.main()