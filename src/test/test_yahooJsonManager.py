import pytest
from manager.yahooJsonManager import YahooJsonManager
import json


# from yahooTestJson import testData
# testData = json.load(testData)
with open('test/yahooTestJson.json', 'r') as myfile:
    testJson=myfile.read()
testJson = json.loads(testJson)

@pytest.fixture
def startClass():
    startClass = YahooJsonManager()
    startClass.setStock('NBEV')
    return startClass

#comment this for not exeeding limit by testing
# def test_getJson(startClass):
#     startClass.getJson()
#     assert startClass.jsonData['quoteType']['shortName']== 'New Age Beverages Corporation'

def test_getKeyData(startClass):
    startClass.jsonData=testJson
    keyData = startClass.getKeyData()
    assert keyData['shortName'] == 'New Age Beverages Corporation'
    assert len(keyData['longBusinessSummary']) >= 50
    assert keyData['returnOnEquity'] == -0.107259996
    assert keyData['dividendYield'] == 33453
    assert keyData['payoutRatio'] == 0
    assert keyData['price'] == 5.06
    assert keyData['priceToEarnings'] == 5.06/0.09
