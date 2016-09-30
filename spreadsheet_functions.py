#!/usr/bin/env python

import numpy as np
import openpyxl as pyxl
import string

from tk_functions import *
from trading_stratigies import *

def setup_columns( _worksheet ):
    _worksheet['A1'] = 'Cur Bid'
    _worksheet['B1'] = 'Cur Ask'
    _worksheet['C1'] = 'strikeprice'
    _worksheet['d1'] = 'xdate'
    _worksheet['e1'] = 'days_to_expir'

    _worksheet['g1'] = 'bid'
    _worksheet['h1'] = 'ask'
    _worksheet['i1'] = 'contract_size'
    _worksheet['j1'] = 'p/c'
    _worksheet['k1'] = 'symbol'
    _worksheet['l1'] = 'imp_vol'
    _worksheet['m1'] = 'delta'
    _worksheet['n1'] = 'gamma'
    _worksheet['o1'] = 'theta'
    _worksheet['p1'] = 'vega'
    _worksheet['q1'] = 'rho'
    _worksheet['r1'] = 'openinterest'

    _worksheet['t1'] = 'bid'
    _worksheet['u1'] = 'ask'
    _worksheet['v1'] = 'contract_size'
    _worksheet['w1'] = 'p/c'
    _worksheet['x1'] = 'symbol'
    _worksheet['y1'] = 'imp_vol'
    _worksheet['z1'] = 'delta'
    _worksheet['aa1'] = 'gamma'
    _worksheet['ab1'] = 'theta'
    _worksheet['ac1'] = 'vega'
    _worksheet['ad1'] = 'rho'
    _worksheet['ae1'] = 'openinterest'
    return _worksheet


def setup_trade_columns( _tradesheet ):
    _tradesheet.cell(row=1, column=1, value='Trade Type')
    _tradesheet.cell(row=1, column=2, value='Bid')
    _tradesheet.cell(row=1, column=3, value='Ask')
    _tradesheet.cell(row=1, column=4, value='Trade Profit')
    last_column = 5
    for i in xrange(1,5):
        _tradesheet.cell(row=1, column=last_column+1, value='put_call')
        _tradesheet.cell(row=1, column=last_column+2, value='rootsymbol')
        _tradesheet.cell(row=1, column=last_column+3, value='strikeprice')
        _tradesheet.cell(row=1, column=last_column+4, value='xdate')
        _tradesheet.cell(row=1, column=last_column+5, value='ask')
        _tradesheet.cell(row=1, column=last_column+6, value='ask_time')
        _tradesheet.cell(row=1, column=last_column+7, value='asksz')
        _tradesheet.cell(row=1, column=last_column+8, value='basis')
        _tradesheet.cell(row=1, column=last_column+9, value='bid')
        _tradesheet.cell(row=1, column=last_column+10, value='bid_time')
        _tradesheet.cell(row=1, column=last_column+11, value='bidsz')
        _tradesheet.cell(row=1, column=last_column+12, value='chg')
        _tradesheet.cell(row=1, column=last_column+13, value='chg_sign')
        _tradesheet.cell(row=1, column=last_column+14, value='chg_t')
        _tradesheet.cell(row=1, column=last_column+15, value='cl')
        _tradesheet.cell(row=1, column=last_column+16, value='days_to_expr')
        _tradesheet.cell(row=1, column=last_column+17, value='exch')
        _tradesheet.cell(row=1, column=last_column+18, value='exch_desc')
        _tradesheet.cell(row=1, column=last_column+19, value='hi')
        _tradesheet.cell(row=1, column=last_column+20, value='incr_vl')
        _tradesheet.cell(row=1, column=last_column+21, value='issue_desc')
        _tradesheet.cell(row=1, column=last_column+22, value='last')
        _tradesheet.cell(row=1, column=last_column+23, value='lo')
        _tradesheet.cell(row=1, column=last_column+24, value='op_delivery')
        _tradesheet.cell(row=1, column=last_column+25, value='op_flag')
        _tradesheet.cell(row=1, column=last_column+26, value='op_style')
        _tradesheet.cell(row=1, column=last_column+27, value='op_subclass')
        _tradesheet.cell(row=1, column=last_column+28, value='opn')
        _tradesheet.cell(row=1, column=last_column+29, value='pchg')
        _tradesheet.cell(row=1, column=last_column+30, value='pchg_sign')
        _tradesheet.cell(row=1, column=last_column+31, value='pcls')
        _tradesheet.cell(row=1, column=last_column+32, value='phi')
        _tradesheet.cell(row=1, column=last_column+33, value='plo')
        _tradesheet.cell(row=1, column=last_column+34, value='popn')
        _tradesheet.cell(row=1, column=last_column+35, value='pr_date')
        _tradesheet.cell(row=1, column=last_column+36, value='pr_openinterest')
        _tradesheet.cell(row=1, column=last_column+37, value='prchg')
        _tradesheet.cell(row=1, column=last_column+38, value='prem_mult')
        _tradesheet.cell(row=1, column=last_column+39, value='pvol')
        _tradesheet.cell(row=1, column=last_column+40, value='secclass')
        _tradesheet.cell(row=1, column=last_column+41, value='sesn')
        _tradesheet.cell(row=1, column=last_column+42, value='symbol')
        _tradesheet.cell(row=1, column=last_column+43, value='tcond')
        _tradesheet.cell(row=1, column=last_column+44, value='timestamp')
        _tradesheet.cell(row=1, column=last_column+45, value='tr_num')
        _tradesheet.cell(row=1, column=last_column+46, value='tradetick')
        _tradesheet.cell(row=1, column=last_column+47, value='under_susip')
        _tradesheet.cell(row=1, column=last_column+48, value='vl')
        _tradesheet.cell(row=1, column=last_column+49, value='vwap')
        _tradesheet.cell(row=1, column=last_column+50, value='wk52hi')
        _tradesheet.cell(row=1, column=last_column+51, value='wk52hidate')
        _tradesheet.cell(row=1, column=last_column+52, value='wk52lo')
        _tradesheet.cell(row=1, column=last_column+53, value='wk52lodate')
        _tradesheet.cell(row=1, column=last_column+54, value='imp_vol')
        _tradesheet.cell(row=1, column=last_column+55, value='idelta')
        _tradesheet.cell(row=1, column=last_column+56, value='igamma')
        _tradesheet.cell(row=1, column=last_column+57, value='itheta')
        _tradesheet.cell(row=1, column=last_column+58, value='ivega')
        _tradesheet.cell(row=1, column=last_column+59, value='irho')
        _tradesheet.cell(row=1, column=last_column+60, value='openinterest')

        last_column = last_column + 61

    return

