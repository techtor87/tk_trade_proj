#!/usr/lib/ruby

# Use the OAuth gem
require 'rubygems'
require 'oauth'
require 'date'

require_relative 'tk_data_classes'

class TK_functions

    # Your key/secrets for authentication
    CONSUMER_KEY        = '5PC6akh4z5QNFOOR33PtCMocUEpeBZ3eN3j4eN3QQOU3'
    CONSUMER_SECRET     = 'g8kphN1GwJwkk2wynq4KGHzAlyppV8Q3PH0P7IQVFcI2'
    ACCESS_TOKEN        = 'tzSCap7Eh7Jr0PsFxQslZ6HJY1dao6QIDq6e1UIpehQ7'
    ACCESS_TOKEN_SECRET = 'Bdqs6xAFayEUbyvoAehjMJ690PuSFJ98x1ajs4IPGZI4'


    # Common String Creation
    MY_ACCOUNT          = '/v1/accounts/'
    GET_QUOTE           = '/v1/market/ext/quotes'
    GET_SEARCH          = '/v1/market/options/search'

    DATE_GREATER_THAN_QUERY  = '&query=xdate-gt%3'
    AND_STD_SIZE        = '%20AND%20contract_size-eq%3100'

    RETURN_TYPE_XML     = '.xml'
    RETURN_TYPE_JSON    = '.json'


    def initialize( accountNum = 38840110)
        @accountNumber = accountNum
        @account = Account.new
        @quote = Quote.new
        @search = Hash.new

        # Set up an OAuth Consumer
        @consumer = OAuth::Consumer.new( CONSUMER_KEY, CONSUMER_SECRET, :site => 'https://api.tradeking.com')

        # Manually update the access token/secret.  Typically this would be done through an OAuth callback when
        # authenticating other users.
        @@access_token = OAuth::AccessToken.new(@consumer, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

    end #initialize

    attr_accessor :account
    attr_accessor :quote
    attr_accessor :search

    def refresh_account_data()
        data = @@access_token.get(  MY_ACCOUNT \
                                    + @accountNumber.to_s \
                                    + RETURN_TYPE_XML )
                                    .body
        @account.parse(data)

        # puts @account
    end #refresh_account_data

    def get_quote( symbol )
        data = @@access_token.get(  GET_QUOTE  \
                                    + RETURN_TYPE_XML \
                                    + '?symbols=' \
                                    + symbol.to_s )
                                    .body

        @quote.parse(data)

        # puts @quote
    end #get_quote

    def get_search( symbol )
        temp_search = Search.new
        data = @@access_token.get(  GET_SEARCH \
                                    + RETURN_TYPE_XML \
                                    + '?symbol=' \
                                    + symbol.to_s \
                                    + DATE_GREATER_THAN_QUERY \
                                    + DateTime.now.strftime('%Y%m%d') \
                                    + AND_STD_SIZE )
                                    .body
        temp_search.parse(data)
        @search[symbol.to_s] = temp_search
        # @search[symbol.to_s].print_each("xdate", "ask", "bid", "openinterest")
    end #get_search

end #tk_functions class