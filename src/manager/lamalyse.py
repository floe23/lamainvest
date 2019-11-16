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
        self.stockSymbolList = stockSymbolList
        self.getYahooDataInfo()
        self.writeDataToCsv()


    def getYahooDataInfo(self):
        self.yahooJsonManager = YahooJsonManager()
        self.yahooJsonManager.debug = self.debug
        stockSymbolList = self.stockSymbolList
        dataList = []
        for stock in stockSymbolList:
            data = self.yahooJsonManager.getStockInfo(stock)
            dataList.append(data)
        self.dataJsonYahooInfo = data
        self.dataList = dataList
        return dataList

    def writeDataToCsv(self):
        row = ["moin","moin"]
        csvfile = "src/data/data.csv"
        with open(csvfile, 'w') as writeFile:
            writer = csv.writer(writeFile)
            writer.writerow(row)


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
