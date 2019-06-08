from manager.yahooJsonManager import YahooJsonManager

analyser = YahooJsonManager()
data = analyser.getStockInfo('NBEV')
print(data['price'])
print(data['priceToEarnings'])
print(data['payoutRatio'])
