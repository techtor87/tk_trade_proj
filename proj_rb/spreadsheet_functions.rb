#!/usr/lib/ruby

# Use the OAuth gem
require 'rubygems'
require 'spreadsheet'
require_relative 'tk_functions'
require_relative 'trading_stratigies'

def setup_columns( _worksheet )
    _worksheet[0, 0]  = 'Cur Bid'
    _worksheet[0, 1]  = 'Cur Ask'
    _worksheet[0, 2]  = 'strikeprice'
    _worksheet[0, 3]  = 'xdate'
    _worksheet[0, 4]  = 'days_to_expir'

    _worksheet[0, 6]  = 'bid'
    _worksheet[0, 7]  = 'ask'
    _worksheet[0, 8]  = 'contract_size'
    _worksheet[0, 9]  = 'p/c'
    _worksheet[0, 10] = 'symbol'
    _worksheet[0, 11] = 'imp_volatility'
    _worksheet[0, 12] = 'delta'
    _worksheet[0, 13] = 'gamma'
    _worksheet[0, 14] = 'theta'
    _worksheet[0, 15] = 'vega'
    _worksheet[0, 16] = 'rho'
    _worksheet[0, 17] = 'openinterest'

    _worksheet[0, 19] = 'bid'
    _worksheet[0, 20] = 'ask'
    _worksheet[0, 21] = 'contract_size'
    _worksheet[0, 22] = 'p/c'
    _worksheet[0, 23] = 'symbol'
    _worksheet[0, 24] = 'imp_volatility'
    _worksheet[0, 25] = 'delta'
    _worksheet[0, 26] = 'gamma'
    _worksheet[0, 27] = 'theta'
    _worksheet[0, 28] = 'vega'
    _worksheet[0, 29] = 'rho'
    _worksheet[0, 30] = 'openinterest'
end

def setup_trade_colums( _tradesheet )
    _tradesheet[0, 0] = 'Trade Type'
    _tradesheet[0, 1] = 'Bid'
    _tradesheet[0, 2] = 'Ask'
    _tradesheet[0, 3] = 'Trade Profit'
    last_column = 4
    4.times do
        _tradesheet[0, last_column+1] = 'put_call'
        _tradesheet[0, last_column+2] = 'rootsymbol'
        _tradesheet[0, last_column+3] = 'strikeprice'
        _tradesheet[0, last_column+4] = 'xdate'
        _tradesheet[0, last_column+5] = 'ask'
        _tradesheet[0, last_column+6] = 'ask_time'
        _tradesheet[0, last_column+7] = 'asksz'
        _tradesheet[0, last_column+8] = 'basis'
        _tradesheet[0, last_column+9] = 'bid'
        _tradesheet[0, last_column+10] = 'bid_time'
        _tradesheet[0, last_column+11] = 'bidsz'
        _tradesheet[0, last_column+12] = 'chg'
        _tradesheet[0, last_column+13] = 'chg_sign'
        _tradesheet[0, last_column+14] = 'chg_t'
        _tradesheet[0, last_column+15] = 'cl'
        _tradesheet[0, last_column+16] = 'days_to_expiration'
        _tradesheet[0, last_column+17] = 'exch'
        _tradesheet[0, last_column+18] = 'exch_desc'
        _tradesheet[0, last_column+19] = 'hi'
        _tradesheet[0, last_column+20] = 'incr_vl'
        _tradesheet[0, last_column+21] = 'issue_desc'
        _tradesheet[0, last_column+22] = 'last'
        _tradesheet[0, last_column+23] = 'lo'
        _tradesheet[0, last_column+24] = 'op_delivery'
        _tradesheet[0, last_column+25] = 'op_flag'
        _tradesheet[0, last_column+26] = 'op_style'
        _tradesheet[0, last_column+27] = 'op_subclass'
        _tradesheet[0, last_column+28] = 'opn'
        _tradesheet[0, last_column+29] = 'pchg'
        _tradesheet[0, last_column+30] = 'pchg_sign'
        _tradesheet[0, last_column+31] = 'pcls'
        _tradesheet[0, last_column+32] = 'phi'
        _tradesheet[0, last_column+33] = 'plo'
        _tradesheet[0, last_column+34] = 'popn'
        _tradesheet[0, last_column+35] = 'pr_date'
        _tradesheet[0, last_column+36] = 'pr_openinterest'
        _tradesheet[0, last_column+37] = 'prchg'
        _tradesheet[0, last_column+38] = 'prem_mult'
        _tradesheet[0, last_column+39] = 'pvol'
        _tradesheet[0, last_column+40] = 'secclass'
        _tradesheet[0, last_column+41] = 'sesn'
        _tradesheet[0, last_column+42] = 'symbol'
        _tradesheet[0, last_column+43] = 'tcond'
        _tradesheet[0, last_column+44] = 'timestamp'
        _tradesheet[0, last_column+45] = 'tr_num'
        _tradesheet[0, last_column+46] = 'tradetick'
        _tradesheet[0, last_column+47] = 'under_cusip'
        _tradesheet[0, last_column+48] = 'vl'
        _tradesheet[0, last_column+49] = 'vwap'
        _tradesheet[0, last_column+50] = 'wk52hi'
        _tradesheet[0, last_column+51] = 'wk52hidate'
        _tradesheet[0, last_column+52] = 'wk52lo'
        _tradesheet[0, last_column+53] = 'wk52lodate'
        _tradesheet[0, last_column+54] = 'imp_volatility'
        _tradesheet[0, last_column+55] = 'idelta'
        _tradesheet[0, last_column+56] = 'igamma'
        _tradesheet[0, last_column+57] = 'itheta'
        _tradesheet[0, last_column+58] = 'ivega'
        _tradesheet[0, last_column+59] = 'irho'
        _tradesheet[0, last_column+60] = 'openinterest'
        last_column = last_column + 61
    end
