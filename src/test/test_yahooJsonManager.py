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
    assert keyData['buyRating'] == 2
    assert keyData['peRating'] == 6


def test_analyseTendency(startClass):
    checkArray = [1,2,3,1,5,2]
    tendency = startClass.analyseTendency(checkArray)
    assert tendency >= 0
    checkArray = [10,9,8,10,6,4]
    tendency = startClass.analyseTendency(checkArray)
    assert tendency <= 0


def test_getEarningsListQuartarly(startClass):
    startClass.jsonData=testJson
    earningsList = startClass.getEarningsListQuartarly()
    assert earningsList == [-0.09, -0.08, -0.18, -0.02]

def test_getEarningsListYearly(startClass):
    startClass.jsonData=testJson
    earningsList = startClass.getEarningsListYearly()
    assert earningsList == [-1103333, -3633079, -3536000, -12135000]

def test_getRevenueListYearly(startClass):
    startClass.jsonData=testJson
    earningsList = startClass.getRevenueListYearly()
    assert earningsList == [2421752, 25301806, 52188000, 52160000]
