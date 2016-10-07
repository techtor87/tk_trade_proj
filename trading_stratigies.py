#!/usr/bin/env python

from tk_functions import *
from trading_functions import *
from proj_1 import *
from itertools import *

def covered_call_profit(_bid, _strike_call):
    return 0

def iron_condor_profit():
    return 0

def long_box_profit( _low_strike_call, _high_strike_call, _low_strike_put, _high_strike_put):
    bull_call_value = long_call_spread(_low_strike_call, _high_strike_call)
    print bull_call_value
    bear_put_value = long_put_spread(_low_strike_put, _high_strike_put)
    print bear_put_value
    total_cost = bull_call_value + bear_put_value
    print total_cost
    total_value = _high_strike_call[2] - _low_strike_call[2]
    print total_value
    return total_value - total_cost - (commision_flat_rate - (commision_per_contract * 4))/100

def short_box_profit( _low_strike_call, _high_strike_call, _low_strike_put, _high_strike_put):
    bear_call_value = short_call_spread(_low_strike_call, _high_strike_call)
    print bull_call_value
    bull_put_value = short_put_spread(_low_strike_put, _high_strike_put)
    print bear_put_value
    total_cost = bear_call_value + bull_put_value
    print total_cost
    total_value = _high_strike_call[2] - _low_strike_call[2]
    print total_value
    return total_value - total_cost - (commision_flat_rate - (commision_per_contract * 4))/100

def covered_call( _cur, _stock, _data, _bid, _ask ):
    return

def iron_condor( _cur, _stock, _data, _bid, _ask ):
    return

def long_box( low_strike_call, high_strike_call, low_strike_put, high_strike_put ):
    if (options_have_same_xdate( low_strike_call, high_strike_call, low_strike_put, high_strike_put) and
        options_have_same_strikeprice( low_strike_call, low_strike_put) and
        options_have_same_strikeprice( high_strike_call, high_strike_put ) and
        low_strike_call[2] < high_strike_call[2] ): # low strike is less than high strike

        value = long_box_profit( low_strike_call, high_strike_call, low_strike_put, high_strike_put )
        if value > 0:
            print value

    return

def short_box( low_strike_call, high_strike_call, low_strike_put, high_strike_put ):
    if (options_have_same_xdate( low_strike_call, high_strike_call, low_strike_put, high_strike_put) and
        options_have_same_strikeprice( low_strike_call, low_strike_put) and
        options_have_same_strikeprice( high_strike_call, high_strike_put ) and
        low_strike_call[2] < high_strike_call[2] ): # low strike is less than high strike

        value = short_box_profit( low_strike_call, high_strike_call, low_strike_put, high_strike_put )
        if value > 0:
            print value

    return
