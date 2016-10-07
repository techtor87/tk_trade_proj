#!/usr/bin/env python

from tk_functions import *
from proj_1 import *


def long_call_spread(_low_strike_call, _high_strike_call):
    # Buy low strike call and sell high strike call
    return _high_strike_call[5] - _low_strike_call[6]

def long_put_spread(_low_strike_put, _high_strike_put):
    # Sell low strike put and buy high strike put
    return _low_strike_put[5] - _high_strike_put[6]

def short_call_spread(_low_strike_call, _high_strike_call):
    # Buy low strike call and sell high strike call
    return _low_strike_call[5] - _high_strike_call[6]

def short_put_spread(_low_strike_put, _high_strike_put):
    # Sell low strike put and buy high strike put
    return _high_strike_put[5] - _low_strike_put[6]


def options_have_same_xdate( _opt1, _opt2, _opt3=None, _opt4=None ):
    if ( _opt1[3] == _opt2[3] ):
        same = True
    else:
        same = False

    if ( _opt3 != None ):
        if( _opt1[3] == _opt3[3] ):
            same = True and same
        else:
            same = False and same

    if( _opt4 != None ):
        if( _opt1[3] == _opt4[3] ):
            same = True and same
        else:
            same = False and same
    # print same ,  _opt1[3], _opt2[3], _opt3[3], _opt4[3]
    return same

def options_have_same_strikeprice( _opt1, _opt2, _opt3=None, _opt4=None ):
    if ( _opt1[2] == _opt2[2] ):
        same = True
    else:
        same = False

    if ( _opt3 != None ):
        if( _opt1[2] == _opt3[2] ):
            same = True and same
        else:
            same = False and same

    if( _opt4 != None ):
        if( _opt1[2] == _opt4[2] ):
            same = True and same
        else:
            same = False and same
    # print same,  _opt1[2], _opt2[2]
    return same

