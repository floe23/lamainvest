from manager.yahooJsonManager import YahooJsonManager
from manager.lamalyse import Lamalyse

analyser = YahooJsonManager()
data = analyser.getStockInfo('AAPL')
