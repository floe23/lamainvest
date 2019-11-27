import pytest
from src.manager.apiManager import ApiManager

@pytest.fixture
def startClass():
    startClass = ApiManager()
    return startClass

def test_default_initial_amount(startClass):
    response = startClass.getYahooStockDetail('AAPL')
    assert response['quoteType']['shortName']== 'Apple Inc.'

# def test_default_initial_amount(startClass):
#     response = startClass.getYahooStockHistory('AAPL')
#     assert response['chart']['result'][0]['meta']['symbol']== 'AAPL'

# def test_writeDataToFile(startClass):
#     filePath = 'test/testDataHistory_AAPL.json'
#     jsonData = '{"test":"moin"}'
#     startClass.writeJsonTofile(filePath, jsonData)
#     assert response['quoteType']['shortName']== 'New Age Beverages Corporation'

# def test_writeDataToGoogleSheet(startClass):
#     response = startClass.writeDataToGoogleSheet('NBEV')
#     assert response == "moin moin"
