#!/usr/bin/env python

# IRA
# 100 - CSCO
# 210 - GE

#  50 - AAPL
# 110 - BP
# 100 - CBI
#  50 - DE
# 100 - M
# 100 - MSFT
# 100 - PG
#  50 - CRM

import sys
import oauth2 as oauth
import time

import sqlite3 as lite
from database_function import *
from spreadsheet_functions import *


def main_output():
    con = lite.connect('trade_test.db')
    with con:
        cur = con.cursor()

    # initialize workbook
    # trade_workbook = pyxl.Workbook()
    # trade_sheet = trade_workbook.active
    # trade_sheet.title = "Trade List"
    # setup_trade_columns( trade_sheet )
    # for stock in stock_list:
    #     stock_sheet = trade_workbook.create_sheet(stock)
    #     setup_columns(stock_sheet)

    # trade_workbook.save("data_dump.xls")

    sql_text = "SELECT * FROM AAPL"
    sql_text += " LIMIT 10"
    cur.execute(sql_text)
    rows = cur.fetchall()

    for row in rows:
        print row

    # time.sleep(outer_repeat_time - ((time.time() - start_time) % outer_repeat_time))

if __name__ == '__main__':
    main_output()
