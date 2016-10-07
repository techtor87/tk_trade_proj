#!/usr/lib/ruby

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

require_relative 'timer'
require_relative 'tk_functions'
require_relative 'spreadsheet_functions'
require 'rubygems'
require 'spreadsheet'

Spreadsheet.client_encoding = 'UTF-8'
tk_data = TK_functions.new
data_store = Spreadsheet::Workbook.new

$commision_flat_rate=4.95
$commision_per_contract=0.65
stock_array = [ "CSCO"]
                # "GE",
                # "AAPL",
                # "BP",
                # "CBI",
                # "DE",
                # "M",
                # "MSFT",
                # "PG",
                # "CRM",
                # "SPY"]

# initialize each worksheet
data_store.create_worksheet :name => "Trade List"
setup_trade_colums(data_store.worksheet("Trade List"))
for stock in stock_array
    data_store.create_worksheet :name => stock.to_s
    setup_columns(data_store.worksheet(stock.to_s))
end

tk_data.refresh_account_data()

# Timer.every 60, 60 do
# 2.times do

    for stock in stock_array
        tk_data.get_search(stock.to_s)
        tk_data.get_quote(stock.to_s)

        fill_row( data_store.worksheet(stock.to_s),
                    tk_data.search[(stock.to_s)],
                    tk_data.quote.bid,
                    tk_data.quote.ask)

        find_profitable_trades(data_store.worksheet("Trade List"),
                    data_store.worksheet(stock.to_s),
                    tk_data.search[(stock.to_s)],
                    tk_data.quote.bid,
                    tk_data.quote.ask)

        puts "done #{stock}"
    end

    data_store.write "data_dump.xls"

    puts "done loop"
# end

tk_data = nil
data_store = nil
# data_store.write "data_dump.xls"

puts "done everything"
