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
    tk_func.refresh_account_data()
    for stock in stock_list:
        tk_func.get_quote(stock)
        # tk_func.get_search(stock)


if __name__ == '__main__':
    main()
