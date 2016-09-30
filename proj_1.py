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

from tk_functions import *
from spreadsheet_functions import *

commision_flat_rate = 4.95
commision_per_contract = 0.65

stock_list = [ 'AAPL',
               'BP',
               'CBI',
               'DE',
               'M',
               'MSFT',
               'PG',
               'CRM' ]

def main():
    tk_func = TK_functions()

    # initialize workbook
    trade_workbook = pyxl.Workbook()
    trade_sheet = trade_workbook.active
    trade_sheet.title = "Trade List"
    setup_trade_columns( trade_sheet )
    for stock in stock_list:
        stock_sheet = trade_workbook.create_sheet(stock)
        setup_columns(stock_sheet)

    trade_workbook.save("data_dump.xls")

    tk_func.refresh_account_data()

    for stock in stock_list:
        tk_func.get_quote(stock)
        tk_func.get_search(stock)

        # fill_row ( trade_workbook.worksheet[stock],
                   # tk_func.search[stock],
                   # tk_func.quote.bid,
                   # tk_func.quote.ask )

        # find_profitable_trades( trade_sheet,
                                # trade_workbook.worksheet[stock],
                                # tk_func.search[stock],
                                # tk_func.quote.bid,
                                # tk_func.quote.ask )

    trade_workbook.save("data_dump.xls")

if __name__ == '__main__':
    main()
