#!/usr/lib/ruby

require 'rexml/document'
require 'nokogiri'
include REXML

class Account
    def initialize
        @account_num = 0
        @accountval = 0
        @buyingpower = 0
        @fedcall = 0
        @housecall = 0
        @accuredinterest = 0
        @cash = 0
        @cashavail = 0
        @marginbalance = 0
        @mmf = 0
        @total = 0
        @uncleareddeposits = 0
        @unsettledfunds = 0
        @yield = 0
        @longoptions = 0
        @longstocks = 0
        @options = 0
        @shortoptions = 0
        @shortstocks = 0
        @stocks = 0
        @total = 0
        @totalsecurities = 0
    end

    def to_s
        "\n" +
        "account_num = #@account_num\n" +
        "accountval = #@accountval\n" +
        "buyingpower = #@buyingpower\n" +
        "fedcall = #@fedcall\n" +
        "housecall = #@housecall\n" +
        "accuredinterest = #@accuredinterest\n" +
        "cash = #@cash\n" +
        "cashavail = #@cashavail\n" +
        "marginbalance = #@marginbalance\n" +
        "mmf = #@mmf\n" +
        "total = #@total\n" +
        "uncleareddeposits = #@uncleareddeposits\n" +
        "unsettledfunds = #@unsettledfunds\n" +
        "yield = #@yield\n" +
        "longoptions = #@longoptions\n" +
        "longstocks = #@longstocks\n" +
        "options = #@options\n" +
        "shortoptions = #@shortoptions\n" +
        "shortstocks = #@shortstocks\n" +
        "stocks = #@stocks\n" +
        "total = #@total\n" +
        "totalsecurities = #@totalsecurities\n\n"
    end

    def parse ( _data )
        xmldoc = Nokogiri::XML(_data)
        @account_num = xmldoc.css("account").text
        @accountval = xmldoc.css("accountvalue").text
        @buyingpower = xmldoc.css("buyingpower").text
        @fedcall = xmldoc.css("fedcall").text
        @housecall = xmldoc.css("housecall").text
        @accuredinterest = xmldoc.css("accruedinterest").text
        @cash = xmldoc.css("cash").text
        @cashavail = xmldoc.css("cashavailable").text
        @marginbalance = xmldoc.css("marginbalance").text
        @mmf = xmldoc.css("mmf").text
        @total = xmldoc.css("total").text
        @uncleareddeposits = xmldoc.css("uncleareddeposits").text
        @unsettledfunds = xmldoc.css("unsettledfunds").text
        @yield = xmldoc.css("yield").text
        @longoptions = xmldoc.css("longoptions").text
        @longstocks = xmldoc.css("longstocks").text
        @options = xmldoc.css("options").text
        @shortoptions = xmldoc.css("shortoptions").text
        @shortstocks = xmldoc.css("shortstocks").text
        @stocks = xmldoc.css("stocks").text
        @total = xmldoc.css("total").text
        @totalsecurities = xmldoc.css("totalsecurities").text
    end

    attr_accessor :account_num
    attr_accessor :accountval
    attr_accessor :buyingpower
    attr_accessor :fedcall
    attr_accessor :housecall
    attr_accessor :accuredinterest
    attr_accessor :cash
    attr_accessor :cashavail
    attr_accessor :marginbalance
    attr_accessor :mmf
    attr_accessor :total
    attr_accessor :uncleareddeposits
    attr_accessor :unsettledfunds
    attr_accessor :yield
    attr_accessor :longoptions
    attr_accessor :longstocks
    attr_accessor :options
    attr_accessor :shortoptions
    attr_accessor :shortstocks
    attr_accessor :stocks
    attr_accessor :total
    attr_accessor :totalsecurities
end