end

def fill_row( _worksheet, _data, _bid, _ask )
    new_row_index = _worksheet.last_row_index
    if( ! _data.search_quote.empty? )
        for quote in _data.search_quote.sort_by { |a| [ a.xdate, a.strikeprice, a.put_call ] }
            if quote.put_call == "call"
            then
                if ( ( _worksheet[new_row_index, 2] != quote.strikeprice ) ) # && !_worksheet[new_row_index, 2].to_s.empty?
                then
                    new_row_index += 1

                    _worksheet[new_row_index,  0] = _bid
                    _worksheet[new_row_index,  1] = _ask
                    _worksheet[new_row_index,  2] = quote.strikeprice
                    _worksheet[new_row_index,  3] = quote.xdate
                    _worksheet[new_row_index,  4] = quote.days_to_expiration
                end
                # Call

                _worksheet[new_row_index,  6] = quote.bid
                _worksheet[new_row_index,  7] = quote.ask
                _worksheet[new_row_index,  8] = quote.contract_size
                _worksheet[new_row_index,  9] = quote.put_call
                _worksheet[new_row_index,  10] = quote.symbol
                _worksheet[new_row_index,  11] = quote.imp_volatility
                _worksheet[new_row_index,  12] = quote.idelta
                _worksheet[new_row_index,  13] = quote.igamma
                _worksheet[new_row_index,  14] = quote.itheta
                _worksheet[new_row_index,  15] = quote.ivega
                _worksheet[new_row_index,  16] = quote.irho
                _worksheet[new_row_index,  17] = quote.openinterest
            elsif quote.put_call == "put"
            then
                if ( ( _worksheet[new_row_index, 2] != quote.strikeprice ) ) # && !_worksheet[new_row_index, 2].to_s.empty?
                then
                    new_row_index += 1

                    _worksheet[new_row_index,  0] = _bid
                    _worksheet[new_row_index,  1] = _ask
                    _worksheet[new_row_index,  2] = quote.strikeprice
                    _worksheet[new_row_index,  3] = quote.xdate
                    _worksheet[new_row_index,  4] = quote.days_to_expiration
                end

                # Puts
                _worksheet[new_row_index,  19] = quote.bid
                _worksheet[new_row_index,  20] = quote.ask
                _worksheet[new_row_index,  21] = quote.contract_size
                _worksheet[new_row_index,  22] = quote.put_call
                _worksheet[new_row_index,  23] = quote.symbol
                _worksheet[new_row_index,  24] = quote.imp_volatility
                _worksheet[new_row_index,  25] = quote.idelta
                _worksheet[new_row_index,  26] = quote.igamma
                _worksheet[new_row_index,  27] = quote.itheta
                _worksheet[new_row_index,  28] = quote.ivega
                _worksheet[new_row_index,  29] = quote.irho
                _worksheet[new_row_index,  30] = quote.openinterest

                # new_row_index += 1
            end
        end
    end
end

