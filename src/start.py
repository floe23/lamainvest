from manager.yahooJsonManager import YahooJsonManager
from manager.lamainvest import Lamalyse

analyser = YahooJsonManager()
data = analyser.getStockInfo('AAPL')
