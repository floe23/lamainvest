import socket

from src.manager.lamalyse import Lamalyse
debug = False
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.settimeout(2000)
stockArray1 = [
    'UBER','LYFT','AMZN','DPW.DE','FB','GOOG','MSFT','B4B.DE','LAME4.SA','SPOT','RDS-A','MA','PYPL','KO','PEP','CMG','VOW.DE','BMW.DE','KMB','GPC','FAST','VALE','PM','PBR','SNE','DB','dov','emr','wmt','axp','trow','xom','ev','gpc','pm','cvx','jnj','mmm','txn','mo','fast','sbsi','ul','ohi','cl','mcd','flo','clx','adp','el','mkc','pg','pep','cost','nke','yum','hsy','wpc','ohi','ravn','kmb','WDI.DE','RKET.DE','HEIA.AS','ATVI','EA','NSRGF','NFLX','AVGO','KEY'
               ]
stockArray = [
        'RKET.DE'
               ]

stockArray2 = [
'TXG','YI','PIH','PIHPP','TURN','FLWS','BCOW','FCCY','SRCE','VNET','TWOU','QFIN','KRKR','JOBS','ETNB','JFK','JFKKR','JFKKU','JFKKW','EGHT','JFU','AAON','ABEO','ABEOW','ABIL','ABMD','AXAS','ACIU','ACIA','ACTG','ACHC','ACAD','ACAM','ACAMU','ACAMW','ACST','AXDX','XLRN','ARAY','ACRX','ACER','ACHV','ACHN','ACIW','ACRS','ACMR','ACNB','ACOR','ACTT','ACTTU','ACTTW','ATVI','ADMS','ADMP','AHCO','AHCOW','ADAP','ADPT','ADUS','AEY','IOTS','ADIL','ADILW','ADMA','ADBE','ADTN','ADRO','ADES','AEIS','AMD','ADXS','ADVM','DWMC','DWSH','ACT','AEGN','AGLE','AEHR','AMTX','AERI','AVAV','ARPO','AIH','AEZS','AEMD','GNMX','AFMD','AFYA','AGBA','AGBAR','AGBAU','AGBAW','AGEN','AGRX','AGYS','AGIO','AGMH','AGNC','AGNCB'
               ]

blueStackNames = [
    '1st Source ','3M ','A. O. Smith ','Aaron ','Abbott Laboratories','AbbVie ','ABM Industries ','Accenture Plc','Aflac ','Air Products & Chemicals ','Albemarle ','Alliant Energy ','Altria Group ','American Equity Investment Life Holding ','American Financial Group ','American States Water ','American Water Works  ','AmeriGas Partners LP','Ameriprise Financial ','AmerisourceBergen ','Analog Devices ','AptarGroup ','Aqua America ','Archer-Daniels-Midland ','Assurant ','AT&T ','Atmos Energy ','Atrion ','Automatic Data Processing ','AXIS Capital Holdings Ltd.','Badger Meter ','Balchem ','BancFirst  (Oklahoma)','Bank of Marin Bancorp','Bank OZK','Becton Dickinson & ','Best Buy  ','Black Hills ','BOK Financial ','Brady ','Broadridge Financial Solutions ','Brookfield Infrastructure Partners LP','Brown & Brown ','Brown-Forman ','Bunge Ltd.','C.H. Robinson Worldwide ','California Water Service Group','Cardinal Health ','Carlisle Cos.'
]
analyser = Lamalyse()
analyser.debug = debug

if debug :
    data = analyser.createCsv(['AAPL','AAPL'])
    print(data)
else:
    data = analyser.createCsv(blueStackNames)

print("successfully updated analyse")
