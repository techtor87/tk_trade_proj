#!/usr/bin/env python

# IRA
# 100 - CSCO
# 210 - GE

#  50 - AAPl
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
from tk_functions import *
from spreadsheet_functions import *

commision_flat_rate = 4.95
commision_per_contract = 0.65

outer_repeat_time = 120.0
inner_repeat_time = 20.0

stock_list = [ 'AAPL',
               # 'BP',
               # 'CBI',
               # 'DE',
               # 'M',
               # 'MSFT',
               # 'PG',
               'CRM' ]

def main():
    tk_func = TK_functions()

    con = lite.connect('trade_test.db')
    with con:
        cur = con.cursor()
        setup_tables(cur, stock_list )

    # initialize workbook
    # trade_workbook = pyxl.Workbook()
    # trade_sheet = trade_workbook.active
    # trade_sheet.title = "Trade List"
    # setup_trade_columns( trade_sheet )
    # for stock in stock_list:
    #     stock_sheet = trade_workbook.create_sheet(stock)
    #     setup_columns(stock_sheet)

    # trade_workbook.save("data_dump.xls")

    # start_time=time.time()
    # while True:

    tk_func.refresh_account_data()

    for stock in stock_list:
        tk_func.get_quote(stock)
        tk_func.get_search(stock)

        # fill_row ( trade_workbook[stock],
        #         tk_func.search.search_quote,
        #         tk_func.quote.bid,
        #         tk_func.quote.ask )

        add_quote(cur,
                  stock,
                  tk_func.search.search_quote,
                  tk_func.quote.bid,
                  tk_func.quote.ask)

        find_profitable_trades( cur,
                                stock,
                                tk_func.search.search_quote,
                                tk_func.quote.bid,
                                tk_func.quote.ask )


        sql_text = "SELECT * FROM " + stock
        sql_text += " LIMIT 10"
        cur.execute(sql_text)
        rows = cur.fetchall()

        # for row in rows:
            # print row

        con.commit()
        print( 'done {} - {}'.format(stock, time.time()))
            # time.sleep(inner_repeat_time - ((time.time() - start_time) % inner_repeat_time))

        # trade_workbook.save("data_dump.xls")
        # time.sleep(outer_repeat_time - ((time.time() - start_time) % outer_repeat_time))

    # sql_text = "SELECT * FROM trades"
    # cur.execute(sql_text)
    # rows = cur.fetchall()

    # for row in rows:
    #     print row
    # trade_workbook.save("data_dump.xls")

if __name__ == '__main__':
    main()
