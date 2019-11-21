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


    def getRevenueListYearly(self):
        jsonData = self.jsonDataDetail
        newEarningList = []
        earningList = jsonData['earnings']['financialsChart']['yearly']
        for earning in earningList:
            revenue = earning['revenue']['raw']
            newEarningList.append(revenue)
        return newEarningList

    def getRevenueListQuarterly(self):
        jsonData = self.jsonDataDetail
        newRevenueList = []
        revenueList = jsonData['earnings']['financialsChart']['quarterly']
        for revenue in revenueList:
            newRevenueList.append(revenue['revenue']['raw'])
        return newRevenueList

    def getEarningsListQuartarly(self):
        jsonData = self.jsonDataDetail
        earnings = []
        earningList = jsonData['earnings']['financialsChart']['quarterly']
        for earning in earningList:
            earnings.append(earning['earnings']['raw'])
        return earnings

    def getEarningsListYearly(self):
        jsonData = self.jsonDataDetail
        earnings = []
        earningList = jsonData['earnings']['financialsChart']['yearly']
        for earning in earningList:
            earnings.append(earning['earnings']['raw'])
        return earnings


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
        self.doCalculations()
        jsonData = self.jsonDataDetail
        pricePerShare = jsonData['price']['regularMarketPrice']['raw']
        earningsPerShare = jsonData['defaultKeyStatistics']['forwardEps']['raw']
        priceToEarnings = pricePerShare / earningsPerShare
        peRating = self.calculatePeRating()
        yearlyRevenueTendency = self.getRevenueListYearlyTendency()
        revenueYearlyRating = self.calculateGrowthRating(yearlyRevenueTendency)
        yearlyEarningsTendency = self.getEarningsListYearlyTendency()
        quarterlyEarningsTendency = self.getEarningsListQuartarlyTendency()
        earningsQuarterlyRating = self.calculateGrowthRating(quarterlyEarningsTendency)
        earningsYearlyRating = self.calculateGrowthRating(yearlyEarningsTendency)
        dividendYield = self.getDividendYield()
        returnOnEquity = self.getReturnOnEquity()
        stockPriceFiveYearChange = self.getFiveYearChange()
        stockPriceThreeYearChange = self.getThreeYearChange()
        stockPriceOneYearChange = self.getOneYearChange()
        dividendYieldRating = self.setDividendYieldRating()
        payoutRatioRating = self.setPayoutRatioRating()
        returnOnEquityRating = self.setReturnOnEquityRating()
        buyingRating = self.getPriceRating()

        newJsonData = {
            'stockPriceFiveYearChange' : stockPriceFiveYearChange,
            'stockPriceThreeYearChange' : stockPriceThreeYearChange,
            'stockPriceOneYearChange' : stockPriceOneYearChange,
            'buyRating' : buyingRating,
            'earningsYearlyRating' : earningsYearlyRating,
            'earningsQuarterlyRating' : earningsQuarterlyRating,
            'peRating' : peRating,
            'dividendYieldRating' : dividendYieldRating,
            'payoutRatioRating' : payoutRatioRating,
            'returnOnEquityRating' : returnOnEquityRating,
            'revenueYearlyRating' : revenueYearlyRating,
            'price' : jsonData['price']['regularMarketPrice']['raw'],
            'stockSymbol' : self.stockSymbol,
            'shortName' : jsonData['quoteType']['shortName'],
            'returnOnEquity' : returnOnEquity,
            'dividendYield' : dividendYield,
            'priceToEarnings' : priceToEarnings,
            'payoutRatio' : jsonData['summaryDetail']['payoutRatio']['raw'],
            'yearlyRevenueTendency' : yearlyRevenueTendency,
            'yearlyEarningsTendency' : yearlyEarningsTendency,
            'quarterlyEarningsTendency' : quarterlyEarningsTendency,
            'priceMax' : self.priceMaxHigh,
            # 'longBusinessSummary' : jsonData['summaryProfile']['longBusinessSummary'],
        }
        return newJsonData
