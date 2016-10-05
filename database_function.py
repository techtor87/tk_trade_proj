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
        sql_text += "imp_vol REAL, "
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
    sql_text  = "INSERT INTO " + stock + " VALUES( "
    sql_text += str(_bid) + ", "
    sql_text += str(_ask) + ", "
    sql_text += "0, "
    sql_text += "0, "
    sql_text += "0, "
    sql_text += "0, "
    sql_text += "0, "
    sql_text += "0, "
    sql_text += "0, "
    sql_text += "0, "
    sql_text += "0, "
    sql_text += "0, "
    sql_text += "0, "
    sql_text += "0, "
    sql_text += "0, "
    sql_text += "0, "
    sql_text += "0 ) "
    print sql_text
    cur.execute(sql_text)
