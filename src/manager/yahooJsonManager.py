from manager.apiManager import ApiManager
import json
import numpy as np

class YahooJsonManager(object):

    def setStock(self,stockSymbol):
        self.stockSymbol = stockSymbol

    def getJson(self):
        apiManager = ApiManager()
        stockSymbol = self.stockSymbol
        self.jsonData = apiManager.getYahooStockAnalyisis(stockSymbol)

    def analyseTendency(self,mylist):

        y = np.array(mylist)
        x = np.arange(1, len(y)+1)

        A = np.vstack([x, np.ones(len(x))]).T
        m, c = np.linalg.lstsq(A, y, rcond=None)[0]
        if m > 0:
            print("Steigender Trend mit Steigung m =", m)
        else:
            print("Fallender Trend mit Steigung m =", m)
        y_fit = m*x + c
        print("y-werte der ausgleichsrechnung: ", y_fit)
        return m


    def calculatePeRating(self):
        jsonData = self.jsonData
        PeRatingBelow_1 = 15
        PeRatingBelow_2 = 20
        PeRatingBelow_3 = 25
        PeRatingBelow_4 = 30
        PeRatingBelow_5 = 35
        pricePerShare = jsonData['price']['regularMarketPrice']['raw']
        earningsPerShare = jsonData['defaultKeyStatistics']['forwardEps']['raw']
        priceToEarnings = pricePerShare / earningsPerShare
        if priceToEarnings < PeRatingBelow_1:
            return 1
        if priceToEarnings < PeRatingBelow_2:
            return 2
        if priceToEarnings < PeRatingBelow_3:
            return 3
        if priceToEarnings < PeRatingBelow_4:
            return 4
        if priceToEarnings < PeRatingBelow_5:
            return 5
        return 6

    def checkPositiveGrowthPercent(self,listToCheck):
        listSum = sum(listToCheck)
        if listSum > 0:
            return True
        return False

    def checkPositiveGrowth(self,listToCheck):
        listSum = sum(listToCheck)
        if listSum > 1000000000:
            return True
        return False

    def getEarningsListQuartarlyTendency(self):
        earningsList = self.getEarningsListQuartarly()
        positiveGrowth = self.checkPositiveGrowthPercent(earningsList)
        if not positiveGrowth:
            return -1
        tendency = self.analyseTendency(earningsList)
        return tendency

    def getEarningsListYearlyTendency(self):
        earningsList = self.getEarningsListYearly()
        positiveGrowth = self.checkPositiveGrowth(earningsList)
        if not positiveGrowth:
            return -1
        tendency = self.analyseTendency(earningsList)
        return tendency

    def getRevenueListYearlyTendency(self):
        earningsList = self.getRevenueListYearly()
        positiveGrowth = self.checkPositiveGrowth(earningsList)
        if not positiveGrowth:
            return -1
        tendency = self.analyseTendency(earningsList)
        return tendency

    def getEarningsListQuartarly(self):
        jsonData = self.jsonData
        earnings = []
        earningList = jsonData['earnings']['earningsChart']['quarterly']
        for earning in earningList:
            earnings.append(earning['actual']['raw'])
        return earnings

    def getEarningsListYearly(self):
        jsonData = self.jsonData
        earnings = []
        earningList = jsonData['earnings']['financialsChart']['yearly']
        for earning in earningList:
            print(earning['earnings']['raw'])
            earnings.append(earning['earnings']['raw'])
        return earnings

    def getRevenueListYearly(self):
        jsonData = self.jsonData
        earnings = []
        earningList = jsonData['earnings']['financialsChart']['yearly']
        for earning in earningList:
            earnings.append(earning['revenue']['raw'])
        return earnings

    def calculatePriceRating(self):
        priceBelowHighRate_1 = 0.5
        priceBelowHighRate_2 = 0.6
        priceBelowHighRate_3 = 0.7
        priceBelowHighRate_4 = 0.8
        priceBelowHighRate_5 = 0.9
        price = self.jsonData['price']['regularMarketPrice']['raw']
        fiftyTwoWeekHigh = self.jsonData['quoteData'][self.stockSymbol]['fiftyTwoWeekHigh']['raw']
        if price < fiftyTwoWeekHigh * priceBelowHighRate_1:
            return 1
        if price < fiftyTwoWeekHigh * priceBelowHighRate_2:
            return 2
        if price < fiftyTwoWeekHigh * priceBelowHighRate_3:
            return 3
        if price < fiftyTwoWeekHigh * priceBelowHighRate_4:
            return 4
        if price < fiftyTwoWeekHigh * priceBelowHighRate_5:
            return 5
        return 6

    def getKeyData(self):
        jsonData = self.jsonData
        pricePerShare = jsonData['price']['regularMarketPrice']['raw']
        earningsPerShare = jsonData['defaultKeyStatistics']['forwardEps']['raw']
        priceToEarnings = pricePerShare / earningsPerShare
        buyingRating = self.calculatePriceRating()
        peRating = self.calculatePeRating()
        newJsonData = {
            'shortName' : jsonData['quoteType']['shortName'],
            'longBusinessSummary' : jsonData['summaryProfile']['longBusinessSummary'],
            'returnOnEquity' : jsonData['financialData']['returnOnEquity']['raw'],
            'dividendYield' : jsonData['summaryDetail']['dividendYield']['raw'],
            'priceToEarnings' : priceToEarnings,
            'price' : jsonData['price']['regularMarketPrice']['raw'],
            'payoutRatio' : jsonData['summaryDetail']['payoutRatio']['raw'],
            'buyRating' : buyingRating,
            'peRating' : peRating
        }
        return newJsonData
