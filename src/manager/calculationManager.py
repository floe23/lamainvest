import json
import numpy as np

class CalculationManager(object):

    def __init__(self,jsonData):
        self.jsonData = jsonData
        self.doCalculations()

    def doCalculations(self):
        self.setPriceMaxHigh()
        self.getRevenueListYearlyTendency()
        #user from own json
        self.calculateGrowthRating(yearlyRevenueTendency)
        self.getEarningsListYearlyTendency()
        self.getEarningsListQuartarlyTendency()
        self.getDividendYield()
        self.getReturnOnEquity()
        self.getFiveYearChange()
        self.getThreeYearChange()
        self.getOneYearChange()


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


    def getRevenueListYearlyTendency(self):
        list = self.getRevenueListYearly()
        tendency = self.calculateGrowthSum(list)
        return tendency

    def getRevenueListQuarterlyTendency(self):
        list = self.getRevenueListQuarterly()
        tendency = self.calculateGrowthSum(list)
        return tendency

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

    def checkRevenueAmount(self,listToCheck):
        listSum = sum(listToCheck)
        oneBillion = 1000000000
        if listSum > oneBillion:
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

    def setPriceMaxHigh(self):
        stockPriceList = self.jsonDataDetailHistory['chart']['result'][0]['indicators']['adjclose'][0]['adjclose']
        priceMaxHigh = max(stockPriceList)
        self.priceMaxHigh = priceMaxHigh

    def getFiveYearChange(self):
        stockPriceList = self.jsonDataDetailHistory['chart']['result'][0]['indicators']['adjclose'][0]['adjclose']
        stockPriceListLength = len(stockPriceList)
        if stockPriceListLength > 20:
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
            today = stockPriceList[stockPriceListLength-1]
            fiveYearsAgo = stockPriceList[stockPriceListLength-13]
            growth = (today-fiveYearsAgo)/fiveYearsAgo
            return round(growth, 2)
        else:
            return 0

    def getOneYearChange(self):
        stockPriceList = self.jsonDataDetailHistory['chart']['result'][0]['indicators']['adjclose'][0]['adjclose']
        stockPriceListLength = len(stockPriceList)
        today = stockPriceList[stockPriceListLength-1]
        fiveYearsAgo = stockPriceList[stockPriceListLength-5]
        growth = (today-fiveYearsAgo)/fiveYearsAgo
        return round(growth, 2)
