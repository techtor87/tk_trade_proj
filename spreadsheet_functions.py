#!/usr/bin/env python

import numpy as np
import openpyxl as pyxl
import string

from tk_functions import *
from trading_stratigies import *

def setup_columns( _worksheet ):
    wb = pyxl.Workbook()
    ws = wb.create_sheet()
    ws['A1'] = 42
    ws.append([1,2,3])
    wb.save(_worksheet)
    return


def setup_trade_columns( _tradesheet ):
    return

