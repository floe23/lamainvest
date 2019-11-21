import csv

from src.manager.yahooJsonManager import YahooJsonManager
from src.manager.googleSheetManager import GoogleSheetManager

class Lamalyse(object):

    debug = False

    def __init__(self):
        print("ini class")

    def start(self,stockSymbol, sheetRow):
        self.sheetRow = sheetRow
        self.getYahooDataInfo(stockSymbol)
        self.writeKeysToSheet()
        self.writeDataToSheet()

    def createCsv(self,stockSymbolList):
        self.getYahooDataInfo(stockSymbolList)
        self.writeDataToCsv()


    def getYahooDataInfo(self, stockSymbolList):
        self.yahooJsonManager = YahooJsonManager()
        self.yahooJsonManager.debug = self.debug
        dataList = []
        data = []
        counter = 0
        max = len(stockSymbolList)
        for stock in stockSymbolList:
            stock = stock.upper()
            counter = counter + 1
            printMsg = "{0}/{1}".format(counter,max)
            data = self.getData(stock)
            if data:
                dataList.append(data)
        self.dataJsonYahooInfo = data
        self.dataList = dataList
        return dataList

    def getData(self,stock):
        data = self.getDataFromApi(stock)
        data = self.setKeyData(data)
        data = self.setCalculatedValues(data)
        data = self.setRatings(data)
        return data

    def setKeyData(self,data):
        return data

    def setCalculatedValues(self,data):
        return data

    def setRatings(self,data):
        return data

    def getDataFromApi(self,stock):
        for i in range(0,5):
            try:
                print("get data for:", stock)
                data = self.yahooJsonManager.getStockInfo(stock)
                return data
            except Exception as e:
                print("error:", e)
                print("try again:", stock)
        return False

    def writeDataToCsv(self):
        dataList = self.createDataValueList()
        csvfile = "src/data/data.csv"
        with open(csvfile, 'w') as writeFile:
            writer = csv.writer(writeFile)
            writer.writerows(dataList)

    def createDataValueList(self):
        jsonDataList = self.dataList
        dataList = []
        keys = []
        for key in jsonDataList[0].keys():
            keys.append(key)
        dataList.append(keys)
        for jsonData in jsonDataList:
            dataValues = []
            for dataValue in jsonData.values():
                if not isinstance(dataValue, str):
                    dataValue = round(dataValue,2)
                dataValues.append(dataValue)
            dataList.append(dataValues)
        return dataList


    def writeKeysToSheet(self):
        googleSheetManager = GoogleSheetManager()
        googleSheetManager.sheetRange = 'test!A1:Z1'
        data = self.dataJsonYahooInfo
        keys = []
        for key in data.keys():
            keys.append(key)
        values = [keys]
        googleSheetManager.writeData(values)

    def writeDataToSheet(self):
        googleSheetManager = GoogleSheetManager()
        googleSheetManager.sheetRange = 'test!A{0}:Z{0}'.format(self.sheetRow)
        data = self.dataJsonYahooInfo
        dataValues = []
        for dataValue in data.values():
            dataValues.append(dataValue)
        values = [dataValues]
        googleSheetManager.writeData(values)
