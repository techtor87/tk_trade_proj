#!/usr/bin/env python

import unittest
from trading_functions_test import *

class trading_functions_test_class(unittest.TestCase):

    def setUp(self):
        return

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

    def test_4_options_have_diff_xdate(self):
        option_1 = [113.34, 113.35, 100.0, 20161007.0, 2.0, 13.15, 13.55, 100, u'call', u'AAPL161007C00100000', u'None', 0.94869, 0.0118, -0.19908, 0.00713, 0.00335, 362.0]
        option_2 = [113.34, 113.35, 100.0, 20161008.0, 2.0, 13.15, 13.55, 100, u'call', u'AAPL161007C00100000', u'None', 0.94869, 0.0118, -0.19908, 0.00713, 0.00335, 362.0]
        option_3 = [113.34, 113.35, 100.0, 20161007.0, 2.0, 13.15, 13.55, 100, u'call', u'AAPL161007C00100000', u'None', 0.94869, 0.0118, -0.19908, 0.00713, 0.00335, 362.0]
        option_4 = [113.34, 113.35, 100.0, 20161007.0, 2.0, 13.15, 13.55, 100, u'call', u'AAPL161007C00100000', u'None', 0.94869, 0.0118, -0.19908, 0.00713, 0.00335, 362.0]
        result = options_have_same_xdate(option_1, option_2, option_3, option_4)
        self.assertEqual(result,False)


if __name__ == '__main__':
    import sys
    sys.path.append('/home/ubuntu/workspace/tk_trade_proj')
    print sys.path
    unittest.main()