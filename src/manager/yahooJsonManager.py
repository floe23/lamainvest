from manager.apiManager import ApiManager
import json

class YahooJsonManager(object):

    def setStock(self,stockSymbol):
        self.stockSymbol = stockSymbol

    def getJson(self):
        apiManager = ApiManager()
        stockSymbol = self.stockSymbol
        self.jsonData = apiManager.getYahooStockAnalyisis(stockSymbol)

    def calculateBuyRating(self):
        priceBelowHighRate_1 = 0.5
        priceBelowHighRate_2 = 0.6
        priceBelowHighRate_3 = 0.7
        priceBelowHighRate_4 = 0.8
        priceBelowHighRate_5 = 0.9
        price = self.jsonData['price']['regularMarketPrice']['raw']
        fiftyTwoWeekHigh = self.jsonData['quoteData'][self.stockSymbol]['fiftyTwoWeekHigh']['raw']
        print("hight",fiftyTwoWeekHigh)
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
        buyingRating = self.calculateBuyRating()
        newJsonData = {
            'shortName' : jsonData['quoteType']['shortName'],
            'longBusinessSummary' : jsonData['summaryProfile']['longBusinessSummary'],
            'returnOnEquity' : jsonData['financialData']['returnOnEquity']['raw'],
            'dividendYield' : jsonData['summaryDetail']['dividendYield']['raw'],
            'priceToEarnings' : priceToEarnings,
            'price' : jsonData['price']['regularMarketPrice']['raw'],
            'payoutRatio' : jsonData['summaryDetail']['payoutRatio']['raw'],
            'buyRating' : buyingRating
        }
        return newJsonData
