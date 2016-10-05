#! /usr/bin/env python

import string
import sqlite3 as lite

from tk_functions import *
from trading_stratigies import *

def setup_tables( cur , stock_list):
    sql_text  = "CREATE TABLE IF NOT EXISTS trades( "
    sql_text += " trade_type TEXT, "
    sql_text += " bid REAL, "
    sql_text += " ask REAL, "
    sql_text += " trade_profit REAL, "
    sql_text += " trade_1 BLOB, "
    sql_text += " trade_2 BLOB, "
    sql_text += " trade_3 BLOB, "
    sql_text += " trade_4 BLOB "
    sql_text += ")"
    cur.execute(sql_text)

    for stock in stock_list:
        sql_text  = "CREATE TABLE IF NOT EXISTS "
        sql_text += stock
        sql_text += "( cur_bid REAL, "
        sql_text += "cur_ask REAL, "
        sql_text += "strike_price REAL, "
        sql_text += "xdate REAL, "
        sql_text += "days_to_expir REAL, "
        sql_text += "bid REAL, "
        sql_text += "ask REAL, "
        sql_text += "contract_size INT, "
        sql_text += "put_call TEXT, "
        sql_text += "symbol TEXT, "
        sql_text += "imp_vol TEXT, "
        sql_text += "delta REAL, "
        sql_text += "gamma REAL, "
        sql_text += "theta REAL, "
        sql_text += "vega REAL, "
        sql_text += "rho REAL, "
        sql_text += "open_interest REAL "
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

def find_profitable_trades( _cur, _data, _bid, _ask):
    covered_call( _cur, _data, _bid, _ask )
    iron_condor(  _cur, _data, _bid, _ask )
    long_box(  _cur, _data, _bid, _ask )
    short_box(  _cur, _data, _bid, _ask )

