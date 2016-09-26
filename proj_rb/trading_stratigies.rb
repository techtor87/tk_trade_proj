#!/usr/lib/ruby

# Use the OAuth gem
require 'rubygems'
require 'spreadsheet'
require_relative 'tk_functions'

@sucess_percentage=0.75

def covered_call_profit(_bid, _strike_call)
    # if _strike_call.imp_volatility
        # value = _strike_call.strikeprice.to_f - _bid - ($commision_flat_rate - ($commision_per_contract * 1))/100
    # else
    #     value = 0
    # end
end

def iron_condor_profit()

end

def long_box_profit( _low_strike_call, _high_strike_call, _low_strike_put, _high_strike_put )
    bull_call_spread = _low_strike_call.ask.to_f - _high_strike_call.bid.to_f
    bear_put_spread = _high_strike_put.ask.to_f - _high_strike_put.bid.to_f
    total_cost = bull_call_spread + bear_put_spread
    total_value = _high_strike_call.strikeprice.to_f - _low_strike_call.strikeprice.to_f
    return total_value - total_cost - ($commision_flat_rate - ($commision_per_contract * 4))/100
end

def short_box_profit( _low_strike_call, _high_strike_call, _low_strike_put, _high_strike_put )
    bull_call_spread = _low_strike_call.bid.to_f - _high_strike_call.ask.to_f
    bear_put_spread = _high_strike_put.bid.to_f - _high_strike_put.ask.to_f
    total_cost = bull_call_spread + bear_put_spread
    total_value = _high_strike_call.strikeprice.to_f - _low_strike_call.strikeprice.to_f
    return total_value - total_cost - $commision_flat_rate - ($commision_per_contract * 4)
end

def covered_call( _tradesheet, _worksheet, _data, _bid, _ask )
    data_by_date_put = Hash.new{ |hash, key| hash[key] = Array.new;}
    data_by_date_call = Hash.new{ |hash, key| hash[key] = Array.new;}
    for quote in _data.search_quote
        if quote.put_call == "put"
            data_by_date_put[quote.xdate].push( quote )
        elsif quote.put_call == "call"
            data_by_date_call[quote.xdate].push( quote )
        end
    end

    for i in data_by_date_call.keys
        for strike_c in data_by_date_call[i].sort_by{ |a| a.strikeprice }
            if strike_c.strikeprice.to_f > _bid.to_f and
               strike_c.openinterest.to_f > 0
            then
                value =  covered_call_profit(_bid, strike_c)
                if value.to_f > 0
                then
                    # save the trade to the workbook
                    print_trades( _tradesheet, _bid, _ask, "covered call", value, strike_c )
                end
            end
        end
    end
end

def iron_condor( _tradesheet, _worksheet, _data, _bid, _ask )
end

def long_box( _tradesheet, _worksheet, _data, _bid, _ask )

    data_by_date_put = Hash.new{ |hash, key| hash[key] = Array.new;}
    data_by_date_call = Hash.new{ |hash, key| hash[key] = Array.new;}
    for quote in _data.search_quote
        if quote.put_call == "put"
            data_by_date_put[quote.xdate].push( quote )
        elsif quote.put_call == "call"
            data_by_date_call[quote.xdate].push( quote )
        end
    end

    for i in data_by_date_call.keys
        for low_strike_c in data_by_date_call[i].sort_by{ |a| a.strikeprice }
            for high_strike_c in data_by_date_call[i].sort_by{ |a| a.strikeprice }
                for low_strike_p in data_by_date_put[i].sort_by{ |a| a.strikeprice }
                    for high_strike_p in data_by_date_put[i].sort_by{ |a| a.strikeprice }
                        if low_strike_c.strikeprice < high_strike_c.strikeprice and
                            low_strike_c.strikeprice == low_strike_p.strikeprice and
                            high_strike_c.strikeprice == high_strike_p.strikeprice and
                            low_strike_c.openinterest.to_f > 0 and
                            high_strike_c.openinterest.to_f > 0 and
                            low_strike_p.openinterest.to_f > 0 and
                            high_strike_p.openinterest.to_f > 0
                        then
                            value =  long_box_profit(low_strike_c, high_strike_c, low_strike_p, high_strike_p)
                            if value > 0
                            then
                                # save the trade to the workbook
                                print_trades( _tradesheet, _bid, _ask, "long_box", value, low_strike_c, high_strike_c, low_strike_p, high_strike_p )
                            end
                        end
                    end
                end
            end
        end
    end
end

def short_box( _tradesheet, _worksheet, _data, _bid, _ask )

    data_by_date_put = Hash.new{ |hash, key| hash[key] = Array.new;}
    data_by_date_call = Hash.new{ |hash, key| hash[key] = Array.new;}
    for quote in _data.search_quote
        if quote.put_call == "put"
            data_by_date_put[quote.xdate].push( quote )
        elsif quote.put_call == "call"
            data_by_date_call[quote.xdate].push( quote )
        end
    end

    for i in data_by_date_call.keys
        for low_strike_c in data_by_date_call[i].sort_by{ |a| a.strikeprice }
            for high_strike_c in data_by_date_call[i].sort_by{ |a| a.strikeprice }
                for low_strike_p in data_by_date_put[i].sort_by{ |a| a.strikeprice }
                    for high_strike_p in data_by_date_put[i].sort_by{ |a| a.strikeprice }
                        if low_strike_c.strikeprice < high_strike_c.strikeprice and
                            low_strike_c.strikeprice == low_strike_p.strikeprice and
                            high_strike_c.strikeprice == high_strike_p.strikeprice and
                            low_strike_c.openinterest.to_f > 0 and
                            high_strike_c.openinterest.to_f > 0 and
                            low_strike_p.openinterest.to_f > 0 and
                            high_strike_p.openinterest.to_f > 0
                        then
                            value =  short_box_profit(low_strike_c, high_strike_c, low_strike_p, high_strike_p)
                            if value > 0
                            then
                                # save the trade to the workbook
                                print_trades( _tradesheet, "short_box", value, low_strike_c, high_strike_c, low_strike_p, high_strike_p )
                            end
                        end
                    end
                end
            end
        end
    end
end