import pytest
from src.manager.lamalyse import Lamalyse
import json

with open('src/test/testDataDetail_AAPL.json', 'r') as myfile:
    testJson=myfile.read()
testJson = json.loads(testJson)

with open('src/test/testDataHistory_AAPL.json', 'r') as myfile1:
    testJsonHist=myfile1.read()
testJsonHist = json.loads(testJsonHist)

@pytest.fixture
def startClass():
    startClass = Lamalyse()
    startClass.debug = True
    startClass.stockSymbolList = ['AAPL']
    startClass.getYahooDataInfo()
    return startClass

#comment this for not exeeding limit by testing
# def test_getJson(startClass):
#     startClass.getJson()
#     assert startClass.jsonData['quoteType']['shortName']== 'New Age Beverages Corporation'

def test_getKeyData(startClass):
    keyData = startClass.dataList[0]
    assert keyData['stockSymbol'] == 'AAPL'
    assert keyData['shortName'] == 'Apple Inc.'
    assert keyData['returnOnEquity'] == 0.49128
    assert keyData['dividendYield'] == 0.0176
    assert keyData['price'] == 194.19
    assert keyData['payoutRatio'] == 0.2446


def test_setCalculatedValues(startClass):
    keyData = startClass.dataList[0]
    assert keyData['priceToEarnings'] == 194.19/12.69
    assert keyData['yearlyRevenueTendency'] == 0.14
    assert keyData['yearlyEarningsTendency'] == 0.15
    assert keyData['quarterlyEarningsTendency'] == 0.22
    assert keyData['stockPriceFiveYearChange'] == 1.1
    assert keyData['stockPriceThreeYearChange'] == 0.8
    assert keyData['stockPriceOneYearChange'] == -0.13
#
def test_setRatings(startClass):
    keyData = startClass.dataList[0]
    assert keyData['revenueYearlyRating'] == 6
    assert keyData['earningsYearlyRating'] == 7
    assert keyData['earningsQuarterlyRating'] == 8
    assert keyData['buyRating'] == 3
    assert keyData['peRating'] == 7
    assert keyData['dividendYieldRating'] == "😃"
    assert keyData['payoutRatioRating'] == "😃"
    assert keyData['returnOnEquityRating'] == "😃"
