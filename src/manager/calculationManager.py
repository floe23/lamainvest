import json
import numpy as np

class CalculationManager(object):

    def __init__(self,allData):
        self.allData = allData
        self.keyData = self.allData['keyData']
        self.jsonDataDetail = self.allData['jsonDataDetail']
        self.jsonDataDetailHistory = self.allData['jsonDataDetailHistory']
        self.doCalculations()

    def doCalculations(self):
        self.setPriceMaxHigh()
        self.getRevenueListYearlyTendency()
        #user from own json
        self.getEarningsListYearlyTendency()
        self.getEarningsListQuartarlyTendency()
        self.getFiveYearChange()
        self.getThreeYearChange()
        self.getOneYearChange()
        self.updateAllData()

    def updateAllData(self):
        self.allData['keyData'] = self.keyData

    def setPriceMaxHigh(self):
        stockPriceList = self.jsonDataDetailHistory['chart']['result'][0]['indicators']['adjclose'][0]['adjclose']
        if stockPriceList:
            priceMaxHigh = max(stockPriceList)
            self.keyData['priceMaxHigh'] = priceMaxHigh

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
        self.keyData['yearlyRevenueTendency'] = tendency

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
        self.keyData['quarterlyEarningsTendency'] = tendency

    def getEarningsListYearlyTendency(self):
        earningsList = self.getEarningsListYearly()
        positiveGrowth = self.checkEarningsAmount(earningsList)
        if not positiveGrowth:
            return -1
        tendency = self.calculateGrowthSum(earningsList)
        self.keyData['yearlyEarningsTendency'] = tendency



    def getFiveYearChange(self):
        change = 0
        stockPriceList = self.jsonDataDetailHistory['chart']['result'][0]['indicators']['adjclose'][0]['adjclose']
        stockPriceListLength = len(stockPriceList)
        if stockPriceListLength > 20:
            today = stockPriceList[stockPriceListLength-1]
            fiveYearsAgo = stockPriceList[stockPriceListLength-21]
            growth = (today-fiveYearsAgo)/fiveYearsAgo
            change = round(growth, 2)
        self.keyData['stockPriceFiveYearChange'] = change


    def getThreeYearChange(self):
        change = 0
        stockPriceList = self.jsonDataDetailHistory['chart']['result'][0]['indicators']['adjclose'][0]['adjclose']
        stockPriceListLength = len(stockPriceList)
        if stockPriceListLength > 12:
            today = stockPriceList[stockPriceListLength-1]
            fiveYearsAgo = stockPriceList[stockPriceListLength-13]
            growth = (today-fiveYearsAgo)/fiveYearsAgo
            change = round(growth, 2)
        self.keyData['stockPriceThreeYearChange'] = change

    def getOneYearChange(self):
        change = 0
        stockPriceList = self.jsonDataDetailHistory['chart']['result'][0]['indicators']['adjclose'][0]['adjclose']
        stockPriceListLength = len(stockPriceList)
        if stockPriceListLength > 4:
            today = stockPriceList[stockPriceListLength-1]
            fiveYearsAgo = stockPriceList[stockPriceListLength-5]
            growth = (today-fiveYearsAgo)/fiveYearsAgo
            change = round(growth, 2)
        self.keyData['stockPriceOneYearChange'] = change

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
