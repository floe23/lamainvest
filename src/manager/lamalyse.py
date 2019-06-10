from manager.yahooJsonManager import YahooJsonManager
from manager.googleSheetManager import GoogleSheetManager

class Lamalyse(object):

    debug = False

    def start(self,stockSymbol):
        self.getYahooDataInfo(stockSymbol)
        self.writeKeysToSheet()
        self.writeDataToSheet()

    def getYahooDataInfo(self,stockSymbol):
        self.yahooJsonManager = YahooJsonManager()
        self.yahooJsonManager.debug = self.debug
        data = self.yahooJsonManager.getStockInfo(stockSymbol)
        self.dataJsonYahooInfo = data

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
        googleSheetManager.sheetRange = 'test!A2:Z2'
        data = self.dataJsonYahooInfo
        dataValues = []
        for dataValue in data.values():
            dataValues.append(dataValue)
        values = [dataValues]
        googleSheetManager.writeData(values)
