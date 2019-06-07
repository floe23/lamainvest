import pytest
from manager.apiManager import ApiManager

@pytest.fixture
def startClass():
    startClass = ApiManager()
    return startClass

# def test_default_initial_amount(startClass):
#     response = startClass.getYahooStockAnalyisis('NBEV')
#     assert response['quoteType']['shortName']== 'New Age Beverages Corporation'

def test_writeDataToGoogleSheet(startClass):
    response = startClass.writeDataToGoogleSheet('NBEV')
    assert response == "moin moin"
