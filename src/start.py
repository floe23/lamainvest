from manager.yahooJsonManager import YahooJsonManager
from manager.lamalyse import Lamalyse

analyser = YahooJsonManager()
data = analyser.getStockInfo('NBEV')
print(data['price'])
print(data['priceToEarnings'])
print(data['payoutRatio'])