class Quote
    def initialize
        @adp_100 = 0
        @adp_200 = 0
        @adp_50 = 0
        @adv_21 = 0
        @adv_30 = 0
        @adv_90 = 0
        @ask = 0
        @ask_time = 0
        @asksz = 0
        @basis = 0
        @beta = 0
        @bid = 0
        @bid_time = 0
        @bidsz = 0
        @bidtick = 0
        @chg = 0
        @chg_sign = 0
        @chg_t = 0
        @cl = 0
        @contract_size = 0
        @cusip = 0
        @date = 0
        @datetime = 0
        @days_to_expiration = 0
        @div = 0
        @divexdate = 0
        @divfreq = 0
        @divpaydt = 0
        @dollar_value = 0
        @eps = 0
        @exch = 0
        @exch_desc = 0
        @hi = 0
        @iad = 0
        @idelta = 0
        @igamma = 0
        @imp_volatility = 0
        @incr_vl = 0
        @irho = 0
        @issue_desc = 0
        @itheta = 0
        @ivega = 0
        @last = 0
        @lo = 0
        @name = 0
        @op_delivery = 0
        @op_flag = 0
        @op_style = 0
        @op_subclass = 0
        @openinterest = 0
        @opn = 0
        @opt_val = 0
        @pchg = 0
        @pchg_sign = 0
        @pcls = 0
        @pe = 0
        @phi = 0
        @plo = 0
        @popn = 0
        @pr_adp_100 = 0
        @pr_adp_200 = 0
        @pr_adp_50 = 0
        @pr_date = 0
        @pr_openinterest = 0
        @prbook = 0
        @prchg = 0
        @prem_mult = 0
        @put_call = 0
        @pvol = 0
        @qcond = 0
        @rootsymbol = 0
        @secclass = 0
        @sesn = 0
        @sho = 0
        @strikeprice = 0
        @symbol = 0
        @tcond = 0
        @timestamp = 0
        @tr_num = 0
        @tradetick = 0
        @trend = 0
        @under_cusip = 0
        @undersymbol = 0
        @vl = 0
        @volatility12 = 0
        @vwap = 0
        @wk52hi = 0
        @wk52hidate = 0
        @wk52lo = 0
        @wk52lodate = 0
        @xdate = 0
        @xday = 0
        @xmonth = 0
        @xyear = 0
        @yield = 0
    end

    def to_s
        "\n" +
        "adp_100 = #@adp_100\n" +
        "adp_200 = #@adp_200\n" +
        "adp_50 = #@adp_50\n" +
        "adv_21 = #@adv_21\n" +
        "adv_30 = #@adv_30\n" +
        "adv_90 = #@adv_90\n" +
        "ask = #@ask\n" +
        "ask_time = #@ask_time\n" +
        "asksz = #@asksz\n" +
        "basis = #@basis\n" +
        "beta = #@beta\n" +
        "bid = #@bid\n" +
        "bid_time = #@bid_time\n" +
        "bidsz = #@bidsz\n" +
        "bidtick = #@bidtick\n" +
        "chg = #@chg\n" +
        "chg_sign = #@chg_sign\n" +
        "chg_t = #@chg_t\n" +
        "cl = #@cl\n" +
        "contract_size = #@contract_size\n" +
        "cusip = #@cusip\n" +
        "date = #@date\n" +
        "datetime = #@datetime\n" +
        "days_to_expiration = #@days_to_expiration\n" +
        "div = #@div\n" +
        "divexdate = #@divexdate\n" +
        "divfreq = #@divfreq\n" +
        "divpaydt = #@divpaydt\n" +
        "dollar_value = #@dollar_value\n" +
        "eps = #@eps\n" +
        "exch = #@exch\n" +
        "exch_desc = #@exch_desc\n" +
        "hi = #@hi\n" +
        "iad = #@iad\n" +
        "idelta = #@idelta\n" +
        "igamma = #@igamma\n" +
        "imp_volatility = #@imp_volatility\n" +
        "incr_vl = #@incr_vl\n" +
        "irho = #@irho\n" +
        "issue_desc = #@issue_desc\n" +
        "itheta = #@itheta\n" +
        "ivega = #@ivega\n" +
        "last = #@last\n" +
        "lo = #@lo\n" +
        "name = #@name\n" +
        "op_delivery = #@op_delivery\n" +
        "op_flag = #@op_flag\n" +
        "op_style = #@op_style\n" +
        "op_subclass = #@op_subclass\n" +
        "openinterest = #@openinterest\n" +
        "opn = #@opn\n" +
        "opt_val = #@opt_val\n" +
        "pchg = #@pchg\n" +
        "pchg_sign = #@pchg_sign\n" +
        "pcls = #@pcls\n" +
        "pe = #@pe\n" +
        "phi = #@phi\n" +
        "plo = #@plo\n" +
        "popn = #@popn\n" +
        "pr_adp_100 = #@pr_adp_100\n" +
        "pr_adp_200 = #@pr_adp_200\n" +
        "pr_adp_50 = #@pr_adp_50\n" +
        "pr_date = #@pr_date\n" +
        "pr_openinterest = #@pr_openinterest\n" +
        "prbook = #@prbook\n" +
        "prchg = #@prchg\n" +
        "prem_mult = #@prem_mult\n" +
        "put_call = #@put_call\n" +
        "pvol = #@pvol\n" +
        "qcond = #@qcond\n" +
        "rootsymbol = #@rootsymbol\n" +
        "secclass = #@secclass\n" +
        "sesn = #@sesn\n" +
        "sho = #@sho\n" +
        "strikeprice = #@strikeprice\n" +
        "symbol = #@symbol\n" +
        "tcond = #@tcond\n" +
        "timestamp = #@timestamp\n" +
        "tr_num = #@tr_num\n" +
        "tradetick = #@tradetick\n" +
        "trend = #@trend\n" +
        "under_cusip = #@under_cusip\n" +
        "undersymbol = #@undersymbol\n" +
        "vl = #@vl\n" +
        "volatility12 = #@volatility12\n" +
        "vwap = #@vwap\n" +
        "wk52hi = #@wk52hi\n" +
        "wk52hidate = #@wk52hidate\n" +
        "wk52lo = #@wk52lo\n" +
        "wk52lodate = #@wk52lodate\n" +
        "xdate = #@xdate\n" +
        "xday = #@xday\n" +
        "xmonth = #@xmonth\n" +
        "xyear = #@xyear\n" +
        "yield = #@yield\n\n"
    end

    def parse ( _data )
        xmldoc = Nokogiri::XML(_data)
        @adp_100 = xmldoc.css("adp_100").text
        @adp_200 = xmldoc.css("adp_200").text
        @adp_50 = xmldoc.css("adp_50").text
        @adv_21 = xmldoc.css("adv_21").text
        @adv_30 = xmldoc.css("adv_30").text
        @adv_90 = xmldoc.css("adv_90").text
        @ask = xmldoc.css("ask").text
        @ask_time = xmldoc.css("ask_time").text
        @asksz = xmldoc.css("asksz").text
        @basis = xmldoc.css("basis").text
        @beta = xmldoc.css("beta").text
        @bid = xmldoc.css("bid").text
        @bidsz = xmldoc.css("bidsz").text
        @bidtick = xmldoc.css("bidtick").text
        @chg = xmldoc.css("chg").text
        @chg_sign = xmldoc.css("chg_sign").text
        @chg_t = xmldoc.css("chg_t").text
        @cl = xmldoc.css("cl").text
        @contract_size = xmldoc.css("contract_size").text
        @cusip = xmldoc.css("cusip").text
        @date = xmldoc.css("date").text
        @datetime = xmldoc.css("datetime").text
        @days_to_expiration = xmldoc.css("days_to_expiration").text
        @div = xmldoc.css("div").text
        @divexdate = xmldoc.css("divexdate").text
        @divfreq = xmldoc.css("divfreq").text
        @divpaydt = xmldoc.css("divpaydt").text
        @dollar_value = xmldoc.css("dollar_value").text
        @eps = xmldoc.css("eps").text
        @exch = xmldoc.css("exch").text
        @exch_desc = xmldoc.css("exch_desc").text
        @hi = xmldoc.css("hi").text
        @iad = xmldoc.css("iad").text
        @idelta = xmldoc.css("idelta").text
        @igamma = xmldoc.css("igamma").text
        @imp_volatility = xmldoc.css("imp_volatility").text
        @incr_vl = xmldoc.css("incr_vl").text
        @irho = xmldoc.css("irho").text
        @issue_desc = xmldoc.css("issue_desc").text
        @itheta = xmldoc.css("itheta").text
        @ivega = xmldoc.css("ivega").text
        @last = xmldoc.css("last").text
        @lo = xmldoc.css("lo").text
        @name = xmldoc.css("name").text
        @op_delivery = xmldoc.css("op_delivery").text
        @op_flag = xmldoc.css("op_flag").text
        @op_style = xmldoc.css("op_style").text
        @op_subclass = xmldoc.css("op_subclass").text
        @openinterest = xmldoc.css("openinterest").text
        @opn = xmldoc.css("opn").text
        @opt_val = xmldoc.css("opt_val").text
        @pchg = xmldoc.css("pchg").text
        @pchg_sign = xmldoc.css("pchg_sign").text
        @pcls = xmldoc.css("pcls").text
        @pe = xmldoc.css("pe").text
        @phi = xmldoc.css("phi").text
        @plo = xmldoc.css("plo").text
        @popn = xmldoc.css("popn").text
        @pr_adp_100 = xmldoc.css("pr_adp_100").text
        @pr_adp_200 = xmldoc.css("pr_adp_200").text
        @pr_adp_50 = xmldoc.css("pr_adp_50").text
        @pr_date = xmldoc.css("pr_date").text
        @pr_openinterest = xmldoc.css("pr_openinterest").text
        @prbook = xmldoc.css("prbook").text
        @prchg = xmldoc.css("prchg").text
        @prem_mult = xmldoc.css("prem_mult").text
        @put_call = xmldoc.css("put_call").text
        @pvol = xmldoc.css("pvol").text
        @qcond = xmldoc.css("qcond").text
        @rootsymbol = xmldoc.css("rootsymbol").text
        @secclass = xmldoc.css("secclass").text
        @sesn = xmldoc.css("sesn").text
        @sho = xmldoc.css("sho").text
        @strikeprice = xmldoc.css("strikeprice").text
        @symbol = xmldoc.css("symbol").text
        @tcond = xmldoc.css("tcond").text
        @timestamp = xmldoc.css("timestamp").text
        @tr_num = xmldoc.css("tr_num").text
        @tradetick = xmldoc.css("tradetick").text
        @trend = xmldoc.css("trend").text
        @under_cusip = xmldoc.css("under_cusip").text
        @undersymbol = xmldoc.css("undersymbol").text
        @vl = xmldoc.css("vl").text
        @volatility12 = xmldoc.css("volatility12").text
        @vwap = xmldoc.css("vwap").text
        @wk52hi = xmldoc.css("wk52hi").text
        @wk52hidate = xmldoc.css("wk52hidate").text
        @wk52lo = xmldoc.css("wk52lo").text
        @wk52lodate = xmldoc.css("wk52lodate").text
        @xdate = xmldoc.css("xdate").text
        @xday = xmldoc.css("xday").text
        @xmonth = xmldoc.css("xmonth").text
        @xyear = xmldoc.css("xyear").text
        @yield = xmldoc.css("yield").text
    end

    attr_accessor :adp_100
    attr_accessor :adp_200
    attr_accessor :adp_50
    attr_accessor :adv_21
    attr_accessor :adv_30
    attr_accessor :adv_90
    attr_accessor :ask
    attr_accessor :ask_time
    attr_accessor :asksz
    attr_accessor :basis
    attr_accessor :beta
    attr_accessor :bid
    attr_accessor :bid_time
    attr_accessor :bidsz
    attr_accessor :bidtick
    attr_accessor :chg
    attr_accessor :chg_sign
    attr_accessor :chg_t
    attr_accessor :cl
    attr_accessor :contract_size
    attr_accessor :cusip
    attr_accessor :date
    attr_accessor :datetime
    attr_accessor :days_to_expiration
    attr_accessor :div
    attr_accessor :divexdate
    attr_accessor :divfreq
    attr_accessor :divpaydt
    attr_accessor :dollar_value
    attr_accessor :eps
    attr_accessor :exch
    attr_accessor :exch_desc
    attr_accessor :hi
    attr_accessor :iad
    attr_accessor :idelta
    attr_accessor :igamma
    attr_accessor :imp_volatility
    attr_accessor :incr_vl
    attr_accessor :irho
    attr_accessor :issue_desc
    attr_accessor :itheta
    attr_accessor :ivega
    attr_accessor :last
    attr_accessor :lo
    attr_accessor :name
    attr_accessor :op_delivery
    attr_accessor :op_flag
    attr_accessor :op_style
    attr_accessor :op_subclass
    attr_accessor :openinterest
    attr_accessor :opn
    attr_accessor :opt_val
    attr_accessor :pchg
    attr_accessor :pchg_sign
    attr_accessor :pcls
    attr_accessor :pe
    attr_accessor :phi
    attr_accessor :plo
    attr_accessor :popn
    attr_accessor :pr_adp_100
    attr_accessor :pr_adp_200
    attr_accessor :pr_adp_50
    attr_accessor :pr_date
    attr_accessor :pr_openinterest
    attr_accessor :prbook
    attr_accessor :prchg
    attr_accessor :prem_mult
    attr_accessor :put_call
    attr_accessor :pvol
    attr_accessor :qcond
    attr_accessor :rootsymbol
    attr_accessor :secclass
    attr_accessor :sesn
    attr_accessor :sho
    attr_accessor :strikeprice
    attr_accessor :symbol
    attr_accessor :tcond
    attr_accessor :timestamp
    attr_accessor :tr_num
    attr_accessor :tradetick
    attr_accessor :trend
    attr_accessor :under_cusip
    attr_accessor :undersymbol
    attr_accessor :vl
    attr_accessor :volatility12
    attr_accessor :vwap
    attr_accessor :wk52hi
    attr_accessor :wk52hidate
    attr_accessor :wk52lo
    attr_accessor :wk52lodate
    attr_accessor :xdate
    attr_accessor :xday
    attr_accessor :xmonth
    attr_accessor :xyear
    attr_accessor :yield
