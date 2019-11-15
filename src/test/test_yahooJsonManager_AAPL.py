import pytest
from src.manager.yahooJsonManager import YahooJsonManager
import json


# from yahooTestJson import testData
# testData = json.load(testData)
with open('src/test/testDataDetail_AAPL.json', 'r') as myfile:
    testJson=myfile.read()
testJson = json.loads(testJson)

with open('src/test/testDataHistory_AAPL.json', 'r') as myfile1:
    testJsonHist=myfile1.read()
testJsonHist = json.loads(testJsonHist)

@pytest.fixture
def startClass():
    startClass = YahooJsonManager()
    startClass.setStock('AAPL')
    startClass.jsonDataDetail=testJson
    startClass.jsonDataDetailHistory=testJsonHist
    return startClass

#comment this for not exeeding limit by testing
# def test_getJson(startClass):
#     startClass.getJson()
#     assert startClass.jsonDataDetail['quoteType']['shortName']== 'New Age Beverages Corporation'

def test_getKeyData(startClass):
    startClass.jsonDataDetail=testJson
    keyData = startClass.getKeyData()
    assert keyData['stockSymbol'] == 'AAPL'
    assert keyData['shortName'] == 'Apple Inc.'
    assert len(keyData['longBusinessSummary']) >= 50
    assert keyData['returnOnEquity'] == 0.49128
    assert keyData['dividendYield'] == 0.0176
    assert keyData['priceToEarnings'] == 194.19/12.69
    assert keyData['price'] == 194.19
    assert keyData['payoutRatio'] == 0.2446
    assert keyData['yearlyRevenueTendency'] == 0.14
    assert keyData['revenueYearlyRating'] == "--"
    assert keyData['yearlyEarningsTendency'] == 0.15
    assert keyData['quarterlyEarningsTendency'] == 0.22
    assert keyData['earningsYearlyRating'] == "-"
    assert keyData['earningsQuarterlyRating'] == "+"
    assert keyData['buyRating'] == "---"
    assert keyData['peRating'] == "++"
    assert keyData['stockPriceFiveYearChange'] == 1.1
    assert keyData['stockPriceThreeYearChange'] == 0.8
    assert keyData['stockPriceOneYearChange'] == -0.13
    assert keyData['dividendYieldRating'] == "😃"
    assert keyData['payoutRatioRating'] == "😃"
    assert keyData['returnOnEquityRating'] == "😃"


def test_calculateGrowthSum(startClass):
    checkArray = [10,20,-10,30, -10,-20]
    tendency = startClass.calculateGrowthSum(checkArray)
    assert tendency == 1.17

def test_calculatePriceRating(startClass):
    priceRating = startClass.calculatePriceRating(1,400)
    assert priceRating == "+++"
    priceRating = startClass.calculatePriceRating(70,400)
    assert priceRating == "++"
    priceRating = startClass.calculatePriceRating(200,400)
    assert priceRating == "+"
    priceRating = startClass.calculatePriceRating(235,400)
    assert priceRating == "-"
    priceRating = startClass.calculatePriceRating(315,400)
    assert priceRating == "--"
    priceRating = startClass.calculatePriceRating(355,400)
    assert priceRating == "---"
    priceRating = startClass.calculatePriceRating(450,400)
    assert priceRating == "---"

def test_calculateGrowthRating(startClass):
    tendencyRating = startClass.calculateGrowthRating(0.6)
    assert tendencyRating == "+++"
    tendencyRating = startClass.calculateGrowthRating(0.4)
    assert tendencyRating == "++"
    tendencyRating = startClass.calculateGrowthRating(0.2)
    assert tendencyRating == "+"
    tendencyRating = startClass.calculateGrowthRating(0.15)
    assert tendencyRating == "-"
    tendencyRating = startClass.calculateGrowthRating(0.1)
    assert tendencyRating == "--"
    tendencyRating = startClass.calculateGrowthRating(0.03)
    assert tendencyRating == "---"
    tendencyRating = startClass.calculateGrowthRating(-1)
    assert tendencyRating == "---"

def test_getRevenueListYearly(startClass):
    earningsList = startClass.getRevenueListYearly()
    assert earningsList == [233715000000, 215639000000, 229234000000, 265595000000]

def test_getRevenueListQuartarly(startClass):
    earningsList = startClass.getRevenueListQuarterly()
    assert earningsList == [53265000000, 62900000000, 84310000000, 58015000000]

def test_getRevenueListYearly(startClass):
    earningsList = startClass.getRevenueListYearly()
    assert earningsList == [233715000000, 215639000000, 229234000000, 265595000000]

# Start fake data test
# calculations are in https://docs.google.com/spreadsheets/d/1OeHKTNaILDhxKtBjxPUjetWIe_fima1dj-PGf_a_AMw/edit#gid=182350962


def test_getRevenueListQuarterlyTendency(startClass):
    tendency = startClass.getRevenueListQuarterlyTendency()
    assert tendency == 0.21


def test_getEarningsListQuartarly(startClass):
    earningsList = startClass.getEarningsListQuartarly()
    assert earningsList == [11519000000, 14125000000, 19965000000, 11561000000]
#
def test_getEarningsListYearly(startClass):
    earningsList = startClass.getEarningsListYearly()
    assert earningsList == [53394000000, 45687000000, 48351000000, 59531000000]
#
#
