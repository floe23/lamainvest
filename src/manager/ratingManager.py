from src.manager.apiManager import ApiManager
import json
import numpy as np

class RatingManager(object):

    def __init__(self,jsonData):
        self.jsonData = jsonData
        self.doCalculations()


    def doCalculations(self):
        self.calculatePeRating()
        self.calculateGrowthRating(quarterlyEarningsTendency)
        self.calculateGrowthRating(yearlyEarningsTendency)
        self.setDividendYieldRating()
        self.setPayoutRatioRating()
        self.setReturnOnEquityRating()
        self.getPriceRating()

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


    def calculatePriceRating(self, price, fiftyTwoWeekHigh):
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


    def getPriceRating(self):

        price = self.jsonDataDetail['price']['regularMarketPrice']['raw']
        fiftyTwoWeekHigh = self.jsonDataDetail['quoteData'][self.stockSymbol]['fiftyTwoWeekHigh']['raw']
        fiftyTwoWeekHigh = self.jsonDataDetail['quoteData'][self.stockSymbol]['fiftyTwoWeekHigh']['raw']
        priceRating = self.calculatePriceRating(price, fiftyTwoWeekHigh)
        return priceRating

    def setDividendYieldRating(self):
        dividendYield = self.getDividendYield()
        if dividendYield > 0.01 and dividendYield < 0.05:
            return "😃"
        else:
            return "🙁"

    def setPayoutRatioRating(self):
        payoutRatio =  self.jsonDataDetail['summaryDetail']['payoutRatio']['raw']
        if payoutRatio < 0.6:
            return "😃"
        else:
            return "🙁"

    def setReturnOnEquityRating(self):
        returnOnEquity = self.getReturnOnEquity()
        if returnOnEquity > 0.1:
            return "😃"
        else:
            return "🙁"
