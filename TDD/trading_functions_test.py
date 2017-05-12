#!/usr/bin/env python

import sys, os
home_dir = os.path.expanduser('~')
home_dir += '/workspace/tk_trade_proj'
print home_dir
sys.path.append(home_dir)

import unittest
from trading_functions import *

class trading_functions_test_class(unittest.TestCase):

    def setUp(self):
        return

# SPREAD_COST TESTS
    def test_spread_same(self):
        buy_option = [113.34, 113.35, 100.0, 20161007.0, 2.0, 13.15, 13.15, 100, u'call', u'AAPL161007C00100000', u'None', 0.94869, 0.0118, -0.19908, 0.00713, 0.00335, 362.0]
        sell_option = [113.34, 113.35, 100.0, 20161007.0, 2.0, 13.15, 13.55, 100, u'call', u'AAPL161007C00100000', u'None', 0.94869, 0.0118, -0.19908, 0.00713, 0.00335, 362.0]
        result = spread_cost(sell_option, buy_option)
        self.assertAlmostEqual(result,0.0)

    def test_long_call_spread_low(self):
        buy_option = [113.34, 113.35, 100.0, 20161007.0, 2.0, 13.15, 13.55, 100, u'call', u'AAPL161007C00100000', u'None', 0.94869, 0.0118, -0.19908, 0.00713, 0.00335, 362.0]
        sell_option = [113.34, 113.35, 100.0, 20161007.0, 2.0, 13.15, 13.55, 100, u'call', u'AAPL161007C00100000', u'None', 0.94869, 0.0118, -0.19908, 0.00713, 0.00335, 362.0]
        result = spread_cost(sell_option, buy_option)
        self.assertAlmostEqual(result,-0.40)

    def test_long_call_spread_high(self):
        buy_option = [113.34, 113.35, 100.0, 20161007.0, 2.0, 13.15, 13.05, 100, u'call', u'AAPL161007C00100000', u'None', 0.94869, 0.0118, -0.19908, 0.00713, 0.00335, 362.0]
        sell_option = [113.34, 113.35, 100.0, 20161007.0, 2.0, 13.15, 13.55, 100, u'call', u'AAPL161007C00100000', u'None', 0.94869, 0.0118, -0.19908, 0.00713, 0.00335, 362.0]
        result = spread_cost(sell_option, buy_option)
        self.assertAlmostEqual(result,0.10)


