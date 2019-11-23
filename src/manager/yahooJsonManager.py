from src.manager.apiManager import ApiManager
import json
import numpy as np

class YahooJsonManager(object):

    debug = True

    def __init__(self):
        self.apiManager = ApiManager()

    def getStockInfo(self,usersInput):
        stockSymbol = self.validaUsersInput(usersInput)
        if stockSymbol:
            self.setStock(stockSymbol)
            self.getJson()
            data = self.getKeyData()
            return data
        return False

    def setStock(self,stockSymbol):
        self.stockSymbol = stockSymbol

    def getJson(self):
        stockSymbol = self.stockSymbol
        if self.debug:
            self.jsonDataAutoComplete = self.getTestJsonAutoComplete()
            self.jsonDataDetail = self.getTestJsonDetail()
            self.jsonDataDetailHistory = self.getTestJsonHistory()
        else:
            self.jsonDataDetail = self.apiManager.getYahooStockDetail(stockSymbol)
            self.jsonDataDetailHistory = self.apiManager.getYahooStockHistory(stockSymbol)

    def validaUsersInput(self,usersInput):
        autoCompleteResponse = self.apiManager.getYahooAutoComplete(usersInput)
        if len(autoCompleteResponse['ResultSet']['Result']) > 0:
            stockSymbol = autoCompleteResponse['ResultSet']['Result'][0]['symbol']
            return stockSymbol
        return False

    def getTestJsonAutoComplete(self):
        with open('src/test/testDataAutoComplete_AAPL.json', 'r') as myfile:
            testJson=myfile.read()
        testJson = json.loads(testJson)
        return testJson

    def getTestJsonDetail(self):
        with open('src/test/testDataDetail_AAPL.json', 'r') as myfile:
            testJson=myfile.read()
        testJson = json.loads(testJson)
        return testJson

    def getTestJsonHistory(self):
        with open('src/test/testDataHistory_AAPL.json', 'r') as myfile:
            testJson=myfile.read()
        testJson = json.loads(testJson)
        return testJson

    def getDividendYield(self):
        try:
            dividendYield = self.jsonDataDetail['summaryDetail']['dividendYield']['raw']
            return dividendYield
        except:
            return 0

    def getReturnOnEquity(self):
        try:
            returnOnEquity = self.jsonDataDetail['financialData']['returnOnEquity']['raw']
            return returnOnEquity
        except:
            return 0

    def getKeyData(self):
        jsonData = self.jsonDataDetail
        pricePerShare = jsonData['price']['regularMarketPrice']['raw']
        earningsPerShare = jsonData['defaultKeyStatistics']['forwardEps']['raw']
        priceToEarnings = pricePerShare / earningsPerShare
        dividendYield = self.getDividendYield()
        returnOnEquity = self.getReturnOnEquity()

        newJsonData = {
            'totalRating' : 0,
            'buyRating' : 0,
            'buySuggestion' : 0,
            'shortName' : jsonData['quoteType']['shortName'],
            'dividendYieldRating' : 0,
            'stockPriceFiveYearChange' : 0,
            'stockPriceThreeYearChange' : 0,
            'stockPriceOneYearChange' : 0,
            'earningsYearlyRating' : 0,
            'earningsQuarterlyRating' : 0,
            'peRating' : 0,
            'payoutRatioRating' : 0,
            'returnOnEquityRating' : 0,
            'revenueYearlyRating' : 0,
            'price' : jsonData['price']['regularMarketPrice']['raw'],
            'stockSymbol' : self.stockSymbol,
            'returnOnEquity' : returnOnEquity,
            'dividendYield' : dividendYield,
            'priceToEarnings' : priceToEarnings,
            'payoutRatio' : jsonData['summaryDetail']['payoutRatio']['raw'],
            'yearlyRevenueTendency' : 0,
            'yearlyEarningsTendency' : 0,
            'quarterlyEarningsTendency' : 0,
            'priceMax' : 0,
            # 'longBusinessSummary' : jsonData['summaryProfile']['longBusinessSummary'],
        }
        self.keyData = newJsonData
        allData = {
            "jsonDataDetail": self.jsonDataDetail,
            "jsonDataDetailHistory": self.jsonDataDetailHistory,
            "keyData": self.keyData
        }
        return allData
