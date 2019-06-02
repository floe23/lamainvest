from manager.yahooJsonManager import YahooJsonManager

analyser = YahooJsonManager()
analyser.setStock('AAPL')
analyser.getJson()
data = analyser.getKeyData()
print(data['price'])
print(data['priceToEarnings'])
print(data['payoutRatio'])