def print_trades( _tradesheet, _bid, _ask, _type, _profit, *_opts )
    new_row_index = _tradesheet.last_row_index + 1
    _tradesheet[new_row_index, 0] = _type
    _tradesheet[new_row_index, 1] = _bid
    _tradesheet[new_row_index, 2] = _ask
    _tradesheet[new_row_index, 3] = _profit
    last_column = 4
    for opt in _opts
        _tradesheet[new_row_index, last_column+1] = opt.put_call
        _tradesheet[new_row_index, last_column+2] = opt.rootsymbol
        _tradesheet[new_row_index, last_column+3] = opt.strikeprice
        _tradesheet[new_row_index, last_column+4] = opt.xdate
        _tradesheet[new_row_index, last_column+5] = opt.ask
        _tradesheet[new_row_index, last_column+6] = opt.ask_time
        _tradesheet[new_row_index, last_column+7] = opt.asksz
        _tradesheet[new_row_index, last_column+8] = opt.basis
        _tradesheet[new_row_index, last_column+9] = opt.bid
        _tradesheet[new_row_index, last_column+10] = opt.bid_time
        _tradesheet[new_row_index, last_column+11] = opt.bidsz
        _tradesheet[new_row_index, last_column+12] = opt.chg
        _tradesheet[new_row_index, last_column+13] = opt.chg_sign
        _tradesheet[new_row_index, last_column+14] = opt.chg_t
        _tradesheet[new_row_index, last_column+15] = opt.cl
        _tradesheet[new_row_index, last_column+16] = opt.days_to_expiration
        _tradesheet[new_row_index, last_column+17] = opt.exch
        _tradesheet[new_row_index, last_column+18] = opt.exch_desc
        _tradesheet[new_row_index, last_column+19] = opt.hi
        _tradesheet[new_row_index, last_column+20] = opt.incr_vl
        _tradesheet[new_row_index, last_column+21] = opt.issue_desc
        _tradesheet[new_row_index, last_column+22] = opt.last
        _tradesheet[new_row_index, last_column+23] = opt.lo
        _tradesheet[new_row_index, last_column+24] = opt.op_delivery
        _tradesheet[new_row_index, last_column+25] = opt.op_flag
        _tradesheet[new_row_index, last_column+26] = opt.op_style
        _tradesheet[new_row_index, last_column+27] = opt.op_subclass
        _tradesheet[new_row_index, last_column+28] = opt.opn
        _tradesheet[new_row_index, last_column+29] = opt.pchg
        _tradesheet[new_row_index, last_column+30] = opt.pchg_sign
        _tradesheet[new_row_index, last_column+31] = opt.pcls
        _tradesheet[new_row_index, last_column+32] = opt.phi
        _tradesheet[new_row_index, last_column+33] = opt.plo
        _tradesheet[new_row_index, last_column+34] = opt.popn
        _tradesheet[new_row_index, last_column+35] = opt.pr_date
        _tradesheet[new_row_index, last_column+36] = opt.pr_openinterest
        _tradesheet[new_row_index, last_column+37] = opt.prchg
        _tradesheet[new_row_index, last_column+38] = opt.prem_mult
        _tradesheet[new_row_index, last_column+39] = opt.pvol
        _tradesheet[new_row_index, last_column+40] = opt.secclass
        _tradesheet[new_row_index, last_column+41] = opt.sesn
        _tradesheet[new_row_index, last_column+42] = opt.symbol
        _tradesheet[new_row_index, last_column+43] = opt.tcond
        _tradesheet[new_row_index, last_column+44] = opt.timestamp
        _tradesheet[new_row_index, last_column+45] = opt.tr_num
        _tradesheet[new_row_index, last_column+46] = opt.tradetick
        _tradesheet[new_row_index, last_column+47] = opt.under_cusip
        _tradesheet[new_row_index, last_column+48] = opt.vl
        _tradesheet[new_row_index, last_column+49] = opt.vwap
        _tradesheet[new_row_index, last_column+50] = opt.wk52hi
        _tradesheet[new_row_index, last_column+51] = opt.wk52hidate
        _tradesheet[new_row_index, last_column+52] = opt.wk52lo
        _tradesheet[new_row_index, last_column+53] = opt.wk52lodate
        _tradesheet[new_row_index, last_column+54] = opt.imp_volatility
        _tradesheet[new_row_index, last_column+55] = opt.idelta
        _tradesheet[new_row_index, last_column+56] = opt.igamma
        _tradesheet[new_row_index, last_column+57] = opt.itheta
        _tradesheet[new_row_index, last_column+58] = opt.ivega
        _tradesheet[new_row_index, last_column+59] = opt.irho
        _tradesheet[new_row_index, last_column+60] = opt.openinterest
        last_column = last_column + 61
    end
end

def find_profitable_trades( _tradesheet, _worksheet, _data, _bid, _ask )
    covered_call( _tradesheet, _worksheet, _data, _bid, _ask )
    iron_condor( _tradesheet, _worksheet, _data, _bid, _ask )
    long_box( _tradesheet, _worksheet, _data, _bid, _ask )
    short_box( _tradesheet, _worksheet, _data, _bid, _ask )
end
