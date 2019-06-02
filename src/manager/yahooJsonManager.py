from apiManager import ApiManager
import json

class YahooJsonManager(object):

    def setStock(self,stockSymbol):
        self.stockSymbol = stockSymbol

    def getJson(self):
        apiManager = ApiManager()
        stockSymbol = self.stockSymbol
        self.jsonData = apiManager.getYahooStockAnalyisis(stockSymbol)
        print(self.jsonData)

    def getKeyData(self):
        jsonData = self.jsonData
        pricePerShare = jsonData['price']['regularMarketPrice']['raw']
        earningsPerShare = jsonData['defaultKeyStatistics']['forwardEps']['raw']
        priceToEarnings = pricePerShare / earningsPerShare
        newJsonData = {
            'shortName' : jsonData['quoteType']['shortName'],
            'longBusinessSummary' : jsonData['summaryProfile']['longBusinessSummary'],
            'returnOnEquity' : jsonData['financialData']['returnOnEquity']['raw'],
            'dividendYield' : jsonData['summaryDetail']['dividendYield']['raw'],
            'priceToEarnings' : priceToEarnings,
            'price' : jsonData['price']['regularMarketPrice']['raw'],
            'payoutRatio' : jsonData['summaryDetail']['payoutRatio']['raw']
        }
        return newJsonData
