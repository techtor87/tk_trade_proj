#!/usr/bin/env python

from tk_functions import *
from trading_functions import *
from proj_1 import *

def covered_call_profit(_bid, _strike_call):
    return 0

def iron_condor_profit():
    return 0

def long_box_profit( _low_strike_call, _high_strike_call, _low_strike_put, _high_strike_put):
    bull_call_value = long_call_spread(_low_strike_call, _high_strike_call)
    bear_put_value = long_put_spread(_low_strike_put, _high_strike_put)
    total_cost = bull_call_value + bear_put_value
    total_value = _high_strike_call[2] - _low_strike_call[2]
    return total_value - total_cost - (commision_flat_rate - (commision_per_contract * 4))/100

def short_box_profit( _low_strike_call, _high_strike_call, _low_strike_put, _high_strike_put):
    bull_call_value = long_call_spread(_low_strike_call, _high_strike_call)
    bear_put_value = long_put_spread(_low_strike_put, _high_strike_put)
    total_cost = bull_call_value + bear_put_value
    total_value = _high_strike_call[2] - _low_strike_call[2]
    return total_value - total_cost - (commision_flat_rate - (commision_per_contract * 4))/100

def covered_call( _cur, _stock, _data, _bid, _ask ):
    return

def iron_condor( _cur, _stock, _data, _bid, _ask ):
    return

def long_box( _cur, _stock, _data, _bid, _ask ):
    sql_text = "SELECT * FROM " + _stock + " WHERE put_call='put'AND contract_size=100 AND open_interest>50 ORDER BY xdate, strike_price LIMIT 20"
    _cur.execute(sql_text)
    data_rows_put = _cur.fetchall()

    sql_text = "SELECT * FROM " + _stock + " WHERE put_call='call' AND contract_size=100 AND open_interest>50 ORDER BY xdate, strike_price"
    _cur.execute(sql_text)
    data_rows_call = _cur.fetchall()

    for low_strike_p in data_rows_put:
        for hi_strike_p in data_rows_put:
            for low_strike_c in data_rows_call:
                for hi_strike_c in data_rows_call:
                    if (options_have_same_xdate( low_strike_c, hi_strike_c, low_strike_p, hi_strike_p) and
                        options_have_same_strikeprice( low_strike_c, low_strike_p) and
                        options_have_same_strikeprice( hi_strike_c, hi_strike_p ) and
                        low_strike_c[2] < hi_strike_c[2] ): # low strike is less than high strike

                        value = short_box_profit(low_strike_c,hi_strike_c,low_strike_p,hi_strike_p)
                        if value > 0:
                            print value

    return

def short_box( _cur, _stock, _data, _bid, _ask ):
    sql_text = "SELECT * FROM " + _stock + " WHERE put_call='put'AND contract_size=100 AND open_interest>50 ORDER BY xdate, strike_price LIMIT 20"
    _cur.execute(sql_text)
    data_rows_put = _cur.fetchall()

    sql_text = "SELECT * FROM " + _stock + " WHERE put_call='call' AND contract_size=100 AND open_interest>50 ORDER BY xdate, strike_price"
    _cur.execute(sql_text)
    data_rows_call = _cur.fetchall()

    for low_strike_p in data_rows_put:
        for hi_strike_p in data_rows_put:
            for low_strike_c in data_rows_call:
                for hi_strike_c in data_rows_call:
                    if (options_have_same_xdate( low_strike_c, hi_strike_c, low_strike_p, hi_strike_p) and
                        options_have_same_strikeprice( low_strike_c, low_strike_p) and
                        options_have_same_strikeprice( hi_strike_c, hi_strike_p ) and
                        low_strike_c[2] < hi_strike_c[2] ): # low strike is less than high strike

                        value = short_box_profit(low_strike_c,hi_strike_c,low_strike_p,hi_strike_p)
                        if value > 0:
                            print value

    return