# OPTIONS_HAVE_SAME_XDATE TESTS
    def test_2_options_have_same_xdate(self):
        option_1 = [113.34, 113.35, 100.0, 20161007.0, 2.0, 13.15, 13.55, 100, u'call', u'AAPL161007C00100000', u'None', 0.94869, 0.0118, -0.19908, 0.00713, 0.00335, 362.0]
        option_2 = [113.34, 113.35, 100.0, 20161007.0, 2.0, 13.15, 13.55, 100, u'call', u'AAPL161007C00100000', u'None', 0.94869, 0.0118, -0.19908, 0.00713, 0.00335, 362.0]
        result = options_have_same_xdate(option_1, option_2)
        self.assertEqual(result,True)

    def test_2_options_have_diff_xdate(self):
        option_1 = [113.34, 113.35, 100.0, 20161007.0, 2.0, 13.15, 13.55, 100, u'call', u'AAPL161007C00100000', u'None', 0.94869, 0.0118, -0.19908, 0.00713, 0.00335, 362.0]
        option_2 = [113.34, 113.35, 100.0, 20161008.0, 2.0, 13.15, 13.55, 100, u'call', u'AAPL161007C00100000', u'None', 0.94869, 0.0118, -0.19908, 0.00713, 0.00335, 362.0]
        result = options_have_same_xdate(option_1, option_2)
        self.assertEqual(result,False)

    def test_4_options_have_same_xdate(self):
        option_1 = [113.34, 113.35, 100.0, 20161008.0, 2.0, 13.15, 13.55, 100, u'call', u'AAPL161007C00100000', u'None', 0.94869, 0.0118, -0.19908, 0.00713, 0.00335, 362.0]
        option_2 = [113.34, 113.35, 100.0, 20161008.0, 2.0, 13.15, 13.55, 100, u'call', u'AAPL161007C00100000', u'None', 0.94869, 0.0118, -0.19908, 0.00713, 0.00335, 362.0]
        option_3 = [113.34, 113.35, 100.0, 20161008.0, 2.0, 13.15, 13.55, 100, u'call', u'AAPL161007C00100000', u'None', 0.94869, 0.0118, -0.19908, 0.00713, 0.00335, 362.0]
        option_4 = [113.34, 113.35, 100.0, 20161008.0, 2.0, 13.15, 13.55, 100, u'call', u'AAPL161007C00100000', u'None', 0.94869, 0.0118, -0.19908, 0.00713, 0.00335, 362.0]
        result = options_have_same_xdate(option_1, option_2, option_3, option_4)
        self.assertEqual(result,True)

    def test_4_options_have_diff_xdate_1(self):
        option_1 = [113.34, 113.35, 100.0, 20161007.0, 2.0, 13.15, 13.55, 100, u'call', u'AAPL161007C00100000', u'None', 0.94869, 0.0118, -0.19908, 0.00713, 0.00335, 362.0]
        option_2 = [113.34, 113.35, 100.0, 20161008.0, 2.0, 13.15, 13.55, 100, u'call', u'AAPL161007C00100000', u'None', 0.94869, 0.0118, -0.19908, 0.00713, 0.00335, 362.0]
        option_3 = [113.34, 113.35, 100.0, 20161007.0, 2.0, 13.15, 13.55, 100, u'call', u'AAPL161007C00100000', u'None', 0.94869, 0.0118, -0.19908, 0.00713, 0.00335, 362.0]
        option_4 = [113.34, 113.35, 100.0, 20161007.0, 2.0, 13.15, 13.55, 100, u'call', u'AAPL161007C00100000', u'None', 0.94869, 0.0118, -0.19908, 0.00713, 0.00335, 362.0]
        result = options_have_same_xdate(option_1, option_2, option_3, option_4)
        self.assertEqual(result,False)

    def test_4_options_have_diff_xdate_2(self):
        option_1 = [113.34, 113.35, 100.0, 20161007.0, 2.0, 13.15, 13.55, 100, u'call', u'AAPL161007C00100000', u'None', 0.94869, 0.0118, -0.19908, 0.00713, 0.00335, 362.0]
        option_2 = [113.34, 113.35, 100.0, 20161008.0, 2.0, 13.15, 13.55, 100, u'call', u'AAPL161007C00100000', u'None', 0.94869, 0.0118, -0.19908, 0.00713, 0.00335, 362.0]
        option_3 = [113.34, 113.35, 100.0, 20161007.0, 2.0, 13.15, 13.55, 100, u'call', u'AAPL161007C00100000', u'None', 0.94869, 0.0118, -0.19908, 0.00713, 0.00335, 362.0]
        option_4 = [113.34, 113.35, 100.0, 20161007.0, 2.0, 13.15, 13.55, 100, u'call', u'AAPL161007C00100000', u'None', 0.94869, 0.0118, -0.19908, 0.00713, 0.00335, 362.0]
        result = options_have_same_xdate(option_1, option_2, option_3, option_4)
        self.assertEqual(result,False)

    def test_4_options_have_diff_xdate_3(self):
        option_1 = [113.34, 113.35, 100.0, 20161007.0, 2.0, 13.15, 13.55, 100, u'call', u'AAPL161007C00100000', u'None', 0.94869, 0.0118, -0.19908, 0.00713, 0.00335, 362.0]
        option_2 = [113.34, 113.35, 100.0, 20161007.0, 2.0, 13.15, 13.55, 100, u'call', u'AAPL161007C00100000', u'None', 0.94869, 0.0118, -0.19908, 0.00713, 0.00335, 362.0]
        option_3 = [113.34, 113.35, 100.0, 20161008.0, 2.0, 13.15, 13.55, 100, u'call', u'AAPL161007C00100000', u'None', 0.94869, 0.0118, -0.19908, 0.00713, 0.00335, 362.0]
        option_4 = [113.34, 113.35, 100.0, 20161007.0, 2.0, 13.15, 13.55, 100, u'call', u'AAPL161007C00100000', u'None', 0.94869, 0.0118, -0.19908, 0.00713, 0.00335, 362.0]
        result = options_have_same_xdate(option_1, option_2, option_3, option_4)
        self.assertEqual(result,False)

    def test_4_options_have_diff_xdate_4(self):
        option_1 = [113.34, 113.35, 100.0, 20161007.0, 2.0, 13.15, 13.55, 100, u'call', u'AAPL161007C00100000', u'None', 0.94869, 0.0118, -0.19908, 0.00713, 0.00335, 362.0]
        option_2 = [113.34, 113.35, 100.0, 20161007.0, 2.0, 13.15, 13.55, 100, u'call', u'AAPL161007C00100000', u'None', 0.94869, 0.0118, -0.19908, 0.00713, 0.00335, 362.0]
        option_3 = [113.34, 113.35, 100.0, 20161007.0, 2.0, 13.15, 13.55, 100, u'call', u'AAPL161007C00100000', u'None', 0.94869, 0.0118, -0.19908, 0.00713, 0.00335, 362.0]
        option_4 = [113.34, 113.35, 100.0, 20161008.0, 2.0, 13.15, 13.55, 100, u'call', u'AAPL161007C00100000', u'None', 0.94869, 0.0118, -0.19908, 0.00713, 0.00335, 362.0]
        result = options_have_same_xdate(option_1, option_2, option_3, option_4)
        self.assertEqual(result,False)

    def test_4_options_have_diff_xdate_5(self):
        option_1 = [113.34, 113.35, 100.0, 20161007.0, 2.0, 13.15, 13.55, 100, u'call', u'AAPL161007C00100000', u'None', 0.94869, 0.0118, -0.19908, 0.00713, 0.00335, 362.0]
        option_2 = [113.34, 113.35, 100.0, 20161008.0, 2.0, 13.15, 13.55, 100, u'call', u'AAPL161007C00100000', u'None', 0.94869, 0.0118, -0.19908, 0.00713, 0.00335, 362.0]
        option_3 = [113.34, 113.35, 100.0, 20161007.0, 2.0, 13.15, 13.55, 100, u'call', u'AAPL161007C00100000', u'None', 0.94869, 0.0118, -0.19908, 0.00713, 0.00335, 362.0]
        option_4 = [113.34, 113.35, 100.0, 20161008.0, 2.0, 13.15, 13.55, 100, u'call', u'AAPL161007C00100000', u'None', 0.94869, 0.0118, -0.19908, 0.00713, 0.00335, 362.0]
        result = options_have_same_xdate(option_1, option_2, option_3, option_4)
        self.assertEqual(result,False)



