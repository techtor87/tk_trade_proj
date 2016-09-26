#!/usr/bin/env python

import sys
import oauth2 as oauth
import datetime

from tk_data_classes import *

class TK_functions:

    # Your key/secrets for authentication
    CONSUMER_KEY        = '5PC6akh4z5QNFOOR33PtCMocUEpeBZ3eN3j4eN3QQOU3'
    CONSUMER_SECRET     = 'g8kphN1GwJwkk2wynq4KGHzAlyppV8Q3PH0P7IQVFcI2'
    ACCESS_TOKEN        = 'tzSCap7Eh7Jr0PsFxQslZ6HJY1dao6QIDq6e1UIpehQ7'
    ACCESS_TOKEN_SECRET = 'Bdqs6xAFayEUbyvoAehjMJ690PuSFJ98x1ajs4IPGZI4'

    SITE                = 'https://api.tradeking.com/v1'
    MY_ACCOUNT          = '/accounts/'
    GET_QUOTE           = '/market/ext/quotes'
    GET_SEARCH          = '/market/options/search'
    GET_CLOCK           = '/market/clock'

    DATE_GREATER_THAN_QUERY = '&query=xdate=gt%3'
    AND_STD_SIZE        = '%20AND%20contract_size-eq%3100'

    RETURN_TYPE_XML     = '.xml'
    RETURN_TYPE_JSON    = '.json'


    def __init__(self, accountNum=38840110):
        self.accountNum = accountNum
        self.account = Account()
        self.quote = Quote()
        self.search = Search()

        self.oauth_consumer = oauth.Consumer( key = self.CONSUMER_KEY, secret = self.CONSUMER_SECRET )
        self.oauth_token = oauth.Token( key = self.ACCESS_TOKEN, secret = self.ACCESS_TOKEN_SECRET )
        self.oauth_client = oauth.Client( self.oauth_consumer, self.oauth_token )


    def refresh_account_data(self):
        response, data = self.oauth_client.request( self.SITE
                                                    + self.MY_ACCOUNT
                                                    + str(self.accountNum)
                                                    + self.RETURN_TYPE_JSON )

        self.account.parse(data)
        # print self.account.to_s()

    def get_quote(self, symbol):
        response, data = self.oauth_client.request( self.SITE
                                                    + self.GET_QUOTE
                                                    + self.RETURN_TYPE_JSON
                                                    + '?symbols='
                                                    + symbol )
        self.quote.parse(data)
        # print self.quote.to_s()

    def get_search(self, symbol):
        response, data = self.oauth_client.request( self.SITE
                                                    + self.GET_SEARCH
                                                    + self.RETURN_TYPE_JSON
                                                    + '?symbol='
                                                    + symbol
                                                    + self.DATE_GREATER_THAN_QUERY
                                                    + datetime.date.today().strftime('%Y%m%d')
                                                    + self.AND_STD_SIZE )

        self.search.parse(data)
        # print self.search.to_s()

