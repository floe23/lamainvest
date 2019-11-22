from src.manager.apiManager import ApiManager
import json
import numpy as np

class RatingManager(object):

    def __init__(self,allData):
        self.allData = allData
        self.keyData = self.allData['keyData']
        self.jsonDataDetail = self.allData['jsonDataDetail']
        self.jsonDataDetailHistory = self.allData['jsonDataDetailHistory']
        self.doCalculations()


    def doCalculations(self):
        self.calculateYearlyRevenueRating()
        self.calculateQuarterlyEarningsRating()
        self.calculateYearlyEarningsRating()
        self.setBuyRating()
        self.setPeRating()
        self.setDividendYieldRating()
        self.setPayoutRatioRating()
        self.setReturnOnEquityRating()
        self.updateAllData()

    def setPeRating(self):
        peRating = self.calculatePeRating()
        self.keyData['peRating'] = peRating

    def setDividendYieldRating(self):
        dividendYieldRating = self.calculateDividendYieldRating()
        self.keyData['dividendYieldRating'] = dividendYieldRating

    def setPayoutRatioRating(self):
        payoutRatioRating = self.calculatePayoutRatioRating()
        self.keyData['payoutRatioRating'] = payoutRatioRating

    def setReturnOnEquityRating(self):
        returnOnEquityRating = self.calculateReturnOnEquityRating()
        self.keyData['returnOnEquityRating'] = returnOnEquityRating

    def calculateYearlyRevenueRating(self):
        yearlyRevenueTendency = self.keyData['yearlyRevenueTendency']
        yearlyRevenueRating = self.calculateGrowthRating(yearlyRevenueTendency)
        self.keyData['revenueYearlyRating'] = yearlyRevenueRating

    def calculateQuarterlyEarningsRating(self):
        quarterlyEarningsTendency = self.keyData['quarterlyEarningsTendency']
        earningsQuarterlyRating = self.calculateGrowthRating(quarterlyEarningsTendency)
        self.keyData['earningsQuarterlyRating'] = earningsQuarterlyRating

    def calculateYearlyEarningsRating(self):
        yearlyEarningsTendency = self.keyData['yearlyEarningsTendency']
        earningsYearlyRating = self.calculateGrowthRating(yearlyEarningsTendency)
        self.keyData['earningsYearlyRating'] = earningsYearlyRating

    def updateAllData(self):
        self.allData['keyData'] = self.keyData


    def calculatePeRating(self):
        jsonData = self.jsonDataDetail
        PeRatingBelow_10 = 5
        PeRatingBelow_9 = 10
        PeRatingBelow_8 = 15
        PeRatingBelow_7 = 25
        PeRatingBelow_6 = 50
        pricePerShare = jsonData['price']['regularMarketPrice']['raw']
        earningsPerShare = jsonData['defaultKeyStatistics']['forwardEps']['raw']
        priceToEarnings = pricePerShare / earningsPerShare
        if priceToEarnings < PeRatingBelow_10:
            return 10
        if priceToEarnings < PeRatingBelow_9:
            return 9
        if priceToEarnings < PeRatingBelow_8:
            return 8
        if priceToEarnings < PeRatingBelow_7:
            return 7
        if priceToEarnings < PeRatingBelow_6:
            return 6
        return 0


    def calculateBuyRating(self, price, fiftyTwoWeekHigh):
        priceBelowHighRate_10 = 0.5
        priceBelowHighRate_9 = 0.45
        priceBelowHighRate_8 = 0.4
        priceBelowHighRate_7 = 0.35
        priceBelowHighRate_6 = 0.3
        priceBelowHighRate_5 = 0.25
        priceBelowHighRate_4 = 0.2
        priceBelowHighRate_3 = 0.15
        priceBelowHighRate_2 = 0.1
        priceBelowHighRate_1 = 0.05
        if (1 - (price / fiftyTwoWeekHigh)) >= priceBelowHighRate_10:
            return 10
        if (1 - (price / fiftyTwoWeekHigh)) >= priceBelowHighRate_9:
            return 9
        if (1 - (price / fiftyTwoWeekHigh)) >= priceBelowHighRate_8:
            return 8
        if (1 - (price / fiftyTwoWeekHigh)) >= priceBelowHighRate_7:
            return 7
        if (1 - (price / fiftyTwoWeekHigh)) >= priceBelowHighRate_6:
            return 6
        if (1 - (price / fiftyTwoWeekHigh)) >= priceBelowHighRate_5:
            return 5
        if (1 - (price / fiftyTwoWeekHigh)) >= priceBelowHighRate_4:
            return 4
        if (1 - (price / fiftyTwoWeekHigh)) >= priceBelowHighRate_3:
            return 3
        if (1 - (price / fiftyTwoWeekHigh)) >= priceBelowHighRate_2:
            return 2
        if (1 - (price / fiftyTwoWeekHigh)) >= priceBelowHighRate_1:
            return 1
        return 0

    def calculateGrowthRating(self, tendency):
        tendency_mark_1 = 0.6
        tendency_mark_2 = 0.4
        tendency_mark_3 = 0.2
        tendency_mark_4 = 0.15
        tendency_mark_5 = 0.1
        if tendency >= tendency_mark_1:
            return 10
        if tendency >= tendency_mark_2:
            return 9
        if tendency >= tendency_mark_3:
            return 8
        if tendency >= tendency_mark_4:
            return 7
        if tendency >= tendency_mark_5:
            return 6
        return 5


    def setBuyRating(self):

        stockSymbol = self.keyData['stockSymbol']
        price = self.jsonDataDetail['price']['regularMarketPrice']['raw']
        fiftyTwoWeekHigh = self.jsonDataDetail['quoteData'][stockSymbol]['fiftyTwoWeekHigh']['raw']
        fiftyTwoWeekHigh = self.jsonDataDetail['quoteData'][stockSymbol]['fiftyTwoWeekHigh']['raw']
        buyRating = self.calculateBuyRating(price, fiftyTwoWeekHigh)
        self.keyData['buyRating'] = buyRating

    def calculateDividendYieldRating(self):
        dividendYield = self.keyData['dividendYield']
        if dividendYield > 0.01 and dividendYield < 0.05:
            return "😃"
        else:
            return "🙁"

    def calculatePayoutRatioRating(self):
        payoutRatio =  self.jsonDataDetail['summaryDetail']['payoutRatio']['raw']
        if payoutRatio < 0.6:
            return "😃"
        else:
            return "🙁"

    def calculateReturnOnEquityRating(self):
        returnOnEquity = self.keyData['returnOnEquity']
        if returnOnEquity > 0.1:
            return "😃"
        else:
            return "🙁"
