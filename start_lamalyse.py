import socket

from src.manager.lamalyse import Lamalyse
debug = False
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.settimeout(2000)
stockArray1 = [
    'UBER','LYFT','AMZN','DPW.DE','FB','GOOG','MSFT','B4B.DE','LAME4.SA','SPOT','OGZPY','RDS-A','MA','PYPL','KO','PEP','MC','CMG','VOW.DE','BMW.DE','KMB','GPC','FAST','VALE','PM','PBR','BAYRY','SMSN.IL','SNE','DB','dov','emr','wmt','axp','trow','xom','ev','gpc','pm','cvx','jnj','mmm','txn','mo','fast','sbsi','ul','ohi','cl','mcd','flo','clx','ko','adp','el','mkc','pg','pep','cost','nke','yum','hsy','wpc','ohi','ravn','kmb'
               ]
stockArray = [
    'DOV','wmt'
               ]
analyser = Lamalyse()
analyser.debug = debug

if debug :
    data = analyser.createCsv(['AAPL','AAPL'])
    print(data)
else:
    data = analyser.createCsv(stockArray1)

print("successfully updated analyse")
