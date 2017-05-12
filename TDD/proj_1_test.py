#!/usr/bin/env python

import sys, os
home_dir = os.path.expanduser('~')
home_dir += '/workspace/tk_trade_proj'
print home_dir
sys.path.append(home_dir)

import unittest
from proj_1 import *

class proj_1_test_class(unittest.TestCase):

    def setUp(self):
        return
    
if __name__ == '__main__':
    unittest.main()