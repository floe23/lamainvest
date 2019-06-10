import pytest
from manager.lamalyse import Lamalyse
import json


@pytest.fixture
def startClass():
    startClass = Lamalyse()
    return startClass

#comment this for not exeeding limit by testing
# def test_getJson(startClass):
#     startClass.getJson()
#     assert startClass.jsonData['quoteType']['shortName']== 'New Age Beverages Corporation'

def test_wholeFunction(startClass):
    startClass.debug = True
    data = startClass.start('NBEV')
    print(data['price'])
    print(data['priceToEarnings'])
    print(data['payoutRatio'])
    assert 1 == 2
