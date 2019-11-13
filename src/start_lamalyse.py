from manager.lamalyse import Lamalyse


stockArray = [
    'AAPL',
    'AAPL',
    'AAPL',
    'AAPL',
    'AAPL',
               ]


analyser = Lamalyse()
analyser.debug = True

counter = 1
for stock in stockArray:
    counter = counter + 1
    data = analyser.start('AAPL',counter)
print("successfully updated analyse")