end

class Search_quote
    def initialize
        @ask = 0
        @ask_time = 0
        @asksz = 0
        @basis = 0
        @bid = 0
        @bid_time = 0
        @bidsz = 0
        @chg = 0
        @chg_sign = 0
        @chg_t = 0
        @cl = 0
        @contract_size = 0
        @date = 0
        @datetime = 0
        @days_to_expiration = 0
        @exch = 0
        @exch_desc = 0
        @hi = 0
        @incr_vl = 0
        @issue_desc = 0
        @last = 0
        @lo = 0
        @op_delivery = 0
        @op_flag = 0
        @op_style = 0
        @op_subclass = 0
        @opn = 0
        @pchg = 0
        @pchg_sign = 0
        @pcls = 0
        @phi = 0
        @plo = 0
        @popn = 0
        @pr_date = 0
        @pr_openinterest = 0
        @prchg = 0
        @prem_mult = 0
        @put_call = 0
        @pvol = 0
        @rootsymbol = 0
        @secclass = 0
        @sesn = 0
        @strikeprice = 0
        @symbol = 0
        @tcond = 0
        @timestamp = 0
        @tr_num = 0
        @tradetick = 0
        @under_cusip = 0
        @undersymbol = 0
        @vl = 0
        @vwap = 0
        @wk52hi = 0
        @wk52hidate = 0
        @wk52lo = 0
        @wk52lodate = 0
        @xdate = 0
        @xday = 0
        @xmonth = 0
        @xyear = 0
        @imp_volatility = 0
        @idelta = 0
        @igamma = 0
        @itheta = 0
        @ivega = 0
        @irho = 0
        @openinterest = 0
    end

    def to_s
        "\n" +
        "ask = #@ask\n" +
        "ask_time = #@ask_time\n" +
        "asksz = #@asksz\n" +
        "basis = #@basis\n" +
        "bid = #@bid\n" +
        "bid_time = #@bid_time\n" +
        "bidsz = #@bidsz\n" +
        "chg = #@chg\n" +
        "chg_sign = #@chg_sign\n" +
        "chg_t = #@chg_t\n" +
        "cl = #@cl\n" +
        "contract_size = #@contract_size\n" +
        "date = #@date\n" +
        "datetime = #@datetime\n" +
        "days_to_expiration = #@days_to_expiration\n" +
        "exch = #@exch\n" +
        "exch_desc = #@exch_desc\n" +
        "hi = #@hi\n" +
        "incr_vl = #@incr_vl\n" +
        "issue_desc = #@issue_desc\n" +
        "last = #@last\n" +
        "lo = #@lo\n" +
        "op_delivery = #@op_delivery\n" +
        "op_flag = #@op_flag\n" +
        "op_style = #@op_style\n" +
        "op_subclass = #@op_subclass\n" +
        "opn = #@opn\n" +
        "pchg = #@pchg\n" +
        "pchg_sign = #@pchg_sign\n" +
        "pcls = #@pcls\n" +
        "phi = #@phi\n" +
        "plo = #@plo\n" +
        "popn = #@popn\n" +
        "pr_date = #@pr_date\n" +
        "pr_openinterest = #@pr_openinterest\n" +
        "prchg = #@prchg\n" +
        "prem_mult = #@prem_mult\n" +
        "put_call = #@put_call\n" +
        "pvol = #@pvol\n" +
        "rootsymbol = #@rootsymbol\n" +
        "secclass = #@secclass\n" +
        "sesn = #@sesn\n" +
        "strikeprice = #@strikeprice\n" +
        "symbol = #@symbol\n" +
        "tcond = #@tcond\n" +
        "timestamp = #@timestamp\n" +
        "tr_num = #@tr_num\n" +
        "tradetick = #@tradetick\n" +
        "under_cusip = #@under_cusip\n" +
        "undersymbol = #@undersymbol\n" +
        "vl = #@vl\n" +
        "vwap = #@vwap\n" +
        "wk52hi = #@wk52hi\n" +
        "wk52hidate = #@wk52hidate\n" +
        "wk52lo = #@wk52lo\n" +
        "wk52lodate = #@wk52lodate\n" +
        "xdate = #@xdate\n" +
        "xday = #@xday\n" +
        "xmonth = #@xmonth\n" +
        "xyear = #@xyear\n" +
        "imp_volatility = #@imp_volatility\n" +
        "idelta = #@idelta\n" +
        "igamma = #@igamma\n" +
        "itheta = #@itheta\n" +
        "ivega = #@ivega\n" +
        "irho = #@irho\n" +
        "openinterest = #@openinterest\n\n"
    end

    def parse ( xmldoc )
        # xmldoc = Nokogiri::XML(_data)
        @ask = xmldoc.css("ask").text
        @ask_time = xmldoc.css("ask_time").text
        @asksz = xmldoc.css("asksz").text
        @basis = xmldoc.css("basis").text
        @bid = xmldoc.css("bid").text
        @bid_time = xmldoc.css("bid_time").text
        @bidsz = xmldoc.css("bidsz").text
        @chg = xmldoc.css("chg").text
        @chg_sign = xmldoc.css("chg_sign").text
        @chg_t = xmldoc.css("chg_t").text
        @cl = xmldoc.css("cl").text
        @contract_size = xmldoc.css("contract_size").text
        @date = xmldoc.css("date").text
        @datetime = xmldoc.css("datetime").text
        @days_to_expiration = xmldoc.css("days_to_expiration").text
        @exch = xmldoc.css("exch").text
        @exch_desc = xmldoc.css("exch_desc").text
        @hi = xmldoc.css("hi").text
        @incr_vl = xmldoc.css("incr_vl").text
        @issue_desc = xmldoc.css("issue_desc").text
        @last = xmldoc.css("last").text
        @lo = xmldoc.css("lo").text
        @op_delivery = xmldoc.css("op_delivery").text
        @op_flag = xmldoc.css("op_flag").text
        @op_style = xmldoc.css("op_style").text
        @op_subclass = xmldoc.css("op_subclass").text
        @opn = xmldoc.css("opn").text
        @pchg = xmldoc.css("pchg").text
        @pchg_sign = xmldoc.css("pchg_sign").text
        @pcls = xmldoc.css("pcls").text
        @phi = xmldoc.css("phi").text
        @plo = xmldoc.css("plo").text
        @popn = xmldoc.css("popn").text
        @pr_date = xmldoc.css("pr_date").text
        @pr_openinterest = xmldoc.css("pr_openinterest").text
        @prchg = xmldoc.css("prchg").text
        @prem_mult = xmldoc.css("prem_mult").text
        @put_call = xmldoc.css("put_call").text
        @pvol = xmldoc.css("pvol").text
        @rootsymbol = xmldoc.css("rootsymbol").text
        @secclass = xmldoc.css("secclass").text
        @sesn = xmldoc.css("sesn").text
        @strikeprice = xmldoc.css("strikeprice").text
        @symbol = xmldoc.css("symbol").text
        @tcond = xmldoc.css("tcond").text
        @timestamp = xmldoc.css("timestamp").text
        @tr_num = xmldoc.css("tr_num").text
        @tradetick = xmldoc.css("tradetick").text
        @under_cusip = xmldoc.css("under_cusip").text
        @undersymbol = xmldoc.css("undersymbol").text
        @vl = xmldoc.css("vl").text
        @vwap = xmldoc.css("vwap").text
        @wk52hi = xmldoc.css("wk52hi").text
        @wk52hidate = xmldoc.css("wk52hidate").text
        @wk52lo = xmldoc.css("wk52lo").text
        @wk52lodate = xmldoc.css("wk52lodate").text
        @xdate = xmldoc.css("xdate").text
        @xday = xmldoc.css("xday").text
        @xmonth = xmldoc.css("xmonth").text
        @xyear = xmldoc.css("xyear").text
        @imp_volatility = xmldoc.css("imp_volatility").text
        @idelta = xmldoc.css("idelta").text
        @igamma = xmldoc.css("igamma").text
        @itheta = xmldoc.css("itheta").text
        @ivega = xmldoc.css("ivega").text
        @irho = xmldoc.css("irho").text
        @openinterest = xmldoc.css("openinterest").text
    end

    attr_accessor :ask
    attr_accessor :ask_time
    attr_accessor :asksz
    attr_accessor :basis
    attr_accessor :bid
    attr_accessor :bid_time
    attr_accessor :bidsz
    attr_accessor :chg
    attr_accessor :chg_sign
    attr_accessor :chg_t
    attr_accessor :cl
    attr_accessor :contract_size
    attr_accessor :date
    attr_accessor :datetime
    attr_accessor :days_to_expiration
    attr_accessor :exch
    attr_accessor :exch_desc
    attr_accessor :hi
    attr_accessor :incr_vl
    attr_accessor :issue_desc
    attr_accessor :last
    attr_accessor :lo
    attr_accessor :op_delivery
    attr_accessor :op_flag
    attr_accessor :op_style
    attr_accessor :op_subclass
    attr_accessor :opn
    attr_accessor :pchg
    attr_accessor :pchg_sign
    attr_accessor :pcls
    attr_accessor :phi
    attr_accessor :plo
    attr_accessor :popn
    attr_accessor :pr_date
    attr_accessor :pr_openinterest
    attr_accessor :prchg
    attr_accessor :prem_mult
    attr_accessor :put_call
    attr_accessor :pvol
    attr_accessor :rootsymbol
    attr_accessor :secclass
    attr_accessor :sesn
    attr_accessor :strikeprice
    attr_accessor :symbol
    attr_accessor :tcond
    attr_accessor :timestamp
    attr_accessor :tr_num
    attr_accessor :tradetick
    attr_accessor :under_cusip
    attr_accessor :undersymbol
    attr_accessor :vl
    attr_accessor :vwap
    attr_accessor :wk52hi
    attr_accessor :wk52hidate
    attr_accessor :wk52lo
    attr_accessor :wk52lodate
    attr_accessor :xdate
    attr_accessor :xday
    attr_accessor :xmonth
    attr_accessor :xyear
    attr_accessor :imp_volatility
    attr_accessor :idelta
    attr_accessor :igamma
    attr_accessor :itheta
    attr_accessor :ivega
    attr_accessor :irho
    attr_accessor :openinterest
