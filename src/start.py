from manager.yahooJsonManager import YahooJsonManager

analyser = YahooJsonManager()
analyser.setStock('BMW.DE')
analyser.getJson()
data = analyser.getKeyData()
print(data)
# print(data['price'])
# print(data['priceToEarnings'])
# print(data['payoutRatio'])
