#!/usr/bin/env python

import sys, os
home_dir = os.path.expanduser('~')
home_dir += '/workspace/tk_trade_proj'
print home_dir
sys.path.append(home_dir)

import unittest
from trading_stratigies import *

class trading_stratigies_test_class(unittest.TestCase):

    def setUp(self):
        return

# long_box_profit TESTS
    def test_long_box_profit_1(self):
        low_call_option = [114.13, 114.14, 150.0, 20161118.0, 44.0, 0.02, 0.04, 100, u'call', u'AAPL161118C00150000', u'None', 0.00751, 0.00166, -0.00293, 0.00822, 0.00099, 1787.0]
        high_call_option = [113.34, 113.35, 90.0, 20161007.0, 2.0, 23.15, 23.55, 100, u'call', u'AAPL161007C00090000', u'None', 0.96726, 0.00497, -0.19944, 0.00495, 0.00307, 84.0]
        low_put_option = [113.34, 113.35, 90.0, 20161007.0, 2.0, 0.0, 0.01, 100, u'put', u'AAPL161007P00090000', u'None', -0.00184, 0.00064, -0.00499, 0.0004, -1e-05, 108.0]
        high_put_option = [113.34, 113.35, 90.0, 20161007.0, 2.0, 0.0, 0.01, 100, u'put', u'AAPL161007P00090000', u'None', -0.00184, 0.00064, -0.00499, 0.0004, -1e-05, 108.0]
        result = long_box_profit(low_call_option, high_call_option, low_put_option, high_put_option)
        self.assertAlmostEqual(result,0.0)


if __name__ == '__main__':
    unittest.main()