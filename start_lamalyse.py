import socket

from src.manager.lamalyse import Lamalyse
debug = False
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.settimeout(2000)
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