# OPTIONS_HAVE_SAME_STRIKEPRICE TESTS
    def test_2_options_have_same_strike(self):
        option_1 = [113.34, 113.35, 100.0, 20161007.0, 2.0, 13.15, 13.55, 100, u'call', u'AAPL161007C00100000', u'None', 0.94869, 0.0118, -0.19908, 0.00713, 0.00335, 362.0]
        option_2 = [113.34, 113.35, 100.0, 20161007.0, 2.0, 13.15, 13.55, 100, u'call', u'AAPL161007C00100000', u'None', 0.94869, 0.0118, -0.19908, 0.00713, 0.00335, 362.0]
        result = options_have_same_strikeprice(option_1, option_2)
        self.assertEqual(result,True)

    def test_2_options_have_diff_strike(self):
        option_1 = [113.34, 113.35, 100.0, 20161007.0, 2.0, 13.15, 13.55, 100, u'call', u'AAPL161007C00100000', u'None', 0.94869, 0.0118, -0.19908, 0.00713, 0.00335, 362.0]
        option_2 = [113.34, 113.35, 102.0, 20161008.0, 2.0, 13.15, 13.55, 100, u'call', u'AAPL161007C00100000', u'None', 0.94869, 0.0118, -0.19908, 0.00713, 0.00335, 362.0]
        result = options_have_same_strikeprice(option_1, option_2)
        self.assertEqual(result,False)

    def test_4_options_have_same_strike(self):
        option_1 = [113.34, 113.35, 100.0, 20161008.0, 2.0, 13.15, 13.55, 100, u'call', u'AAPL161007C00100000', u'None', 0.94869, 0.0118, -0.19908, 0.00713, 0.00335, 362.0]
        option_2 = [113.34, 113.35, 100.0, 20161008.0, 2.0, 13.15, 13.55, 100, u'call', u'AAPL161007C00100000', u'None', 0.94869, 0.0118, -0.19908, 0.00713, 0.00335, 362.0]
        option_3 = [113.34, 113.35, 100.0, 20161008.0, 2.0, 13.15, 13.55, 100, u'call', u'AAPL161007C00100000', u'None', 0.94869, 0.0118, -0.19908, 0.00713, 0.00335, 362.0]
        option_4 = [113.34, 113.35, 100.0, 20161008.0, 2.0, 13.15, 13.55, 100, u'call', u'AAPL161007C00100000', u'None', 0.94869, 0.0118, -0.19908, 0.00713, 0.00335, 362.0]
        result = options_have_same_strikeprice(option_1, option_2, option_3, option_4)
        self.assertEqual(result,True)

    def test_4_options_have_diff_strike_1(self):
        option_1 = [113.34, 113.35, 100.0, 20161007.0, 2.0, 13.15, 13.55, 100, u'call', u'AAPL161007C00100000', u'None', 0.94869, 0.0118, -0.19908, 0.00713, 0.00335, 362.0]
        option_2 = [113.34, 113.35, 102.0, 20161008.0, 2.0, 13.15, 13.55, 100, u'call', u'AAPL161007C00100000', u'None', 0.94869, 0.0118, -0.19908, 0.00713, 0.00335, 362.0]
        option_3 = [113.34, 113.35, 100.0, 20161007.0, 2.0, 13.15, 13.55, 100, u'call', u'AAPL161007C00100000', u'None', 0.94869, 0.0118, -0.19908, 0.00713, 0.00335, 362.0]
        option_4 = [113.34, 113.35, 100.0, 20161007.0, 2.0, 13.15, 13.55, 100, u'call', u'AAPL161007C00100000', u'None', 0.94869, 0.0118, -0.19908, 0.00713, 0.00335, 362.0]
        result = options_have_same_strikeprice(option_1, option_2, option_3, option_4)
        self.assertEqual(result,False)

    def test_4_options_have_diff_strike_2(self):
        option_1 = [113.34, 113.35, 100.0, 20161007.0, 2.0, 13.15, 13.55, 100, u'call', u'AAPL161007C00100000', u'None', 0.94869, 0.0118, -0.19908, 0.00713, 0.00335, 362.0]
        option_2 = [113.34, 113.35, 102.0, 20161008.0, 2.0, 13.15, 13.55, 100, u'call', u'AAPL161007C00100000', u'None', 0.94869, 0.0118, -0.19908, 0.00713, 0.00335, 362.0]
        option_3 = [113.34, 113.35, 100.0, 20161007.0, 2.0, 13.15, 13.55, 100, u'call', u'AAPL161007C00100000', u'None', 0.94869, 0.0118, -0.19908, 0.00713, 0.00335, 362.0]
        option_4 = [113.34, 113.35, 100.0, 20161007.0, 2.0, 13.15, 13.55, 100, u'call', u'AAPL161007C00100000', u'None', 0.94869, 0.0118, -0.19908, 0.00713, 0.00335, 362.0]
        result = options_have_same_strikeprice(option_1, option_2, option_3, option_4)
        self.assertEqual(result,False)

    def test_4_options_have_diff_strike_3(self):
        option_1 = [113.34, 113.35, 100.0, 20161007.0, 2.0, 13.15, 13.55, 100, u'call', u'AAPL161007C00100000', u'None', 0.94869, 0.0118, -0.19908, 0.00713, 0.00335, 362.0]
        option_2 = [113.34, 113.35, 100.0, 20161008.0, 2.0, 13.15, 13.55, 100, u'call', u'AAPL161007C00100000', u'None', 0.94869, 0.0118, -0.19908, 0.00713, 0.00335, 362.0]
        option_3 = [113.34, 113.35, 102.0, 20161007.0, 2.0, 13.15, 13.55, 100, u'call', u'AAPL161007C00100000', u'None', 0.94869, 0.0118, -0.19908, 0.00713, 0.00335, 362.0]
        option_4 = [113.34, 113.35, 100.0, 20161007.0, 2.0, 13.15, 13.55, 100, u'call', u'AAPL161007C00100000', u'None', 0.94869, 0.0118, -0.19908, 0.00713, 0.00335, 362.0]
        result = options_have_same_strikeprice(option_1, option_2, option_3, option_4)
        self.assertEqual(result,False)

    def test_4_options_have_diff_strike_4(self):
        option_1 = [113.34, 113.35, 100.0, 20161007.0, 2.0, 13.15, 13.55, 100, u'call', u'AAPL161007C00100000', u'None', 0.94869, 0.0118, -0.19908, 0.00713, 0.00335, 362.0]
        option_2 = [113.34, 113.35, 100.0, 20161008.0, 2.0, 13.15, 13.55, 100, u'call', u'AAPL161007C00100000', u'None', 0.94869, 0.0118, -0.19908, 0.00713, 0.00335, 362.0]
        option_3 = [113.34, 113.35, 100.0, 20161007.0, 2.0, 13.15, 13.55, 100, u'call', u'AAPL161007C00100000', u'None', 0.94869, 0.0118, -0.19908, 0.00713, 0.00335, 362.0]
        option_4 = [113.34, 113.35, 102.0, 20161007.0, 2.0, 13.15, 13.55, 100, u'call', u'AAPL161007C00100000', u'None', 0.94869, 0.0118, -0.19908, 0.00713, 0.00335, 362.0]
        result = options_have_same_strikeprice(option_1, option_2, option_3, option_4)
        self.assertEqual(result,False)

    def test_4_options_have_diff_strike_5(self):
        option_1 = [113.34, 113.35, 100.0, 20161007.0, 2.0, 13.15, 13.55, 100, u'call', u'AAPL161007C00100000', u'None', 0.94869, 0.0118, -0.19908, 0.00713, 0.00335, 362.0]
        option_2 = [113.34, 113.35, 102.2, 20161008.0, 2.0, 13.15, 13.55, 100, u'call', u'AAPL161007C00100000', u'None', 0.94869, 0.0118, -0.19908, 0.00713, 0.00335, 362.0]
        option_3 = [113.34, 113.35, 100.0, 20161007.0, 2.0, 13.15, 13.55, 100, u'call', u'AAPL161007C00100000', u'None', 0.94869, 0.0118, -0.19908, 0.00713, 0.00335, 362.0]
        option_4 = [113.34, 113.35, 100.2, 20161007.0, 2.0, 13.15, 13.55, 100, u'call', u'AAPL161007C00100000', u'None', 0.94869, 0.0118, -0.19908, 0.00713, 0.00335, 362.0]
        result = options_have_same_strikeprice(option_1, option_2, option_3, option_4)
        self.assertEqual(result,False)


if __name__ == '__main__':
    unittest.main()