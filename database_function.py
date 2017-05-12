#! /usr/bin/env python

import string
import sqlite3 as lite

from tk_functions import *
from trading_stratigies import *

def setup_tables( cur , stock_list):

    sql_text  = "CREATE TABLE IF NOT EXISTS trades( "
    sql_text += " trade_type TEXT, "            # trades[0] = trade_type
    sql_text += " bid REAL, "                   # trades[1] = bid
    sql_text += " ask REAL, "                   # trades[2] = ask
    sql_text += " trade_profit REAL, "          # trades[3] = trade_profit
    sql_text += " trade_1 BLOB, "               # trades[4] = trade_1
    sql_text += " trade_2 BLOB, "               # trades[5] = trade_2
    sql_text += " trade_3 BLOB, "               # trades[6] = trade_3
    sql_text += " trade_4 BLOB "                # trades[7] = trade_4
    sql_text += ")"
    cur.execute(sql_text)

    for stock in stock_list:
        sql_text  = "CREATE TABLE IF NOT EXISTS "
        sql_text += stock
        sql_text += "( cur_bid REAL, "          # stock[0] = cur_bid
        sql_text += "cur_ask REAL, "            # stock[1] = cur_ask
        sql_text += "strike_price REAL, "       # stock[2] = strike_price
        sql_text += "xdate REAL, "              # stock[3] = xdate
        sql_text += "days_to_expir REAL, "      # stock[4] = days_to_expir
        sql_text += "bid REAL, "                # stock[5] = bid
        sql_text += "ask REAL, "                # stock[6] = ask
        sql_text += "contract_size INT, "       # stock[7] = contract_size
        sql_text += "put_call TEXT, "           # stock[8] = put_call
        sql_text += "symbol TEXT, "             # stock[9] = symbol
        sql_text += "imp_vol TEXT, "            # stock[10]= imp_vol
        sql_text += "delta REAL, "              # stock[11]= delta
        sql_text += "gamma REAL, "              # stock[12]= gamma
        sql_text += "theta REAL, "              # stock[13]= theta
        sql_text += "vega REAL, "               # stock[14]= vega
        sql_text += "rho REAL, "                # stock[15]= rho
        sql_text += "open_interest REAL "       # stock[16]= open_interest
        sql_text += ")"
        # print sql_text
        cur.execute(sql_text)

def add_quote( cur, stock, _data, _bid, _ask ):
    # print _data.search.search_quote[0].xdate
    for quote in _data:
        sql_text  = "INSERT INTO " + stock + " VALUES( "
        sql_text += str(_bid) + ", "
        sql_text += str(_ask) + ", "
        sql_text += str(quote.strikeprice ) + ", "
        sql_text += str(quote.xdate ) + ", "
        sql_text += str(quote.days_to_expiration ) + ", "
        sql_text += str(quote.bid ) + ", "
        sql_text += str(quote.ask ) + ", "
        sql_text += str(quote.contract_size ) + ", "
        sql_text += "'" + str(quote.put_call ) + "', "
        sql_text += "'" + str(quote.symbol ) + "', "
        sql_text += "'" + str(quote.imp_volatility ) + "', "
        sql_text += str(quote.idelta ) + ", "
        sql_text += str(quote.igamma ) + ", "
        sql_text += str(quote.itheta ) + ", "
        sql_text += str(quote.ivega ) + ", "
        sql_text += str(quote.irho ) + ", "
        sql_text += str(quote.openinterest ) + ")"
        # print sql_text
        cur.execute(sql_text)

def add_trade( cur, _bid, _ask, _type, _profit, _option1, _option2, _option3, _option4):
    sql_test  = "INSERT INTO trades VALUES ( "
    sql_test += "'" + _type + "', "
    sql_text += str(_bid) + ", "
    sql_text += str(_ask) + ", "
    sql_test += str(_profit) + ". "
    sql_test += str(_option1) + ". "
    sql_test += str(_option2) + ". "
    sql_test += str(_option3) + ". "
    sql_test += str(_option4) + ")"
    print sql_test
    cur.execute(sql_text)

def find_profitable_trades( _cur, _stock, _data, _bid, _ask):
    sql_text = "SELECT * FROM " + _stock + " WHERE put_call='put'AND contract_size=100 AND open_interest>50 ORDER BY xdate, strike_price LIMIT 20"
    _cur.execute(sql_text)
    data_rows_put = _cur.fetchall()

    sql_text = "SELECT * FROM " + _stock + " WHERE put_call='call' AND contract_size=100 AND open_interest>50 ORDER BY xdate, strike_price"
    _cur.execute(sql_text)
    data_rows_call = _cur.fetchall()

    start_time1 = time.time()
    start_time2 = time.time()
    # start_time3 = time.time()
    for low_strike_p in data_rows_put:
        for hi_strike_p in data_rows_put:
            for low_strike_c in data_rows_call:
                for hi_strike_c in data_rows_call:
                    # covered_call( _cur, _stock, _data, _bid, _ask )
                    # iron_condor(  _cur, _stock, _data, _bid, _ask )
                    long_box( low_strike_c, hi_strike_c, low_strike_p, hi_strike_p )
                    short_box( low_strike_c, hi_strike_c, low_strike_p, hi_strike_p )


                # print 'inner loop done - {}'.format(time.time()-start_time3)
                # start_time3 = time.time()

        #     print 'middle loop done - {}'.format(time.time()-start_time2)
        #     start_time2 = time.time()

        # print 'outer loop done - {}'.format(time.time()-start_time1)
        # start_time1 = time.time()

