from src.manager.apiManager import ApiManager
import json
import numpy as np

class YahooJsonManager(object):

    debug = True

    def getStockInfo(self,stockSymbol):
        self.setStock(stockSymbol)
        self.getJson()
        data = self.getKeyData()
        return data

    def setStock(self,stockSymbol):
        self.stockSymbol = stockSymbol

    def getJson(self):
        apiManager = ApiManager()
        stockSymbol = self.stockSymbol
        if self.debug:
            self.jsonDataDetail = self.getTestJsonDetail()
            self.jsonDataDetailHistory = self.getTestJsonHistory()
        else:
            self.jsonDataDetail = apiManager.getYahooStockDetail(stockSymbol)
            self.jsonDataDetailHistory = apiManager.getYahooStockHistory(stockSymbol)

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
            'shortName' : jsonData['quoteType']['shortName'],
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
