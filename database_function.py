#! /usr/bin/env python

import string
import sqlite3 as lite

from tk_functions import *
from trading_stratigies import *

def setup_tables( cur , stock_list):
    cur.execute("CREATE TABLE IF NOT EXISTS trades(Id INT, Name TEXT, Price INT)")
    for stock in stock_list:
        cur.execute("CREATE TABLE IF NOT EXISTS :stock_name(Id INT, Name TEXT, Price INT)",{"stock_name": stock})
