from src.manager.lamalyse import Lamalyse
debug = True

stockArray = [
    'UBER',
    'LYFT',
    'AMZN',
    'FB',
    'GOOG',
    'AAPL',
               ]


analyser = Lamalyse()
analyser.debug = debug

if debug :
    data = analyser.start('AAPL',2)
else:
    counter = 1
    for stock in stockArray:
        counter = counter + 1
        data = analyser.start(stock,counter)

print("successfully updated analyse")
