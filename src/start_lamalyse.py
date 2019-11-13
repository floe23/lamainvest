from manager.lamalyse import Lamalyse

analyser = Lamalyse()
analyser.debug = False
data = analyser.start('AAPL')
print("successfully updated analyse")
