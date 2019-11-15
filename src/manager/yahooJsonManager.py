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


    def calculateGrowthSlope(self,mylist):

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

    def calculateGrowthSum(self,mylist):

        growthArray = []
        for pop in range(1, len(mylist)):
            growth = ((mylist[pop] - mylist[pop-1]) / mylist[pop-1])
            if mylist[pop-1] < 0:
                growth = growth * -1
            growthArray.append(growth)
        totalGrwoth = sum(growthArray)
        return round(totalGrwoth,2)


    def calculatePeRating(self):
        jsonData = self.jsonDataDetail
        PeRatingBelow_1 = 15
        PeRatingBelow_2 = 20
        PeRatingBelow_3 = 25
        PeRatingBelow_4 = 30
        PeRatingBelow_5 = 35
        pricePerShare = jsonData['price']['regularMarketPrice']['raw']
        earningsPerShare = jsonData['defaultKeyStatistics']['forwardEps']['raw']
        priceToEarnings = pricePerShare / earningsPerShare
        if priceToEarnings < PeRatingBelow_1:
            return "+++"
        if priceToEarnings < PeRatingBelow_2:
            return "++"
        if priceToEarnings < PeRatingBelow_3:
            return "+"
        if priceToEarnings < PeRatingBelow_4:
            return "-"
        if priceToEarnings < PeRatingBelow_5:
            return "--"
        return "---"


    def getRevenueListYearly(self):
        jsonData = self.jsonDataDetail
        newEarningList = []
        earningList = jsonData['earnings']['financialsChart']['yearly']
        for earning in earningList:
            revenue = earning['revenue']['raw']
            newEarningList.append(revenue)
        return newEarningList

    def checkRevenueAmount(self,listToCheck):
        listSum = sum(listToCheck)
        oneBillion = 1000000000
        if listSum > oneBillion:
            return True
        return False

    def getRevenueListYearlyTendency(self):
        list = self.getRevenueListYearly()
        tendency = self.calculateGrowthSum(list)
        return tendency

    def getRevenueListQuarterlyTendency(self):
        list = self.getRevenueListQuarterly()
        tendency = self.calculateGrowthSum(list)
        return tendency

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


    def checkEarningsAmount(self,listToCheck):
        listSum = sum(listToCheck)
        oneMillion = 1000000
        if listSum > (10*oneMillion):
            return True
        return False

    def checkEarningsAmountQuarterly(self,listToCheck):
        listSum = sum(listToCheck)
        if listSum > 5:
            return True
        return False


    def getEarningsListQuartarlyTendency(self):
        earningsList = self.getEarningsListQuartarly()
        positiveGrowth = self.checkEarningsAmountQuarterly(earningsList)
        if not positiveGrowth:
            return -1
        tendency = self.calculateGrowthSum(earningsList)
        return tendency

    def getEarningsListYearlyTendency(self):
        earningsList = self.getEarningsListYearly()
        positiveGrowth = self.checkEarningsAmount(earningsList)
        if not positiveGrowth:
            return -1
        tendency = self.calculateGrowthSum(earningsList)
        return tendency


    def getEarningsListYearly(self):
        jsonData = self.jsonDataDetail
        earnings = []
        earningList = jsonData['earnings']['financialsChart']['yearly']
        for earning in earningList:
            print(earning['earnings']['raw'])
            earnings.append(earning['earnings']['raw'])
        return earnings


    def calculatePriceRating(self, price, fiftyTwoWeekHigh):
        priceBelowHighRate_1 = 0.98
        priceBelowHighRate_2 = 0.8
        priceBelowHighRate_3 = 0.5
        priceBelowHighRate_4 = 0.4
        priceBelowHighRate_5 = 0.2
        if (1 - (price / fiftyTwoWeekHigh)) >= priceBelowHighRate_1:
            return "+++"
        if (1 - (price / fiftyTwoWeekHigh)) >= priceBelowHighRate_2:
            return "++"
        if (1 - (price / fiftyTwoWeekHigh)) >= priceBelowHighRate_3:
            return "+"
        if (1 - (price / fiftyTwoWeekHigh)) >= priceBelowHighRate_4:
            return "-"
        if (1 - (price / fiftyTwoWeekHigh)) >= priceBelowHighRate_5:
            return "--"
        return "---"

    def calculateGrowthRating(self, tendency):
        print("tendency",tendency)
        tendency_mark_1 = 0.6
        tendency_mark_2 = 0.4
        tendency_mark_3 = 0.2
        tendency_mark_4 = 0.15
        tendency_mark_5 = 0.1
        if tendency >= tendency_mark_1:
            return "+++"
        if tendency >= tendency_mark_2:
            return "++"
        if tendency >= tendency_mark_3:
            return "+"
        if tendency >= tendency_mark_4:
            return "-"
        if tendency >= tendency_mark_5:
            return "--"
        return "---"


    def getPriceRating(self):

        price = self.jsonDataDetail['price']['regularMarketPrice']['raw']
        fiftyTwoWeekHigh = self.jsonDataDetail['quoteData'][self.stockSymbol]['fiftyTwoWeekHigh']['raw']
        priceRating = self.calculatePriceRating(price, fiftyTwoWeekHigh)
        return priceRating

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

    def getFiveYearChange(self):
        stockPriceList = self.jsonDataDetailHistory['chart']['result'][0]['indicators']['adjclose'][0]['adjclose']
        stockPriceListLength = len(stockPriceList)
        if stockPriceListLength > 20:
            print(stockPriceListLength)
            today = stockPriceList[stockPriceListLength-1]
            fiveYearsAgo = stockPriceList[stockPriceListLength-21]
            growth = (today-fiveYearsAgo)/fiveYearsAgo
            return round(growth, 2)
        else:
            return 0

    def getThreeYearChange(self):
        stockPriceList = self.jsonDataDetailHistory['chart']['result'][0]['indicators']['adjclose'][0]['adjclose']
        stockPriceListLength = len(stockPriceList)
        if stockPriceListLength > 20:
            print(stockPriceListLength)
            today = stockPriceList[stockPriceListLength-1]
            fiveYearsAgo = stockPriceList[stockPriceListLength-13]
            growth = (today-fiveYearsAgo)/fiveYearsAgo
            return round(growth, 2)
        else:
            return 0

    def getOneYearChange(self):
        stockPriceList = self.jsonDataDetailHistory['chart']['result'][0]['indicators']['adjclose'][0]['adjclose']
        stockPriceListLength = len(stockPriceList)
        print(stockPriceListLength)
        today = stockPriceList[stockPriceListLength-1]
        fiveYearsAgo = stockPriceList[stockPriceListLength-5]
        growth = (today-fiveYearsAgo)/fiveYearsAgo
        return round(growth, 2)

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

    def getKeyData(self):
        jsonData = self.jsonDataDetail
        pricePerShare = jsonData['price']['regularMarketPrice']['raw']
        earningsPerShare = jsonData['defaultKeyStatistics']['forwardEps']['raw']
        priceToEarnings = pricePerShare / earningsPerShare
        buyingRating = self.getPriceRating()
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
            'longBusinessSummary' : jsonData['summaryProfile']['longBusinessSummary'],
        }
        return newJsonData
