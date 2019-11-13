from manager.lamalyse import Lamalyse


stockArray = [
    'UBER',
    'LYFT',
    'AMZN',
    'FB',
    'GOOG',
    'AAPL',
               ]


analyser = Lamalyse()
analyser.debug = False

counter = 1
for stock in stockArray:
    counter = counter + 1
    data = analyser.start(stock,counter)
print("successfully updated analyse")
