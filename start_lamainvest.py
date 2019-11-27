import socket
from src.settings import allStocks, debug

from src.manager.lamainvest import Lamalyse

analyser = Lamalyse()
analyser.debug = debug

if debug :
    data = analyser.createCsv(['AAPL','AAPL'])
    print(data)
else:
    data = analyser.createCsv(allStocks)

print("successfully updated analyse")
