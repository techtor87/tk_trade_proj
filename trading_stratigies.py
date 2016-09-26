#!/usr/bin/env python

from tk_functions import *

success_percentage = 0.75

def covered_call_profit(_bid, _strike_call):
    return 0

def iron_condor_profit():
    return 0

def long_box_profit( _low_strike_call, _high_strike_call, _low_strike_put, _high_strike_put):
    bull_call_spread = _low_strike_call.ask.to_f() - _high_strike_call.bid.to_f()
    bear_put_spread = _high_strike_put.ask.to_f() - _low_strike_put.ask.to_f()
    total_cost = bull_call_spread + bear_put_spread
    total_value = _high_strike_call.strikeprice.to_f() - _low_strike_call.strikeprice.to_f()
    return total_value - total_cost - (commision_flat_rate - (commision_per_contract * 4))/100

def short_box_profit( _low_strike_call, _high_strike_call, _low_strike_put, _high_strike_put):
    return 0