end

class Search
    def initialize
        @search_quote = Array.new
    end

    def parse ( _data )
        xmldoc = Nokogiri::XML(_data)

        for quote in xmldoc.css("quote")
            temp_search_quote = Search_quote.new
            temp_search_quote.parse(quote)

            @search_quote << temp_search_quote
        end
    end

    def print_each( *args )
        if args.length > 1
            for quote in @search_quote
                for arg in args
                    case arg
                        when "all" then puts quote
                        when "ask" then puts quote.ask
                        when "ask_time" then puts quote.ask_time
                        when "asksz" then puts quote.asksz
                        when "basis" then puts quote.basis
                        when "bid" then puts quote.bid
                        when "bid_time" then puts quote.bid_time
                        when "bidsz" then puts quote.bidsz
                        when "chg" then puts quote.chg
                        when "chg_sign" then puts quote.chg_sign
                        when "chg_t" then puts quote.chg_t
                        when "cl" then puts quote.cl
                        when "contract_size" then puts quote.contract_size
                        when "date" then puts quote.date
                        when "datetime" then puts quote.datetime
                        when "days_to_expiration" then puts quote.days_to_expiration
                        when "exch" then puts quote.exch
                        when "exch_desc" then puts quote.exch_desc
                        when "hi" then puts quote.hi
                        when "incr_vl" then puts quote.incr_vl
                        when "issue_desc" then puts quote.issue_desc
                        when "last" then puts quote.last
                        when "lo" then puts quote.lo
                        when "op_delivery" then puts quote.op_delivery
                        when "op_flag" then puts quote.op_flag
                        when "op_style" then puts quote.op_style
                        when "op_subclass" then puts quote.op_subclass
                        when "opn" then puts quote.opn
                        when "pchg" then puts quote.pchg
                        when "pchg_sign" then puts quote.pchg_sign
                        when "pcls" then puts quote.pcls
                        when "phi" then puts quote.phi
                        when "plo" then puts quote.plo
                        when "popn" then puts quote.popn
                        when "pr_date" then puts quote.pr_date
                        when "pr_openinterest" then puts quote.pr_openinterest
                        when "prchg" then puts quote.prchg
                        when "prem_mult" then puts quote.prem_mult
                        when "put_call" then puts quote.put_call
                        when "pvol" then puts quote.pvol
                        when "rootsymbol" then puts quote.rootsymbol
                        when "secclass" then puts quote.secclass
                        when "sesn" then puts quote.sesn
                        when "strikeprice" then puts quote.strikeprice
                        when "symbol" then puts quote.symbol
                        when "tcond" then puts quote.tcond
                        when "timestamp" then puts quote.timestamp
                        when "tr_num" then puts quote.tr_num
                        when "tradetick" then puts quote.tradetick
                        when "under_cusip" then puts quote.under_cusip
                        when "undersymbol" then puts quote.undersymbol
                        when "vl" then puts quote.vl
                        when "vwap" then puts quote.vwap
                        when "wk52hi" then puts quote.wk52hi
                        when "wk52hidate" then puts quote.wk52hidate
                        when "wk52lo" then puts quote.wk52lo
                        when "wk52lodate" then puts quote.wk52lodate
                        when "xdate" then puts quote.xdate
                        when "xday" then puts quote.xday
                        when "xmonth" then puts quote.xmonth
                        when "xyear" then puts quote.xyear
                        when "imp_volatility" then puts quote.imp_volatility
                        when "idelta" then puts quote.idelta
                        when "igamma" then puts quote.igamma
                        when "itheta" then puts quote.itheta
                        when "ivega" then puts quote.ivega
                        when "irho" then puts quote.irho
                        when "openinterest" then puts quote.openinterest
                    else
                        puts _val + " is not a valid operation"
                        break;
                    end
                end
                puts # add new line after each quote
            end
        elsif args.length == 1
            print_each_local( args[0].to_s )
        else    # defalut case - print all
            print_each_local("all")
        end
    end

    def print_each_local( _val  )
        for quote in @search_quote
            case _val
                when "all" then puts quote
                when "ask" then puts quote.ask
                when "ask_time" then puts quote.ask_time
                when "asksz" then puts quote.asksz
                when "basis" then puts quote.basis
                when "bid" then puts quote.bid
                when "bid_time" then puts quote.bid_time
                when "bidsz" then puts quote.bidsz
                when "chg" then puts quote.chg
                when "chg_sign" then puts quote.chg_sign
                when "chg_t" then puts quote.chg_t
                when "cl" then puts quote.cl
                when "contract_size" then puts quote.contract_size
                when "date" then puts quote.date
                when "datetime" then puts quote.datetime
                when "days_to_expiration" then puts quote.days_to_expiration
                when "exch" then puts quote.exch
                when "exch_desc" then puts quote.exch_desc
                when "hi" then puts quote.hi
                when "incr_vl" then puts quote.incr_vl
                when "issue_desc" then puts quote.issue_desc
                when "last" then puts quote.last
                when "lo" then puts quote.lo
                when "op_delivery" then puts quote.op_delivery
                when "op_flag" then puts quote.op_flag
                when "op_style" then puts quote.op_style
                when "op_subclass" then puts quote.op_subclass
                when "opn" then puts quote.opn
                when "pchg" then puts quote.pchg
                when "pchg_sign" then puts quote.pchg_sign
                when "pcls" then puts quote.pcls
                when "phi" then puts quote.phi
                when "plo" then puts quote.plo
                when "popn" then puts quote.popn
                when "pr_date" then puts quote.pr_date
                when "pr_openinterest" then puts quote.pr_openinterest
                when "prchg" then puts quote.prchg
                when "prem_mult" then puts quote.prem_mult
                when "put_call" then puts quote.put_call
                when "pvol" then puts quote.pvol
                when "rootsymbol" then puts quote.rootsymbol
                when "secclass" then puts quote.secclass
                when "sesn" then puts quote.sesn
                when "strikeprice" then puts quote.strikeprice
                when "symbol" then puts quote.symbol
                when "tcond" then puts quote.tcond
                when "timestamp" then puts quote.timestamp
                when "tr_num" then puts quote.tr_num
                when "tradetick" then puts quote.tradetick
                when "under_cusip" then puts quote.under_cusip
                when "undersymbol" then puts quote.undersymbol
                when "vl" then puts quote.vl
                when "vwap" then puts quote.vwap
                when "wk52hi" then puts quote.wk52hi
                when "wk52hidate" then puts quote.wk52hidate
                when "wk52lo" then puts quote.wk52lo
                when "wk52lodate" then puts quote.wk52lodate
                when "xdate" then puts quote.xdate
                when "xday" then puts quote.xday
                when "xmonth" then puts quote.xmonth
                when "xyear" then puts quote.xyear
                when "imp_volatility" then puts quote.imp_volatility
                when "idelta" then puts quote.idelta
                when "igamma" then puts quote.igamma
                when "itheta" then puts quote.itheta
                when "ivega" then puts quote.ivega
                when "irho" then puts quote.irho
                when "openinterest" then puts quote.openinterest
            else
                puts _val + " is not a valid operation"
                break;
            end
        end
    end


    attr_accessor :search_quote
end