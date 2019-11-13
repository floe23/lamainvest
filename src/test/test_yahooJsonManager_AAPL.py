import pytest
from manager.yahooJsonManager import YahooJsonManager
import json


# from yahooTestJson import testData
# testData = json.load(testData)
with open('test/testDataDetail_AAPL.json', 'r') as myfile:
    testJson=myfile.read()
testJson = json.loads(testJson)

@pytest.fixture
def startClass():
    startClass = YahooJsonManager()
    startClass.setStock('AAPL')
    startClass.jsonDataDetail=testJson
    return startClass

#comment this for not exeeding limit by testing
# def test_getJson(startClass):
#     startClass.getJson()
#     assert startClass.jsonDataDetail['quoteType']['shortName']== 'New Age Beverages Corporation'

def test_getKeyData(startClass):
    startClass.jsonDataDetail=testJson
    keyData = startClass.getKeyData()
    assert keyData['shortName'] == 'Apple Inc.'
    assert len(keyData['longBusinessSummary']) >= 50
    assert keyData['returnOnEquity'] == 0.49128
    assert keyData['dividendYield'] == 0.0176
    assert keyData['payoutRatio'] == 0.2446
    assert keyData['price'] == 194.19
    assert keyData['priceToEarnings'] == 194.19/12.69
    assert keyData['buyRating'] == 6
    assert keyData['peRating'] == 2
    assert keyData['earningsQuarterlyRating'] == 4
    assert keyData['earningsYearlyRating'] == 1
    assert keyData['revenueYearlyRating'] == 1


def test_analyseTendency(startClass):
    checkArray = [1,2,3,1,5,2]
    tendency = startClass.analyseTendency(checkArray)
    assert tendency >= 0
    checkArray = [10,9,8,10,6,4]
    tendency = startClass.analyseTendency(checkArray)
    assert tendency <= 0

def test_calculatePriceRating(startClass):
    priceRating = startClass.calculatePriceRating(1,400)
    assert priceRating == 1
    priceRating = startClass.calculatePriceRating(70,400)
    assert priceRating == 2
    priceRating = startClass.calculatePriceRating(200,400)
    assert priceRating == 3
    priceRating = startClass.calculatePriceRating(235,400)
    assert priceRating == 4
    priceRating = startClass.calculatePriceRating(315,400)
    assert priceRating == 5
    priceRating = startClass.calculatePriceRating(355,400)
    assert priceRating == 6
    priceRating = startClass.calculatePriceRating(450,400)
    assert priceRating == 6

def test_calculateGrowthRating(startClass):
    tendencyRating = startClass.calculateGrowthRating(0.6)
    assert tendencyRating == 1
    tendencyRating = startClass.calculateGrowthRating(0.4)
    assert tendencyRating == 2
    tendencyRating = startClass.calculateGrowthRating(0.2)
    assert tendencyRating == 3
    tendencyRating = startClass.calculateGrowthRating(0.15)
    assert tendencyRating == 4
    tendencyRating = startClass.calculateGrowthRating(0.1)
    assert tendencyRating == 5
    tendencyRating = startClass.calculateGrowthRating(0.03)
    assert tendencyRating == 6
    tendencyRating = startClass.calculateGrowthRating(-1)
    assert tendencyRating == 6

def test_getEarningsListQuartarly(startClass):
    earningsList = startClass.getEarningsListQuartarly()
    assert earningsList == [2.34, 2.91, 4.18, 2.46]

def test_getEarningsListYearly(startClass):
    earningsList = startClass.getEarningsListYearly()
    assert earningsList == [233715000000, 53394000000, 215639000000, 45687000000]

def test_getRevenueListYearly(startClass):
    earningsList = startClass.getRevenueListYearly()
    assert earningsList == [229234000000, 265595000000, 53265000000, 52160000]


def test_checkPositiveGrowthPercent(startClass):
    checkList = [-0.09, -0.08, -0.18, -0.02]
    positiveGrowth = startClass.checkPositiveGrowthPercent(checkList)
    assert positiveGrowth == False
    checkList = [0.09, -0.08, 0.18, 0.02]
    positiveGrowth = startClass.checkPositiveGrowthPercent(checkList)
    assert positiveGrowth == True


def test_checkPositiveGrowth(startClass):
    #check a good Revenue how many millions
    checkList = [-1103333, -3633079, -3536000, -12135000]
    positiveGrowth = startClass.checkPositiveGrowth(checkList)
    assert positiveGrowth == False
    checkList = [100000, 3633079, 3536000, 12135000]
    positiveGrowth = startClass.checkPositiveGrowth(checkList)
    assert positiveGrowth == False
    checkList = [1000000000, 3633079, 3536000, 12135000]
    positiveGrowth = startClass.checkPositiveGrowth(checkList)
    assert positiveGrowth == True

def test_getEarningsListQuartarlyTendency(startClass):
    tendency = startClass.getEarningsListQuartarlyTendency()
    assert tendency == -1

def test_getEarningsListYearlyTendency(startClass):
    tendency = startClass.getEarningsListYearlyTendency()
    assert tendency == -1
    startClass.jsonDataDetail['earnings']['financialsChart']['yearly'][0]['earnings']['raw'] = 1000000000
    startClass.jsonDataDetail['earnings']['financialsChart']['yearly'][1]['earnings']['raw'] = 1200000000
    startClass.jsonDataDetail['earnings']['financialsChart']['yearly'][2]['earnings']['raw'] = 1300000000
    startClass.jsonDataDetail['earnings']['financialsChart']['yearly'][3]['earnings']['raw'] = 1400000000
    tendency = startClass.getEarningsListYearlyTendency()
    assert tendency >= 0

def test_getRevenueListYearlyTendency(startClass):
    tendency = startClass.getRevenueListYearlyTendency()
    assert tendency == -1
    startClass.jsonDataDetail['earnings']['financialsChart']['yearly'][0]['revenue']['raw'] = 1000000000
    startClass.jsonDataDetail['earnings']['financialsChart']['yearly'][1]['revenue']['raw'] = 1200000000
    startClass.jsonDataDetail['earnings']['financialsChart']['yearly'][2]['revenue']['raw'] = 1300000000
    startClass.jsonDataDetail['earnings']['financialsChart']['yearly'][3]['revenue']['raw'] = 1400000000
    tendency = startClass.getRevenueListYearlyTendency()
    assert tendency >= 0
